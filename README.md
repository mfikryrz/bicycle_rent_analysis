# 🚲 Bicycle Rental Analysis Dashboard

This project is an interactive data analysis dashboard built with **Streamlit**. It visualizes and explores patterns in a bike rental dataset, helping users understand trends in rentals based on **hour**, **month**, **weather**, and **season**. The data spans the years **2011 and 2012**.

> 📊 The project includes a Jupyter Notebook (`Proyek_Analisis_Data.ipynb`) for exploratory analysis, and a dashboard app (`dashboard/dashboard.py`) for interactive data visualization.

---

## 📂 Project Structure

```
bicycle_rent_analysis/
│
├── dataset/
│   ├── day_cleaned.csv         # Daily aggregated rental data
│   └── hour_cleaned.csv        # Hourly rental data
│
├── dashboard/
│   └── dashboard.py            # Streamlit dashboard application
│
├── Proyek_Analisis_Data.ipynb  # Jupyter notebook for data exploration
└── README.md
```

---

## 💡 Features

✅ Interactive sidebar to filter by year (2011 or 2012)
✅ Hourly rental trends: total, casual, and registered users
✅ Monthly rental trends and seasonal patterns
✅ Weather conditions over time (temperature, humidity, wind speed)
✅ Real-time visualization using **matplotlib** and **seaborn**
✅ Summary metrics per season/year

---

## 📈 Dataset Description

The dataset includes:

* `hour_cleaned.csv`: Hourly aggregated rental data
* `day_cleaned.csv`: Daily aggregated rental data

Each file includes columns such as:

* `cnt`: total bike rentals
* `casual`: unregistered user rentals
* `registered`: registered user rentals
* `temp`, `hum`, `windspeed`: weather indicators
* `season`, `yr`, `mnth`, `hr`: time and seasonal identifiers

---

## 🚀 Running the Dashboard

To run the dashboard locally:

### 1. Install dependencies

```bash
pip install requirements.txt
```

### 2. Start the dashboard

```bash
streamlit run dashboard/dashboard.py
```

> Make sure `day_cleaned.csv` and `hour_cleaned.csv` are located in the correct path relative to the script.

---

## 📗 Notebook: Exploratory Analysis

You can also explore the dataset step-by-step in the provided Jupyter notebook:

```bash
jupyter notebook Proyek_Analisis_Data.ipynb
```

The notebook includes:

* Correlation analysis
* Data cleaning
* Feature engineering
* Visualization of usage trends

---

## ✍️ Author

**Muhammad Fikry Rizal**
📫 [muh.fikryrizal@gmail.com](mailto:muh.fikryrizal@gmail.com)

---

## 📄 License

This project is open-source and free to use for learning and research purposes.
