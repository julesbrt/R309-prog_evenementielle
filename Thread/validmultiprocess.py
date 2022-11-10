import time
import multiprocessing
import requests

img_urls = ['https://cdn.pixabay.com/photo/2020/04/15/04/11/lake-5045059_960_720.jpg',
            'https://cdn.pixabay.com/photo/2020/02/08/19/15/snow-4831013_960_720.jpg']


def download_image(img_url):
    img_bytes = requests.get(img_url).content
    # -1 pour prendre le dernier élément de la liste
    img_name = img_url.split('/')[-1]
    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        print(f"{img_name} was downloaded")


def main():
    p1 = multiprocessing.Process(target=download_image, args=[img_urls[0]])
    p2 = multiprocessing.Process(target=download_image, args=[img_urls[1]])
    p1.start()
    p2.start()
    p1.join()
    p2.join()


if __name__ == '__main__':
    start = time.perf_counter()
    main()
    end = time.perf_counter()
    print(f"Tasks ended in {round(end - start, 2)} second(s)")
