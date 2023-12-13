import streamlit as st #pip install streamlit
import cv2 #pip install opencv-python
from PIL import Image
import numpy as np
from collections import Counter

def get_hex_color_codes(image):
    image = np.array(image.convert('RGB'))  # Arka planı olmayan resimler için
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    resized_image = cv2.resize(image, (40, 40), interpolation=cv2.INTER_AREA)
    pil_image = Image.fromarray(cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB))

    colors = pil_image.getcolors(40*40)
    total_pixels = sum(count for color, count in colors)
    color_counts = Counter({'#{:02x}{:02x}{:02x}'.format(*color[1]): color[0] for color in colors})
    most_common_colors = color_counts.most_common(20)
    return [(color[0], color[1] / total_pixels * 100) for color in most_common_colors]

def display_color(hex_color, percentage):
    st.markdown(
        f"<div style='display: inline-block; margin: 10px; padding: 10px; background-color: {hex_color}; color: white; border-radius: 5px;'>{hex_color} - {percentage:.2f}%</div>",
        unsafe_allow_html=True)

def main():
    st.title("Resimden Hex Renk Kodu Çıkarıcı")
    uploaded_file = st.file_uploader("Bir resim dosyası yükle (PNG, JPEG, JPG)", type=["png", "jpeg", "jpg"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        hex_codes = get_hex_color_codes(image)
        st.write("En Sık Bulunan 20 Hex Renk Kodu ve Yüzdelikleri:")
        for hex_color, percentage in hex_codes:
            display_color(hex_color, percentage)
        st.image(image, caption='Yüklenen Resim', use_column_width=True)

if __name__ == "__main__":
    main()
