import os.path
from docx import Document


def retrieve_text(pth):
    doc=Document(pth)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)

def retrieve_text2(pth):
    doc=Document(pth)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return fullText


