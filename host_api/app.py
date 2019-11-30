import flask
from flask import request, jsonify
from flask_restful import Resource, Api
import visionAPI, lineSegmenter, fuzzyMatching, scheduleMaker
import io, sys
import base64

app = flask.Flask(__name__)
app.config["DEBUG"] = True


api=Api(app)


#path for testing image (get request)
path = "test_img1.jpeg"

#initialise data for fuzzy match
fuzzyMatching.initialise_data()


def convert_and_save(b64_string):

#     b64_string += '=' * (-len(b64_string) % 4)  # restore stripped '='s
#     string = b'{b64_string}'
#     with open("imageToSave.jpeg", "wb") as fh:
#         fh.write(base64.decodebytes(string))

    with open("imageToSave.jpeg", "wb") as fh:
#         fh.write(base64.decodebytes(b64_string.encode()))
        fh.write(base64.decodebytes(b64_string))


@app.route('/prepareSchedule', methods=['GET', 'POST'])   #change it to post and take image from body
def prepSchedule():
    
    
#     input_image is to be taken from the body of request for POST request
    if request.method == 'POST':

#         base64Stream = request.get_data()
#         print(vase64Stream , file=sys.stderr)
#         input_image = base64.decodestring(base64Stream)
        
#         data = request.get_json()
#         img_data = data['img']
        img_data = request.get_data() #for body
        
        print(img_data, file=sys.stderr)
        
        convert_and_save(img_data)
        path = "imageToSave.jpeg"
        with io.open(path, 'rb') as image_file:
            input_image = image_file.read()
    
    vision_api_output =  visionAPI.detect_document(input_image)
    print(vision_api_output , file=sys.stderr)
    lines = lineSegmenter.lineSegmenter(vision_api_output)
    print(lines , file=sys.stderr)
    medicine_lines = fuzzyMatching.detect_lines_with_medicine(lines)
    print(medicine_lines , file=sys.stderr)
    schedules = scheduleMaker.schedulePredicter(medicine_lines)
    print(schedules , file=sys.stderr)
    outputJSON=[]
    for sch in schedules:
        outputJSON.append(vars(sch))
    print(outputJSON , file=sys.stderr)
    
#     l=""
#     for line in medicine_lines:
#         l = l.join(line)
    
    return jsonify(outputJSON)
app.run()