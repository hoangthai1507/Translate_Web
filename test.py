import requests
from fpdf import FPDF
import streamlit
import streamlit as st
import gpt
import getdata
import arg
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from PIL import Image
from reportlab.lib.utils import ImageReader

from reportlab.pdfgen import canvas
from PyPDF2 import PdfFileReader, PdfWriter
import io

def create_pdf(file_name, title, content):
    # Create PDF writer object
    pdf_writer = PdfWriter()

    # Create a new PDF page
    pdf_writer.addPage()

    # Set the page title
    pdf_writer.setTitle(title)

    # Set the page content
    stream = io.StringIO()
    for line in content:
        stream.write(line)
    pdf_writer.write(stream)

    # Save the PDF file
    with open(file_name, "wb") as out_file:
        pdf_writer.write(out_file)

gt = getdata
N_pages = 1
title = gt.get_title(arg.url)
# label = title[0]
# link = gt.get_link_by_title(label,arg.url)
# content = gt.get_content(link)
# print(type(content))
# for i in range (N_pages):
#             label = title[i]
#             label_translate = label
#             link = gt.get_link_by_title(label,arg.url)
#             tag = gt.get_tag(link)
#             img = gt.get_main_image_vnexpress(link)
#             caption = gt.get_caption_image(link)
#             content = gt.get_content(link)
#             create_pdf(content,label_translate)



label = title[0]
label_translate = label
link = gt.get_link_by_title(label,arg.url)
tag = gt.get_tag(link)
# img = gt.get_main_image_vnexpress(link)
# caption = gt.get_caption_image(link)
content = gt.get_content(link)
name_file = "save_pdf/" + label +  ".pdf" 
create_pdf(name_file,content,label)