import streamlit as st
from PIL import Image, ImageDraw
import numpy as np
from collections import Counter

def get_hex_color_codes(image, area, num_colors=20):
    # Resmin işlenecek alanını kes
    cropped_image = image.crop(area)
    # Resmi numpy dizisine dönüştür
    np_image = np.array(cropped_image)
    # Tüm pikselleri (w, h, 3) şeklinde düzleştir
    pixels = np_image.reshape(-1, np_image.shape[-1])
    # En yaygın renkleri say
    counts = Counter(map(tuple, pixels))
    # En sık kullanılan renkleri al
    most_common = counts.most_common(num_colors)

    hex_colors = []
    for color, count in most_common:
        # RGB'den HEX'e dönüştür
        hex_color = '#{:02x}{:02x}{:02x}'.format(*color)
        # Renklerin oranını hesapla
        percentage = (count / len(pixels)) * 100
        hex_colors.append({'hex': hex_color, 'percentage': percentage})

    return hex_colors

def display_colors(hex_colors):
    for color in hex_colors:
        st.markdown(
            f"<div style='display: inline-flex; align-items: center; justify-content: center; width: 100px; height: 50px; background-color: {color['hex']}; color: #fff; margin: 10px; border-radius: 10px;'>{color['hex']}<br>({color['percentage']:.2f}%)</div>",
            unsafe_allow_html=True)

def highlight_processed_area(image, area):
    """ İşlenen alanı göstermek için resmin üzerine bir dikdörtgen çizer. """
    draw = ImageDraw.Draw(image)
    draw.rectangle(area, outline='red', width=3)
    return image

def main():
    st.title("Resimden Hex Renk Kodu Çıkarıcı")
    uploaded_file = st.file_uploader("Bir resim dosyası yükle (PNG, JPEG, JPG)", type=["png", "jpeg", "jpg"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file).convert('RGB')

        # İşlenecek alanın koordinatları (örnek: resmin orta kısmı)
        processed_area = (40, 40, 100, 100)

        # İşlenen alanı vurgulayın
        image_with_highlight = highlight_processed_area(image.copy(), processed_area)

        hex_codes = get_hex_color_codes(image, processed_area)
        st.write("En Sık Bulunan 20 Hex Renk Kodu:")
        display_colors(hex_codes)

        # Yüklenen ve işlenen resmi göster
        st.image(image_with_highlight, caption='İşlenen Alanı Vurgulanan Resim', use_column_width=True)

if __name__ == "__main__":
    main()
