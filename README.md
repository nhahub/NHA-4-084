<div align="center">
<h1>🚗 Car Decision Assistant</h1>
*Choose the car that best fits your needs with data-driven insights.*
Live App
</div>
## 📊 Business Problem & Solution
**The Problem:** The used car market in Egypt suffers from fragmented information. Prices fluctuate frequently, and data is scattered across multiple platforms (Hatla2ee, ContactCars, YallaMotor). Buyers waste hours manually comparing listings, and purchasing decisions are often based on assumptions rather than real market data.
**The Solution:** An end-to-end Data Engineering pipeline that autonomously scrapes, cleans, and centralizes real-time automotive market data. The **Car Decision Assistant** utilizes AI-ready datasets to analyze market trends, detect pricing anomalies, and provide users with a unified, interactive platform for making optimal purchasing decisions.
## 🏗️ Pipeline Architecture & ETL Flow
We built a robust, scalable Data Warehouse leveraging **Databricks** and the **Medallion Architecture**.
### 1️⃣ Data Ingestion (Web Scraping)
 * **Sources:** Hatla2ee, ContactCars, YallaMotor.
 * **Tools:** selenium, undetected-chromedriver, pandas.
 * **Challenges Overcome:** Bypassed dynamic website structures, infinite scrolling, frequent HTML updates, and stringent Cloudflare anti-bot mechanisms.
### 2️⃣ The Medallion Architecture (Delta Lake)

| Layer | Purpose & Transformations |
| :--- | :--- |
| 🥉 **Bronze** | **Raw Data:** Immutable historical archive. Scraped CSV files are ingested as-is without altering schemas to preserve original data state. |
| 🥈 **Silver** | **Cleansing & Validation:** String normalization (lower, initcap, regex text removal). Strict data type casting (bigint, double). Listing dates standardized to YYYY-MM-DD. Duplicate and missing value handling. |
| 🥇 **Gold** | **Business & AI Ready:** Statistical anomaly detection. PySpark Window functions remove extreme price outliers exceeding 3 standard deviations (Price <= Mean + 3*StdDev). Data aggregated into optimized marts (e.g., Gold_price_by_model). | <br> ## 🌍 Platform Features & Outputs
| Feature | Details |
| :--- | :--- |
| **Real-time Price Estimation** | Streamlit app queries Gold tables to provide accurate median prices for any selected Brand/Model/Year combination. |
| **Statistical Outlier Filtering** | The platform automatically ignores fake or unrealistic listings to ensure data reliability and accurate market averages. |
| **Market Dashboards** | Deep-dive Power BI reports tracking depreciation by year, mileage distributions, and geographic supply metrics (e.g., Toyota vs. Nissan). |
| **Interactive Filtering** | Users can seamlessly filter market data by Location, Fuel Type (Gasoline vs. Natural Gas), Transmission, and Year. | <br> ## 🚀 Future Enhancements <br> * 🤖 **AI Price Prediction:** Implementing machine learning models to forecast future car values. <br> * 🎙️ **Arabic Voice Assistant:** NLP-powered voice searches for accessibility. <br> * 🔔 **Automatic Price Alerts:** Real-time notifications for market drops. <br> * 📱 **Mobile Application:** Expanding the Streamlit experience into a native mobile app. <br> ## 👥 The Team (DEPI - Microsoft Data Engineering Track)
| Name | Role |
| :--- | :--- |
| **Yusif Saeed** | Data Engineering & Architecture |
| **Mina Dawood** | Data Engineering & Architecture |
| **Abdalrahman Saleh** | Data Engineering & Architecture |
| **Mohamed Ateya Elhag** | Data Engineering & Architecture |
| **Khaled Abdelmageed** | Data Engineering & Architecture |
| **Karim Wessam** | Data Engineering & Architecture |

<div align="center">
Live App
</div>
