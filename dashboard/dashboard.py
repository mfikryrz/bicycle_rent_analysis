import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


with st.sidebar:
    
    st.text('Ini merupakan filter')
    
    # Membuat filter untuk tahun
    selected_year = st.selectbox("Select Year", options=[2011, 2012], index=0)
    st.write('Filtering Tahun:', selected_year)

data_day = pd.read_csv('day_cleaned.csv')
data_hour = pd.read_csv('hour_cleaned.csv')
 
# Mapping angka bulan menjadi nama bulan
month_mapping = {
    1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June',
    7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'
}

# Mengubah angka bulan menjadi nama bulan
data_day['mnth'] = data_day['mnth'].map(month_mapping)


# Mengubah 'mnth' menjadi kategori dengan urutan yang benar
data_day['mnth'] = pd.Categorical(data_day['mnth'],
                                       categories=['January', 'February', 'March', 'April', 'May', 'June',
                                                   'July', 'August', 'September', 'October', 'November', 'December'],
                                       ordered=True)

# =================================================== Data hour ======================================================

def total_data_hr(data):
    hourly_trend = data.groupby(['hr']).agg({
        'cnt': 'sum',
        'casual': 'sum',
        'registered': 'sum'}).astype(int).reset_index()
    return hourly_trend

def total_data_year_hr(data, year):
    hourly_trend = data[data['yr'] == year].groupby(['hr']).agg({
        'cnt': 'sum',
        'casual': 'sum',
        'registered': 'sum'}).astype(int).reset_index()
    return hourly_trend

def total_measure_data_hr(data):
    hourly_trend = data.groupby(['hr']).agg({
        'temp': 'mean',
        'hum': 'mean',
        'windspeed': 'mean'}).astype(int).reset_index()
    return hourly_trend

def total_measure_data_year_hr(data, year):
    hourly_trend = data[data['yr'] == year].groupby(['hr']).agg({
        'temp': 'mean',
        'hum': 'mean',
        'windspeed': 'mean'}).astype(int).reset_index()
    return hourly_trend

def total_season_data_hr(data):
    hourly_trend = data.groupby(['season']).agg({'cnt': 'sum'}).astype(int).reset_index().sort_values(by='cnt',ascending=False)
    return hourly_trend

def total_season_data_year_hr(data,year):
    hourly_trend = data[data['yr'] == year].groupby(['season']).agg({
        'cnt': 'sum'}).astype(int).reset_index().sort_values(by='cnt',ascending=False)
    return hourly_trend
# =================================================== Data Day ======================================================
def total_data_mnth(data):
    monthly_trend = data.groupby(['mnth']).agg({
        'cnt': 'sum','casual':'sum','registered':'sum'
        }).reset_index().sort_values(by='mnth')
    return monthly_trend

def total_data_year_mnth(data, year):
    monthly_trend = data[data['yr'] == year].groupby(['mnth']).agg({
        'cnt': 'sum','casual':'sum','registered':'sum'
        }).reset_index().sort_values(by='mnth')
    return monthly_trend

def measurement_data_mnth(data):
    monthly_trend = data.groupby(['mnth']).agg({
        'temp':'mean','atemp':'mean','hum':'mean','windspeed':'mean'
        }).reset_index().sort_values(by='mnth')
    return monthly_trend

def measurement_data_year_mnth(data, year):
    monthly_trend = data[data['yr'] == year].groupby(['mnth']).agg({
        'temp':'mean','atemp':'mean','hum':'mean','windspeed':'mean'
        }).reset_index().sort_values(by='mnth')
    return monthly_trend
# =================================================== Data Visualization ======================================================

def visualize_total_data(data,x):
    # Membuat figure dan axis
    fig, ax = plt.subplots(figsize=(12,6))

    # Plot garis menggunakan ax
    sns.lineplot(x=x, y='cnt', data=data, marker='o', label='Total Rentals', linewidth=2, ax=ax)
    sns.lineplot(x=x, y='casual', data=data, marker='o', label='Casual Users', linestyle='dashed', ax=ax)
    sns.lineplot(x=x, y='registered', data=data, marker='o', label='Registered Users', linestyle='dotted', ax=ax)

    # Menambahkan label dan judul
    if x == 'hr':
        ax.set_xlabel("Hour of the Day (hr)")
        ax.set_ylabel("Number of Rentals")
        ax.set_title("Trend of Bike Rentals")
        ax.set_xticks(range(0, 24))  # Menampilkan semua jam dari 0-23
        ax.legend()
        ax.grid(True)

        # Menampilkan plot
        st.pyplot(fig)
    else:
        ax.set_xlabel("Month of the Year (mnth)")
        ax.set_ylabel("Number of Rentals")
        ax.set_title("Trend of Bike Rentals")
        ax.legend()
        ax.grid(axis='y')

        # Menampilkan plot
        st.pyplot(fig)

def visualize_measurement(data,x):
    # Membuat figure dan axis
    fig, ax = plt.subplots(figsize=(15,6))

    # Plot garis menggunakan ax
    sns.lineplot(x=x, y='temp', data=data, marker='o', label='Temperatur', linewidth=2, ax=ax)
    sns.lineplot(x=x, y='hum', data=data, marker='o', label='Humidity', linestyle='dashed', ax=ax)
    sns.lineplot(x=x, y='windspeed', data=data, marker='o', label='Windspeed', linestyle='dotted', ax=ax)

    # Menambahkan label dan judul
    if x == 'hr':
        ax.set_xlabel("Hour of the Day (hr)")
        ax.set_ylabel("Number of Measurement")
        ax.set_title("Trend of Temperature, Humidity, and Windspeed")
        ax.set_xticks(range(0, 24))  # Menampilkan semua jam dari 0-23
        ax.legend()
        ax.grid(True)
        st.pyplot(fig)
    else:
        ax.set_xlabel("Month of the Year (mnth)")
        ax.set_ylabel("Number of Measurement")
        ax.set_title("Trend of Temperature, Humidity, and Windspeed")
        ax.legend()
        ax.grid(axis='y')
        st.pyplot(fig)

