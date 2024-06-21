from paddleocr import PaddleOCR
from pypdf import PdfReader
import requests
from io import BytesIO


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


def get_text_from_pdf(pdf_url):
    """
    Get text from pdf
    :param pdf_url: pdf url
    :return: text from pdf
    """
    response = requests.get(pdf_url)
    if response.status_code != 200:
        return ""
    pdf_stream = BytesIO(response.content)
    pdf = PdfReader(pdf_stream)
    text = ""
    for page in pdf.pages:
        text += page.extract_text()
    return text
