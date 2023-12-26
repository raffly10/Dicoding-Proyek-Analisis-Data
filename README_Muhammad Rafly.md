# E-Commerce Data Scientist - Dicoding


## Ringkasan
Proyek ini merupakan proyek analisis dan visualisasi data yang berfokus pada data publik e-commerce. Ini mencakup kode untuk perselisihan data, analisis data eksplorasi (EDA), dan dasbor Streamlit untuk eksplorasi data interaktif. Proyek ini bertujuan untuk menganalisis data pada E-Commerce Public Dataset.

## Konstruksi Direktori

- **/DATAREAL**: Direktori ini digunakan untuk proyek analisis data, dan disimpan dalam format .csv atau bisa digunakan menggunakan link raw .
- **/dashboard**: Direktori ini berisi my_streamlit.py yang digunakan untuk membuat dashboard hasil proyek analisis data dan akan ditampilkan di streamlit 
- **Notebook_Muhammad Rafly**: File ini merupakan rekap proyek analisis data.

## Instalasi
1. Clone repository ini ke komputer lokal dengan menggunakan perintah dibawah ini :
    
    ```shell
    git clone https://github.com/raffly10/dicoding-proyek-analisis-data.git
    ```

2. Pastikan terdapat aplikasi Python contohnya menggunakan visual studio code dan pilih pustaka yang diperlukan. Pustaka dapat di instal dengan menjalankan perintah dibawah ini:

   ```shell
   pip install streamlit
   pip install -r dashboard/requirements.txt
   ```  

## Penggunaan
1. **Data Wrangling**: Skrip pengaturan data tersedia di file `Notebook_Muhammad Rafly.ipynb` untuk menyiapkan dan membersihkan data.

2. **Exploratory Data Analysis(EDA)**: Jelajahi dan analisis data menggunakan skrip Python yang disediakan. Wawasan EDA dapat memandu pemahaman tentang pola data publik e-niaga.

3. **Visualization**: Jalankan dashboard Streamlit untuk eksplorasi data interaktif. Untuk menjalankan streamlit lakukan perintah dibawah ini :

  ```shell
  cd dicoding-proyek-analisis-data/dashboard
  streamlit run my_streamlit.
  ```
atau bisa mengunjungi link tautan berikut [E-Commerce Data Dashboard Streamlit App](https://raflymuhammad.streamlit.app/)

## Sumber data
Proyek ini menggunakan Kumpulan Data Publik E-Commerce dari [Belajar Analisis Data dengan Proyek Akhir Python](https://drive.google.com/file/d/1MsAjPM7oKtVfJL_wRp1qmCajtSG1mdcK/view) yang ditawarkan oleh [Dicoding](https://www.dicoding.com/)