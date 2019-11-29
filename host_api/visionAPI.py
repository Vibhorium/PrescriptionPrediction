# To run this always set GOOGLE_APPLICATION_CREDENTIALS on the same anaconda prompt first
def detect_document(input_image):
    """Detects document features in an image."""
    from google.cloud import vision
    import io
    client = vision.ImageAnnotatorClient.from_service_account_file("api-key.json")
    
#     client = vision.Client.from_service_account_json(
#         'service_account.json')

    # Sending image in its pure form not as path of file
#     with io.open(path, 'rb') as image_file:
#         content = image_file.read()

    content = input_image

    image = vision.types.Image(content=content)

    response = client.document_text_detection(image=image)

    Output = ""
    
    for page in response.full_text_annotation.pages:
        for block in page.blocks:
           
            for paragraph in block.paragraphs:
               
                for word in paragraph.words:
                    word_text = ''.join([
                        symbol.text for symbol in word.symbols
                    ])
                    Output += word_text +' '
                    
    return Output