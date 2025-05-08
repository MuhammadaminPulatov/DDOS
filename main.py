import requests
from concurrent.futures import ThreadPoolExecutor
import time

urls = [
    'https://www.../'
]

def send_request(url):
    try:
        r = requests.get(url, timeout=1)
        print(f"{url} -> {r.status_code}")
    except Exception as e:
        print(f"{url} -> Error: {e}")

start = time.time()

with ThreadPoolExecutor(max_workers=100000000) as executor:
    for _ in range(10000000):
        for url in urls:
            executor.submit(send_request, url)

print("Tugadi. Time:", time.time() - start)
