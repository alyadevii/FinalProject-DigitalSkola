import streamlit as st
from ml_app import run_ml_app

def main():
    menu = ['Home', 'Machine Learning']
    choice = st.sidebar.selectbox('Menu', menu) 

    if choice == 'Home':
        st.title('Welcome to Final Project Data Sapiens Home Page')
        st.write('Ini adalah website deploy kelompok 1 (Data Sapiens) untuk mengklasifikasikan pendapatan seseorang ke dalam dua kategori, yaitu pendapatan kurang dari atau sama dengan 50 ribu dolar (<=50K) dan lebih dari 50 ribu dolar (>50K). Prediksi ini didasarkan pada berbagai atribut demografis dan pekerjaan seperti usia, jenis pekerjaan, tingkat pendidikan, status pernikahan, ras, jenis kelamin, jam kerja per minggu, serta informasi finansial seperti keuntungan atau kerugian modal. Dengan menggunakan data tersebut, model dapat membantu memperkirakan tingkat pendapatan seseorang berdasarkan karakteristik individu tersebut.')
        st.image('https://img.freepik.com/premium-vector/salary-vector-concept-male-worker-female-looking-his-salary-while-standing-with-big-calendar_199064-209.jpg')  # Ganti URL gambar sesuai kebutuhan
    elif choice == 'Machine Learning':
        run_ml_app()
        
if __name__ == '__main__':
    main()
