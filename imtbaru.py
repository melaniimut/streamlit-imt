import streamlit as st

# Fungsi untuk menghitung BMI
def calculate_bmi(weight, height):
    return weight / ((height / 100) ** 2)

# Fungsi untuk mengkategorikan BMI
def categorize_bmi(bmi):
    if bmi < 17:
        return "0 - Kurus kekurangan berat badan tingkat berat"
    elif 17 <= bmi < 18.5:
        return "1 - Kurus kekurangan berat badan tingkat ringan"
    elif 18.5 <= bmi < 25:
        return "2 - Normal"
    elif 25 <= bmi < 27:
        return "3 - Gemuk tingkat ringan"
    else:
        return "4 - Obesitas"

# Layout Streamlit
st.title("Kalkulator Index Massa Tubuh (IMT)")

# Input gender dari pengguna
gender = st.radio("Pilih Jenis Kelamin Anda:", ('Laki-laki', 'Perempuan'))

# Input berat dan tinggi dari pengguna
weight = st.number_input("Masukkan Berat Badan Anda (kg):", min_value=0.0, step=0.1)
height = st.number_input("Masukkan Tinggi Badan Anda (cm):", min_value=0.0, step=0.1)

# Kalkulasi BMI dan kategorinya
if st.button("Hitung IMT"):
    if weight > 0 and height > 0:
        bmi = calculate_bmi(weight, height)
        category = categorize_bmi(bmi)
        st.write(f"Indeks Massa Tubuh Anda adalah: {bmi:.2f}")
        st.write(f"Kategori: {category}")
        if gender == 'Laki-laki':
            st.write("Note: Untuk Laki-laki, massa otot dapat mempengaruhi interpretasi IMT.")
        else:
            st.write("Note: Untuk Perempuan, Faktor seperti omposisi tubuh dan perubahan hormonal dapat mempengaruhi IMT.")
    else:
        st.write("Masukan berat dan tinggi badan yang valid.")
