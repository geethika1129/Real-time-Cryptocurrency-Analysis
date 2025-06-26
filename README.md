# 💸 Real-time Cryptocurrency Market Analysis Pipeline
## 📌 Project Description
This project demonstrates a real-time data pipeline for cryptocurrency price analysis, using live data from the CoinGecko API. The architecture is designed with Azure Event Hub, Azure Databricks, and Power BI to simulate an event-driven analytics platform.

✅ Data Ingestion:
Live or periodic cryptocurrency prices (e.g., Bitcoin, Ethereum) are fetched from the CoinGecko API and ingested into Azure Event Hub, simulating real-time data streams.

✅ Real-time Processing in Azure Databricks:
Using Structured Streaming in Databricks, the price data is read from Event Hub, processed in near-real-time, and cleaned/aggregated as necessary.

✅ Delta Lake Storage (Bronze → Silver → Gold):

Bronze: Raw JSON streamed from CoinGecko via Event Hub

Silver: Cleaned price + timestamp

Gold: Aggregated insights (e.g., % change, moving average)

## ✅ Power BI Visualization:
The Gold Delta table is used as a source for Power BI dashboards, visualizing price trends, comparisons, and volatility over time.

<img width="800" alt="image" src="https://github.com/user-attachments/assets/5e0c6677-d847-4882-8bcc-e7e2f09a2866" />

## 🔄 Extendability
This architecture can easily be extended to:

Multiple coins

Live alerting (e.g., threshold breaches)

Prediction models (e.g., future price forecasting)

Auto-refreshing Power BI dashboards

## Architecture
       +----------------------+
       |  CoinGecko API       |
       |  (Crypto Data)       |
       +----------+-----------+
                  |
                  v
       +----------------------+
       | Python Script        |
       | (Data Fetch & Push)  |
       |   .env for Secrets   |
       +----------+-----------+
                  |
                  v
       +----------------------+
       | Azure Event Hub      |
       |   (Ingestion Layer)  |
       +----------+-----------+
                  |
                  v
       +----------------------+
       | Databricks           | 
       | Structured Streaming |
       |   & Delta Lake       |
       +----------+-----------+
                  |
                  v
       +----------------------+
       | Power BI             |
       | (Visualization)      |
       +----------------------+






