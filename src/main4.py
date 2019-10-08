from __future__ import division
from __future__ import print_function

import sys
import argparse
import cv2
import editdistance
from DataLoader import DataLoader, Batch
from Model import Model, DecoderType
from SamplePreprocessor import preprocess
import os
import numpy as np
from PIL import Image
from WordSegmentation import wordSegmentation, prepareImg

linewise_strings=[]
# import image
def getsegmented(path):
    image = cv2.imread(path)
    # cv2.imshow('orig',image)
    # cv2.waitKey(0)

    # grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # cv2.imshow('gray',gray)
    cv2.waitKey(0)

    # binary
    ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)
    # cv2.imshow('second',thresh)
    cv2.waitKey(0)

    # dilation
    kernel = np.ones((5, 100), np.uint8)
    img_dilation = cv2.dilate(thresh, kernel, iterations=1)
    # cv2.imshow('dilated',img_dilation)
    cv2.waitKey(0)

    # find contours
    ctrs, hier = cv2.findContours(img_dilation.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # sort contours
    sorted_ctrs = sorted(ctrs, key=lambda ctr: cv2.boundingRect(ctr)[0])
    line_imgs = []
    line_path = '../data2/'
    for i, ctr in enumerate(sorted_ctrs):
        # Get bounding box
        x, y, w, h = cv2.boundingRect(ctr)

        # Getting ROI
        roi = image[y:y + h , x:x + w]
        line_imgs.append(roi)
        filename = str(i) + '.png'
        cv2.imwrite(line_path + filename, roi)
        # show ROI
        # cv2.imshow('segment no:'+str(i),roi)
        cv2.rectangle(image, (x, y), (x + w, y + h), (90, 0, 255), 2)
        cv2.waitKey(0)

    cv2.imshow('marked areas', image)
    cv2.waitKey(0)
    return line_imgs


imgFiles = os.listdir('../data2/')
segmented_files = os.listdir('../out/')


def change_contrast(img, level):
    factor = (259 * (level + 255)) / (255 * (259 - level))

    def contrast(c):
        return 128 + factor * (c - 128)

    return img.point(contrast)


def convInputImg2(img):
    # cv2.imshow("img",img)

    # -----Converting image to LAB Color model-----------------------------------
    lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    # cv2.imshow("lab",lab)

    # -----Splitting the LAB image to different channels-------------------------
    l, a, b = cv2.split(lab)
    # cv2.imshow('l_channel', l)
    # cv2.imshow('a_channel', a)
    # cv2.imshow('b_channel', b)

    # -----Applying CLAHE to L-channel-------------------------------------------
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
    cl = clahe.apply(l)
    # cv2.imshow('CLAHE output', cl)

    # -----Merge the CLAHE enhanced L-channel with the a and b channel-----------
    limg = cv2.merge((cl, a, b))
    # cv2.imshow('limg', limg)

    # -----Converting image from LAB Color model to RGB model--------------------
    final = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)
    # cv2.imshow('final', final)
    return final


def convInputImg(img):
    # img = cv2.imread('in.png', cv2.IMREAD_GRAYSCALE)

    # increase contrast
    pxmin = np.min(img)
    pxmax = np.max(img)
    imgContrast = (img - pxmin) / (pxmax - pxmin) * 255

    # increase line width
    kernel = np.ones((3, 3), np.uint8)
    imgMorph = cv2.erode(imgContrast, kernel, iterations=1)

    # write
    # cv2.imwrite('out.png', imgMorph)
    return imgMorph


def main():
    """reads images from data/ and outputs the word-segmentation to out/"""

    # read input images from 'in' directory
    print(imgFiles)
    for (i, f) in enumerate(imgFiles):
        # read image, prepare it by resizing it to fixed height and converting it to grayscale
        img = cv2.imread('../data2/' + f)
        print(img.shape)
        h = img.shape[0]
        w = img.shape[1]
        #if ((w / h) < 6):
        #   continue
        print(f)
        print('Segmenting words of sample %s' % f)
        # img=convInputImg(img)
        img2 = prepareImg(cv2.imread('../data2/%s' % f), 50)
        img = convInputImg(img2)
        # img=convInputImg2(img)
        # cv2.imshow('hello',img)
        # execute segmentation with given parameters
        # -kernelSize: size of filter kernel (odd integer)
        # -sigma: standard deviation of Gaussian function used for filter kernel
        # -theta: approximated width/height ratio of words, filter function is distorted by this factor
        # - minArea: ignore word candidates smaller than specified area
        res = wordSegmentation(img, kernelSize=25, sigma=11, theta=7, minArea=100)

        # write output to 'out/inputFileName' directory
        if not os.path.exists('../out/%s' % f):
            os.mkdir('../out/%s' % f)

        # iterate over all segmented words
        print('Segmented into %d words' % len(res))
        for (j, w) in enumerate(res):
            (wordBox, wordImg) = w
            (x, y, w, h) = wordBox
            cv2.imwrite('../out/%s/%d.png' % (f, j), wordImg)  # save word
            cv2.rectangle(img, (x, y), (x + w, y + h), 0, 1)  # draw bounding box in summary image

        # output summary image with bounding boxes around words
        cv2.imwrite('../out/%s/summary.png' % f, img)


class FilePaths:
    "filenames and paths to data"
    fnCharList = '../model/charList.txt'
    fnAccuracy = '../model/accuracy.txt'
    fnTrain = '../data/'
    fnInfer = '../data/4.png'
    fnCorpus = '../data/corpus.txt'


