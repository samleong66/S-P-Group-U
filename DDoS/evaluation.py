import requests
import time

IP = '10.211.55.5'
PORT = 8000

def calculate_response_time(ip_address, port):
    try:
        start_time = time.time()
        url = f"http://{ip_address}:{port}"
        response = requests.get(url)
        end_time = time.time()
        if response.status_code == 200:
            return end_time - start_time
        else:
            return None
    except requests.exceptions.RequestException:
        return None

def main():
    ip_address = IP
    port = PORT
    response_time = calculate_response_time(ip_address, port)
    if response_time is not None:
        print("Response time:", response_time, "seconds")
    else:
        print("Unable to get response time for", ip_address)

if __name__ == "__main__":
    while True:
        try:
            main()
        except KeyboardInterrupt:
            print('Stop')
        time.sleep(1)

