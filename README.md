# Real-time-Cryptocurrency-Analysis
This project demonstrates an end-to-end real-time streaming analytics solution for cryptocurrency market data. It is designed to simulate a production-grade pipeline:

Data is fetched in real-time from CoinGecko API.

Azure Event Hub acts as a high-throughput broker to ingest and buffer the incoming events.

Azure Databricks (or alternatively a Python-based batch process) consumes the stream, performs transformations such as calculating daily percentage changes and moving averages, and writes the processed data into Delta Lake.

Power BI Desktop connects to the Delta Lake (or to the transformed CSV file) for interactive real-time visualization and analysis.

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

## Power BI Analysis
<img width="800" alt="image" src="https://github.com/user-attachments/assets/5e0c6677-d847-4882-8bcc-e7e2f09a2866" />




