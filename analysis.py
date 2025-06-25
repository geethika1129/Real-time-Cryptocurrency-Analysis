import os
import json
import time
import pandas as pd
import requests
from dotenv import load_dotenv
from azure.eventhub import EventHubProducerClient, EventData

# Load environment variables
load_dotenv()
EVENT_HUB_CONN_STR = os.getenv("EVENT_HUB_CONN_STR")
EVENT_HUB_NAME = os.getenv("EVENT_HUB_NAME")

# Initialize Event Hub producer
producer = EventHubProducerClient.from_connection_string(
    conn_str=EVENT_HUB_CONN_STR, eventhub_name=EVENT_HUB_NAME
)

def fetch_crypto_data():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": "bitcoin,ethereum,solana",
        "vs_currencies": "usd",
        "include_market_cap": "true",
        "include_24hr_vol": "true",
        "include_24hr_change": "true"
    }
    response = requests.get(url, params=params)
    return response.json()

def send_data_to_eventhub(data_dict):
    event_data_batch = producer.create_batch()
    
    for coin, values in data_dict.items():
        payload = {
            "coin": coin,
            "usd": values.get("usd"),
            "market_cap": values.get("usd_market_cap"),
            "volume_24h": values.get("usd_24h_vol"),
            "change_24h": values.get("usd_24h_change"),
            "timestamp": pd.Timestamp.utcnow().isoformat()
        }
        event_data_batch.add(EventData(json.dumps(payload)))
    
    producer.send_batch(event_data_batch)
    print("✅ Sent data to Event Hub")

if __name__ == "__main__":
    while True:
        data = fetch_crypto_data()
        send_data_to_eventhub(data)
        time.sleep(10)  # send every 10 seconds