def train(model, loader):
    "train NN"
    epoch = 0  # number of training epochs since start
    bestCharErrorRate = float('inf')  # best valdiation character error rate
    noImprovementSince = 0  # number of epochs no improvement of character error rate occured
    earlyStopping = 5  # stop training after this number of epochs without improvement
    while True:
        epoch += 1
        print('Epoch:', epoch)

        # train
        print('Train NN')
        loader.trainSet()
        while loader.hasNext():
            iterInfo = loader.getIteratorInfo()
            batch = loader.getNext()
            loss = model.trainBatch(batch)
            print('Batch:', iterInfo[0], '/', iterInfo[1], 'Loss:', loss)

        # validate
        charErrorRate = validate(model, loader)

        # if best validation accuracy so far, save model parameters
        if charErrorRate < bestCharErrorRate:
            print('Character error rate improved, save model')
            bestCharErrorRate = charErrorRate
            noImprovementSince = 0
            model.save()
            open(FilePaths.fnAccuracy, 'w').write(
                'Validation character error rate of saved model: %f%%' % (charErrorRate * 100.0))
        else:
            print('Character error rate not improved')
            noImprovementSince += 1

        # stop training if no more improvement in the last x epochs
        if noImprovementSince >= earlyStopping:
            print('No more improvement since %d epochs. Training stopped.' % earlyStopping)
            break


def validate(model, loader):
    "validate NN"
    print('Validate NN')
    loader.validationSet()
    numCharErr = 0
    numCharTotal = 0
    numWordOK = 0
    numWordTotal = 0
    while loader.hasNext():
        iterInfo = loader.getIteratorInfo()
        print('Batch:', iterInfo[0], '/', iterInfo[1])
        batch = loader.getNext()
        (recognized, _) = model.inferBatch(batch)

        print('Ground truth -> Recognized')
        for i in range(len(recognized)):
            numWordOK += 1 if batch.gtTexts[i] == recognized[i] else 0
            numWordTotal += 1
            dist = editdistance.eval(recognized[i], batch.gtTexts[i])
            numCharErr += dist
            numCharTotal += len(batch.gtTexts[i])
            print('[OK]' if dist == 0 else '[ERR:%d]' % dist, '"' + batch.gtTexts[i] + '"', '->',
                  '"' + recognized[i] + '"')

    # print validation result
    charErrorRate = numCharErr / numCharTotal
    wordAccuracy = numWordOK / numWordTotal
    print('Character error rate: %f%%. Word accuracy: %f%%.' % (charErrorRate * 100.0, wordAccuracy * 100.0))
    return charErrorRate


def infer(model, fnImg):
    "recognize text in image provided by file path"
    print(fnImg)
    img = preprocess(cv2.imread(fnImg, cv2.IMREAD_GRAYSCALE), Model.imgSize)
    batch = Batch(None, [img])
    (recognized, probability) = model.inferBatch(batch, True)
    print('Recognized:', '"' + recognized[0] + '"')
    print('Probability:', probability[0])
    return recognized[0]


def main2():
    "main function"
    # optional command line args
    parser = argparse.ArgumentParser()
    parser.add_argument('--train', help='train the NN', action='store_true')
    parser.add_argument('--validate', help='validate the NN', action='store_true')
    parser.add_argument('--beamsearch', help='use beam search instead of best path decoding', action='store_true')
    parser.add_argument('--wordbeamsearch', help='use word beam search instead of best path decoding',
                        action='store_true')
    parser.add_argument('--dump', help='dump output of NN to CSV file(s)', action='store_true')

    args = parser.parse_args()

    decoderType = DecoderType.BestPath
    if args.beamsearch:
        decoderType = DecoderType.BeamSearch
    elif args.wordbeamsearch:
        decoderType = DecoderType.WordBeamSearch

    # train or validate on IAM dataset
    if args.train or args.validate:
        # load training data, create TF model
        loader = DataLoader(FilePaths.fnTrain, Model.batchSize, Model.imgSize, Model.maxTextLen)

        # save characters of model for inference mode
        open(FilePaths.fnCharList, 'w').write(str().join(loader.charList))

        # save words contained in dataset into file
        open(FilePaths.fnCorpus, 'w').write(str(' ').join(loader.trainWords + loader.validationWords))

        # execute training or validation
        if args.train:
            model = Model(loader.charList, decoderType)
            train(model, loader)
        elif args.validate:
            model = Model(loader.charList, decoderType, mustRestore=True)
            validate(model, loader)

    # infer text on test image
    else:
        print(open(FilePaths.fnAccuracy).read())
        model = Model(open(FilePaths.fnCharList).read(), decoderType, mustRestore=True, dump=args.dump)
        for (i, f) in enumerate(segmented_files):
            print(f)
            imgFolder = os.listdir('../out/' + f + '/')
            imgPath = '../out/' + f + '/'
            s=""
            for j in range(0, len(imgFolder) - 1):
                print(imgFolder[j])
                s=s+infer(model, imgPath + str(imgFolder[j]))
                s=s+" "
            linewise_strings.append(s)
        """
        for i in range(0, len(imgFiles)):
            print(imgFiles[i])
            imgFolder = os.listdir('../out/' + str(imgFiles[i]) + '/')
            imgPath = '../out/' + imgFiles[i] + '/'
            for j in range(0, len(imgFolder) - 1):
                print(imgFolder[j])
                infer(model, imgPath + str(imgFolder[j]))
        """


if __name__ == '__main__':
    line_imgs = getsegmented('../fullimg/15.jpeg')
    main()
    main2()
    k=0
    for i in range(0,len(linewise_strings)):
        if len(linewise_strings[i]) > 5:
            print("Line "+str(k)+":",end=' ')
            print(linewise_strings[i])
            k=k+1
