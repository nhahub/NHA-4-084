<div align="center">
<h1>🚗 Car Decision Assistant</h1>
  <img width="1024" height="559" alt="image_7d86d91f-e6af-467e-a710-7a9ec9e6678f" src="https://github.com/user-attachments/assets/95845645-feb9-41e4-9420-20cdc9558f14" />

<p><em>Choose the car that best fits your needs with data-driven insights.</em></p>
<p><a href="https://car-decision-assistant-1.streamlit.app/"><strong>🔗 Live App</strong></a></p>
</div>

## 📋 Overview

**Car Decision Assistant** is an AI-powered platform that analyzes the Egyptian used car market to help buyers find the best vehicle at fair prices. It combines real-time web scraping, data engineering, and machine learning to provide data-driven insights across multiple sources (Hatla2ee, ContactCars, YallaMotor).

The platform leverages a **Medallion Architecture** on **Databricks** to autonomously scrape, clean, and centralize automotive market data, enabling accurate price estimation and market analysis.

---

## 📚 Table of Contents

- [Overview](#-overview)
- [Business Problem & Solution](#-business-problem--solution)
- [Tech Stack](#-tech-stack)
- [Pipeline Architecture](#-pipeline-architecture--etl-flow)
- [Features](#-features)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [Usage](#-usage)
- [Future Enhancements](#-future-enhancements)
- [Team](#-team)

---

## 📊 Business Problem & Solution

### The Problem
The used car market in Egypt suffers from fragmented information:
- **Price Volatility:** Prices fluctuate frequently without clear patterns
- **Scattered Data:** Information dispersed across multiple platforms (Hatla2ee, ContactCars, YallaMotor)
- **Data Quality Issues:** No centralized source of truth for accurate market pricing
- **Inefficient Decision-Making:** Buyers lack data-driven insights to make informed purchases

### The Solution
An end-to-end **Data Engineering pipeline** that:
- ✅ Autonomously scrapes real-time data from multiple sources
- ✅ Cleans and validates data at scale
- ✅ Centralizes information in an AI-ready data warehouse
- ✅ Provides accurate price estimates and market analytics
- ✅ Delivers actionable insights via interactive dashboards

---

## 🛠️ Tech Stack

| Component | Technology |
| :--- | :--- |
| **Data Ingestion** | Selenium, Undetected-Chromedriver, Pandas |
| **Data Warehouse** | Databricks, Delta Lake |
| **Data Processing** | PySpark, SQL |
| **Frontend** | Streamlit |
| **Visualization** | Power BI |
| **Languages** | Python (70.9%), Jupyter Notebooks (69.1%) |
| **Infrastructure** | Cloud-based (Databricks) |

---

## 🏗️ Pipeline Architecture & ETL Flow

We built a robust, scalable **Data Warehouse** leveraging **Databricks** and the **Medallion Architecture**.

### 1️⃣ Data Ingestion (Web Scraping)

* **Sources:** Hatla2ee, ContactCars, YallaMotor
* **Tools:** Selenium, Undetected-Chromedriver, Pandas
* **Challenges Overcome:**
  - Bypassed dynamic website structures and infinite scrolling
  - Handled frequent HTML updates
  - Defeated stringent Cloudflare anti-bot mechanisms
  - Automated continuous data collection

### 2️⃣ The Medallion Architecture (Delta Lake)

| Layer | Purpose & Transformations |
| :--- | :--- |
| 🥉 **Bronze** | **Raw Data:** Immutable historical archive. Scraped CSV files ingested as-is without altering schemas to preserve original data state. |
| 🥈 **Silver** | **Cleansing & Validation:** String normalization (lower, initcap, regex text removal). Strict data type casting (bigint, double). Listing dates standardized to YYYY-MM-DD. Duplicates removed. Data quality checks enforced. |
| 🥇 **Gold** | **Business & AI Ready:** Statistical anomaly detection. PySpark Window functions remove extreme price outliers exceeding 3 standard deviations (Price ≤ Mean + 3×StdDev). Data aggregated by Brand/Model/Year. Optimized for analytics and ML pipelines. |

### 3️⃣ Data Flow Diagram

<img width="1024" height="582" alt="image_10c3562b-c685-493c-b9ef-380b113f970b" src="https://github.com/user-attachments/assets/4659ee06-6da7-403a-87dc-a4b26a3da30a" />


---

## ✨ Features

| Feature | Details |
| :--- | :--- |
| **Real-time Price Estimation** | Streamlit app queries Gold tables to provide accurate median prices for any selected Brand/Model/Year combination. |
| **Statistical Outlier Filtering** | The platform automatically ignores fake or unrealistic listings to ensure data reliability and accurate market averages. |
| **Market Dashboards** | Deep-dive Power BI reports tracking depreciation by year, mileage distributions, and geographic supply metrics (e.g., Toyota vs. Nissan). |
| **Interactive Filtering** | Users can seamlessly filter market data by Location, Fuel Type (Gasoline vs. Natural Gas), Transmission, and Year. |
| **Scalable Architecture** | Medallion Architecture enables easy scaling and maintenance of data pipelines. |
| **Historical Analytics** | Track market trends over time with immutable historical data. |

---

## 📁 Project Structure

```
NHA-4-084/
├── notebooks/              # Jupyter notebooks for ETL pipelines
│   ├── bronze_layer.ipynb
│   ├── silver_layer.ipynb
│   ├── gold_layer.ipynb
├── src/                    # Python modules
│   ├── scrapers/          # Web scraping
module
├── streamlit_app/         # Streamlit
├── power_bi/              # Power BI report definitions
├── data/                  # Sample datasets
├── requirements.txt       # Python dependencies
├── README.md             # This file
information
```

---

## 🚀 Getting Started

### Prerequisites

- **Python:** 3.8 or higher
- **Databricks:** Workspace access (if running on Databricks)
- **Git:** For cloning the repository
- **pip:** Python package manager

### Installation

1. **Clone the repository:**
```bash
git clone https://github.com/nhahub/NHA-4-084.git
cd NHA-4-084
```

2. **Create a virtual environment (recommended):**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Configure your environment:**
   - Set up Databricks credentials in your environment variables
   - Update `config/` files with your API keys and workspace settings

5. **Run the Streamlit app:**
```bash
streamlit run streamlit_app/app.py
```

---

## 💡 Usage

### Running the Streamlit Application

1. Launch the app:
```bash
streamlit run streamlit_app/app.py
```

2. **Using the Dashboard:**
   - Select vehicle specifications (Brand, Model, Year)
   - View real-time median prices and market insights
   - Filter by Location, Fuel Type, Transmission
   - Explore historical trends and depreciation patterns

### Running ETL Pipelines

1. **Bronze Layer (Data Ingestion):**
```python
# Run notebook: notebooks/bronze_ingestion.ipynb
# Scrapes data from all sources into raw Delta tables
```

2. **Silver Layer (Data Cleaning):**
```python
# Run notebook: notebooks/silver_cleaning.ipynb
# Validates, cleanses, and standardizes data
```

3. **Gold Layer (Aggregation):**
```python
# Run notebook: notebooks/gold_aggregation.ipynb
# Creates business-ready datasets with outlier filtering
```

## 🚀 Future Enhancements

- 🤖 **AI Price Prediction Models:** Implement regression and ensemble methods for price forecasting
- 📱 **Mobile Application:** iOS/Android app for on-the-go market insights
- 🔔 **Real-time Price Alerts:** Notify users when prices drop for specific vehicles
- 🌍 **Market Expansion:** Extend to other Middle Eastern and North African markets
- 📊 **Advanced Analytics:** Implement time-series forecasting and anomaly detection
- 🔗 **API Service:** RESTful API for third-party integrations
- 🎯 **Recommendation Engine:** ML-based vehicle recommendations based on user preferences

---

## 🤝 Contributing

We welcome contributions! Please follow these guidelines:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

For detailed guidelines, see [CONTRIBUTING.md](CONTRIBUTING.md) (if available).

---

## 👥 Team

| Name | Role |
| :--- | :--- |
| **Yusif Saeed** | Data Engineering & Architecture |
| **Mina Dawood** | Data Engineering & Architecture |
| **Abdalrahman Saleh** | Data Engineering & Architecture |
| **Mohamed Ateya Elhag** | Data Engineering & Architecture |
| **Khaled Abdelmageed** | Data Engineering & Architecture |
| **Karim Wessam** | Data Engineering & Architecture |

---

<div align="center">
<p><strong>Made with ❤️ by the NHA Team</strong></p>
<p><a href="https://car-decision-assistant-1.streamlit.app/"><strong>🔗 Live App</strong></a> | <a href="https://github.com/nhahub/NHA-4-084">GitHub</a></p>
</div>