def visualize_season(data,x):
    # Membuat figure dan axis
    fig, ax = plt.subplots(figsize=(12,6))

    # Plot garis menggunakan ax
    sns.barplot(x='season', y='cnt', data=data, palette='coolwarm',ax=ax)

    # Menambahkan label dan judul
    if x == 'hr':
        ax.set_xlabel("Season by the Hour (hr)")
    else:
        ax.set_xlabel("Season by the Month (mnth)")
    ax.set_ylabel("Total Bike Rentals")
    ax.set_title("Total Bike Rentals per Season")
    ax.legend()
    ax.grid(axis='y')

    # Menampilkan plot
    st.pyplot(fig)



st.title('Belajar Analisis Data')
st.subheader(f'Total Sewa Sepeda Tahun Keseluruhan Berdasarkan Jam')
filtered_hour_data = total_data_hr(data_hour)
filtered_hour_season = total_season_data_hr(data_hour)
total_revenue = np.sum(filtered_hour_data['cnt'])
col1, col2, col3 = st.columns([1,1,1])  # Menjadikan kolom tengah lebih besar
with col2:
    st.metric("Total Sewa Sepeda", value=f"{total_revenue:,}")

visualize_total_data(filtered_hour_data,'hr')

col1, col2, col3, col4 = st.columns([1,1,1,1])  # Menjadikan kolom tengah lebih besar
with col1:
    season = 'Fall'
    filtered_hour_season1 = filtered_hour_season[filtered_hour_season['season']==season]
    total_revenue = np.sum(filtered_hour_season1['cnt'])
    st.metric(f"Total Sewa musim {season}", value=f"{total_revenue:,}")
with col2:
    season = 'Summer'
    filtered_hour_season2 = filtered_hour_season[filtered_hour_season['season']==season]
    total_revenue = np.sum(filtered_hour_season2['cnt'])
    st.metric(f"Total Sewa musim {season}", value=f"{total_revenue:,}")
with col3:
    season = 'Winter'
    filtered_hour_season3 = filtered_hour_season[filtered_hour_season['season']==season]
    total_revenue = np.sum(filtered_hour_season3['cnt'])
    st.metric(f"Total Sewa musim {season}", value=f"{total_revenue:,}")
with col4:
    season = 'Spring'
    filtered_hour_season4 = filtered_hour_season[filtered_hour_season['season']==season]
    total_revenue = np.sum(filtered_hour_season4['cnt'])
    st.metric(f"Total Sewa musim {season}", value=f"{total_revenue:,}")
visualize_season(filtered_hour_season,'hr')

if (selected_year == 2011) or (selected_year == 2012):
    filtered_hour_data = total_data_year_hr(data_hour, selected_year)
    filtered_hour_measure = total_measure_data_year_hr(data_hour, selected_year)
    total_revenue = np.sum(filtered_hour_data['cnt'])
    col1, col2, col3 = st.columns([1,1,1])  # Menjadikan kolom tengah lebih besar
    with col2:
        st.metric(f"Total Sewa Sepeda {selected_year}", value=f"{total_revenue:,}")
    st.subheader(f'Total Sewa Sepeda Tahun {selected_year} Berdasarkan Jam')
    visualize_total_data(filtered_hour_data,'hr')
    st.subheader(f'Total Keadaan Cuaca {selected_year} Berdasarkan Jam')
    visualize_measurement(filtered_hour_measure,'hr')
    st.subheader(f'Total Sewa Sepeda Tahun {selected_year} Berdasarkan Musim dalam keseluruhan Jam')
    filtered_hour_season = total_season_data_year_hr(data_hour, selected_year)
    visualize_season(filtered_hour_season,'hr')

# =================================================== Data Day ======================================================
st.subheader(f'Total Sewa Sepeda Tahun Keseluruhan Berdasarkan Bulan ke Bulan')
col1, col2 = st.columns([1,1])  # Menjadikan kolom tengah lebih besar
with col1:
    st.text(f'Total Sewa Keseluruhan')
    filtered_mnth_data = total_data_mnth(data_day)
    visualize_total_data(filtered_mnth_data,'mnth')
with col2:
    if (selected_year == 2011) or (selected_year == 2012):
        st.text(f'Total Sewa Sepeda Tahun {selected_year}')
        filtered_mnth_data = total_data_year_mnth(data_day, selected_year)
        visualize_total_data(filtered_mnth_data,'mnth')

st.subheader(f'Keadaan Cuaca Berdasarkan Bulan ke Bulan')
col1, col2 = st.columns([1,1])  # Menjadikan kolom tengah lebih besar
with col1:
    st.text(f'Keadaan Cuaca Keseluruhan')
    filtered_mnth_measurement = measurement_data_mnth(data_day)
    visualize_measurement(filtered_mnth_measurement,'mnth')
with col2:
    if (selected_year == 2011) or (selected_year == 2012):
        st.text(f'Keadaan Cuaca Tahun {selected_year}')
        filtered_mnth_measurement = measurement_data_year_mnth(data_day,selected_year)
        visualize_measurement(filtered_mnth_measurement,'mnth')
