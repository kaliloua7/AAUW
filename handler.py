import os.path
from docx import Document


def retrieve_text(pth):
    doc=Document(pth)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return ' '.join(fullText)

def retrieve_text2(pth):
    doc=Document(pth)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return fullText

def retrieve_image(pth):
    return ""


