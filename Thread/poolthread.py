import time
import concurrent.futures
import requests

img_urls = ['https://cdn.pixabay.com/photo/2020/04/15/04/11/lake-5045059_960_720.jpg', 'https://cdn.pixabay.com/photo/2020/02/08/19/15/snow-4831013_960_720.jpg']

#Pool de threads
def download_image(img_url):
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[-1] #-1 pour prendre le dernier élément de la liste
    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        print(f"{img_name} was downloaded")

start = time.perf_counter()

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(download_image, img_urls)

end = time.perf_counter()
print(f"Tasks ended in {round(end - start, 2)} second(s)")
