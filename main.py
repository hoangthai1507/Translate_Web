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
import createPDF
gt = getdata
pdf = createPDF
# def main():
#     # Phần đầu trang
#     st.sidebar.title('Lựa chọn ngôn ngữ')
#     language = st.sidebar.selectbox('Chọn một ngôn ngữ:', arg.language)

#     # Phần thứ hai trang
#     st.sidebar.title('Các bài viết')
#     button_labels =  gt.get_title(arg.url)# list các label của các button
#     for label in button_labels:
#         if st.sidebar.button(label):        
#             label_translate, tag, img, caption, content = gpt.preprocess_data(label,language)
#             st.title(f'{label_translate}')
#             st.write(tag)
#             st.image(img, caption= caption)
#             for line in content:
#                 st.write(line)

def main():
    # Phần đầu trang
    button_labels =  gt.get_title(arg.url)# list các label của các button
    st.sidebar.title('Lựa chọn ngôn ngữ')
    language = st.sidebar.selectbox('Chọn một ngôn ngữ:', arg.language)

    # Thêm trường nhập số
    num_input = st.sidebar.number_input('số bài báo:', min_value=1, max_value=10)
    
    # Thêm nút "In ra PDF"
    if st.sidebar.button('In ra PDF'):
        # Lấy nội dung hiển thị trên trang
        for news in range(num_input):
            label = button_labels[news]
            label_translate,content = gpt.preprocess_data_2(label,language)
            pdf.write_newspaper_to_pdf(label_translate,content)


    # Phần thứ hai trang
    st.sidebar.title('Các bài viết')
    for label in button_labels:
        if st.sidebar.button(label):        
            label_translate, tag, img, caption, content = gpt.preprocess_data(label,language)
            st.title(f'{label_translate}')
            st.write(tag)
            st.image(img, caption= caption)
            for line in content:
                st.write(line)



 
if __name__ == '__main__':
    main()

# Phần cuối trang

