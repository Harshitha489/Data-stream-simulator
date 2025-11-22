import time
import random

def generate_data():
    """Simulate a single data packet."""
    data = {
        "temperature": round(random.uniform(20.0, 35.0), 2),
        "humidity": round(random.uniform(40.0, 90.0), 2),
        "pressure": round(random.uniform(900.0, 1100.0), 2),
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }
    return data

def start_stream():
    print("Starting Data Stream...\n")
    
    while True:
        data_packet = generate_data()
        print(data_packet)
        time.sleep(1)  # 1 second delay between packets

if __name__ == "__main__":
    start_stream()