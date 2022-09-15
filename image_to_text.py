from paddleocr import PaddleOCR


def get_text_from_image(image_url):
    """
    Get text from image
    :param image_url: image url
    :return: text from image
    """
    ocr = PaddleOCR(use_angle_cls=True, lang="en")
    result = ocr.ocr(image_url)
    text = ""
    for line in result:
        text += line[1][0] + " "
    return text
