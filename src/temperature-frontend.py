import streamlit as st
from PIL import Image
import requests
import urllib.request

# header

urllib.request.urlretrieve("https://images.unsplash.com/photo-1584267385494-9fdd9a71ad75?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1470&q=80", "image.jpeg")
image = Image.open("image.jpeg")
st.image(image)
st.title("Temperature Predictor App")
st.markdown('*easy way to predict temperature*')
st.divider()
st.subheader('Type the value then click Predict button.')

# form input

with st.form("iris-app-form"):
    ddd_car = st.selectbox('Arah Angin Terkencang:',
    ('C',
    'N',
    'E',
    'S',
    'W',
    'NE',
    'SE',
    'SW',
    'NW'))

    province_id = st.selectbox('Provinsi Domisili:',
    ('Nanggroe Aceh Darussalam',
    'Sumatera Utara',
    'Sumatera Barat',
    'Riau',
    'Jambi',
    'Sumatera Selatan',
    'Bengkulu',
    'Lampung',
    'Kep. Bangka Belitung',
    'Kep. Riau',
    'DKI Jakarta',
    'Jawa Barat',
    'Jawa Tengah',
    'DI Yogyakarta',
    'Jawa Timur',
    'Banten',
    'Bali',
    'Nusa Tenggara Barat',
    'Nusa Tenggara Timur',
    'Kalimantan Barat',
    'Kalimantan Tengah',
    'Kalimantan Selatan',
    'Kalimantan Timur',
    'Sulawesi Utara',
    'Sulawesi Tengah',
    'Sulawesi Selatan',
    'Sulawesi Tenggara',
    'Gorontalo',
    'Sulawesi Barat',
    'Maluku',
    'Maluku Utara',
    'Papua',
    'Papua Barat',
    'Kalimantan Utara'))

    month = st.selectbox('Bulan:', (
        'Januari',
        'Februari',
        'Maret',
        'April',
        'Mei',
        'Juni',
        'Juli',
        'Agustus',
        'September',
        'Oktober',
        'November',
        'Desember'
    ))

    RH_avg = st.number_input("Rerata Kelembaban (%)", help="Nilai antara 0 - 100")
    RR = st.number_input("Curah Hujan (mm)", help="Nilai harus > 0.")
    ss = st.number_input("Durasi Sinar Matahari (hour)", help="Nilai harus > 0.")
    ff_x = st.number_input("Kecepatan Angin Maksimal (m/s)", help="Nilai harus > 0.")
    ddd_x = st.number_input("Arah Angin Saat Kecepatan Maksimal (°)", help="Nilai antara 1 - 360.")
    ff_avg = st.number_input("Kecepatan Angin Rata-rata (m/s)", help="Nilai harus > 0.")

    # submit button
    submitted = st.form_submit_button("Predict")

    if submitted:
        def choose_ddd_car(ddd_car):
            ddd_car_list={
                "C":[1, 0, 0, 0, 0, 0, 0, 0, 0],
                "E":[0, 1, 0, 0, 0, 0, 0, 0, 0],
                "N":[0, 0, 1, 0, 0, 0, 0, 0, 0],
                "NE":[0, 0, 0, 1, 0, 0, 0, 0, 0],
                "NW":[0, 0, 0, 0, 1, 0, 0, 0, 0],
                "S":[0, 0, 0, 0, 0, 1, 0, 0, 0],
                "SE":[0, 0, 0, 0, 0, 0, 1, 0, 0],
                "SW":[0, 0, 0, 0, 0, 0, 0, 1, 0],
                "W":[0, 0, 0, 0, 0, 0, 0, 0, 1]
            }
            option_ddd_car = ddd_car_list[ddd_car]
            return option_ddd_car
        ddd_car = choose_ddd_car(ddd_car)

        
        # match ddd_car:
        #     case "C":
        #         ddd_car = [1, 0, 0, 0, 0, 0, 0, 0, 0]
        #     case 'E':
        #         ddd_car = [0, 1, 0, 0, 0, 0, 0, 0, 0]
        #     case 'N':
        #         ddd_car = [0, 0, 1, 0, 0, 0, 0, 0, 0]
        #     case 'NE':
        #         ddd_car = [0, 0, 0, 1, 0, 0, 0, 0, 0]
        #     case 'NW':
        #         ddd_car = [0, 0, 0, 0, 1, 0, 0, 0, 0]
        #     case 'S':
        #         ddd_car = [0, 0, 0, 0, 0, 1, 0, 0, 0]
        #     case 'SE':
        #         ddd_car = [0, 0, 0, 0, 0, 0, 1, 0, 0]
        #     case 'SW':
        #         ddd_car = [0, 0, 0, 0, 0, 0, 0, 1, 0]
        #     case 'W':
        #         ddd_car = [0, 0, 0, 0, 0, 0, 0, 0, 1]

        month_list={
            "Januari":[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            "Februari":[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            "Maret":[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            "April":[0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            "Mei":[0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            "Juni":[0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
            "Juli":[0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            "Agustus":[0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
            "September":[0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
            "Oktober":[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            "November":[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
            "Desember":[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
            }
        
        def choose_month(month):
            option_month = month_list[month]
            return option_month
        month = choose_month(month)
        
        # match month:
        #     case 'Januari':
        #         month = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        #     case 'Februari':
        #         month = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        #     case 'Maret':
        #         month = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        #     case 'April':
        #         month = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
        #     case 'Mei':
        #         month = [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
        #     case 'Juni':
        #         month = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
        #     case 'Juli':
        #         month = [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
        #     case 'Agustus':
        #         month = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
        #     case 'September':
        #         month = [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
        #     case 'Oktober':
        #         month = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
        #     case 'November':
        #         month = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
        #     case 'Desember':
        #         month = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
        province_list={
            "Nanggroe Aceh Darussalam":[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            'Sumatera Utara':[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            'Sumatera Barat':[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            'Riau':[0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            'Jambi':[0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            'Sumatera Selatan':[0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            'Bengkulu':[0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            'Lampung':[0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            'Kep. Bangka Belitung':[0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            'Kep. Riau':[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            'DKI Jakarta':[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            'Jawa Barat':[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            'Jawa Tengah':[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            'DI Yogyakarta':[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            'Jawa Timur':[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            'Banten':[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            'Bali':[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            'Nusa Tenggara Barat':[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            'Nusa Tenggara Timur':[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            'Kalimantan Barat':[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            'Kalimantan Tengah':[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            'Kalimantan Selatan':[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            'Kalimantan Timur':[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            'Sulawesi Utara':[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            'Sulawesi Tengah':[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            'Sulawesi Selatan':[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            'Sulawesi Tenggara':[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            'Gorontalo':[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
            'Sulawesi Barat':[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            'Maluku':[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
            'Maluku Utara':[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
            'Papua':[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            'Papua Barat':[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
            'Kalimantan Utara':[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
            }
        def choose_province(province_id):
            option_province = province_list[province_id]
            return option_province
        province_id = choose_province(province_id)
        
            
        # match province_id:
        #     case 'Nanggroe Aceh Darussalam':
        #         province_id = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        #     case 'Sumatera Utara':
        #         province_id = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        #     case 'Sumatera Barat':
        #         province_id = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        #     case 'Riau':
        #         province_id = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        #     case 'Jambi':
        #         province_id = [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        #     case 'Sumatera Selatan':
        #         province_id = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        #     case 'Bengkulu':
        #         province_id = [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        #     case 'Lampung':
        #         province_id = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        #     case 'Kep. Bangka Belitung':
        #         province_id = [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        #     case 'Kep. Riau':
        #         province_id = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        #     case 'DKI Jakarta':
        #         province_id = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        #     case 'Jawa Barat':
        #         province_id = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        #     case 'Jawa Tengah':
        #         province_id = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        #     case 'DI Yogyakarta':
        #         province_id = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        #     case 'Jawa Timur':
        #         province_id = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        #     case 'Banten':
        #         province_id = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        #     case 'Bali':
        #         province_id = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        #     case 'Nusa Tenggara Barat':
        #         province_id = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        #     case 'Nusa Tenggara Timur':
        #         province_id = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        #     case 'Kalimantan Barat':
        #         province_id = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        #     case 'Kalimantan Tengah':
        #         province_id = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        #     case 'Kalimantan Selatan':
        #         province_id = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        #     case 'Kalimantan Timur':
        #         province_id = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        #     case 'Sulawesi Utara':
        #         province_id = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        #     case 'Sulawesi Tengah':
        #         province_id = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        #     case 'Sulawesi Selatan':
        #         province_id = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
        #     case 'Sulawesi Tenggara':
        #         province_id = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
        #     case 'Gorontalo':
        #         province_id = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
        #     case 'Sulawesi Barat':
        #         province_id = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
        #     case 'Maluku':
        #         province_id = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
        #     case 'Maluku Utara':
        #         province_id = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
        #     case 'Papua':
        #         province_id = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
        #     case 'Papua Barat':
        #         province_id = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
        #     case 'Kalimantan Utara':
        #         province_id = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
                    
        data = {
            "ddd_car":ddd_car,
            "month":month,
            "province_id":province_id,
            "RH_avg":RH_avg,
            "RR":RR,
            "ss":ss,
            "ff_x":ff_x,
            "ddd_x":ddd_x,
            "ff_avg":ff_avg
        }
    
        # post request
        response = requests.post('http://backend:8000/predict', json=data)

        # get result
        result = response.json()
        
        # check response
        if result['Code'] == 200:
            st.success(result['Message'])
            st.write(result['Prediction_tavg'])
            st.write(result['Prediction_tn'])
            st.write(result['Prediction_tx'])
        else:
            st.error(result['Message'])
            st.write(result['Error'])
   
   
   
   
   
   
