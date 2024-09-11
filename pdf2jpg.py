# pip install streamlit pdf2image pillow

import streamlit as st
from pdf2image import convert_from_path
from PIL import Image
import os

# Streamlit 애플리케이션 설정
st.title("PDF to JPG Converter")

# PDF 파일 업로드
uploaded_file = st.file_uploader("PDF 파일을 업로드하세요", type=["pdf"])

if uploaded_file is not None:
    # PDF 파일을 임시 저장
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    # PDF 파일을 이미지로 변환
    images = convert_from_path("temp.pdf")

    # 변환된 이미지 저장 및 화면에 출력
    st.write(f"총 {len(images)}개의 페이지가 변환되었습니다.")
    for i, image in enumerate(images):
        # 이미지 파일 저장
        image_path = f"page_{i+1}.jpg"
        image.save(image_path, "JPEG")

        # 이미지 출력
        st.image(image, caption=f"Page {i+1}", use_column_width=True)

        # 이미지 다운로드 버튼
        with open(image_path, "rb") as img_file:
            btn = st.download_button(
                label=f"Page {i+1} 다운로드",
                data=img_file,
                file_name=image_path,
                mime="image/jpeg"
            )

    # 임시 PDF 파일 삭제
    os.remove("temp.pdf")
