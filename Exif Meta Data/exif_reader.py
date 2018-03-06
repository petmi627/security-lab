import requests
import urllib
import exifread
import sys, os

from bs4 import BeautifulSoup

def get_pic_urls(url):
    response = requests.get(url)
    if response.status_code == 200:

        doc = BeautifulSoup(response.text, "html.parser")

        images = doc.find_all('img')

        images_found = []

        for img in images:
            try:
                img_url = urllib.parse.urljoin(url, img.attrs["src"])
                images_found.append(img_url)
            except BaseException:
                print("Cannot extract src attribute from image tag")
                print(img.attrs)
                sys.exit(1)

        return images_found

    else:
        print("Error contacting server: Code " + str(response.status_code))
        sys.exit(1)

def download_images(images):
    path = os.path.realpath("./images")
    path_list = []
    if not os.path.exists(path):
        os.mkdir(path)


    for image in images:
        filename = image.split('/')[-1]
        response = requests.get(image)
        if response.status_code == 200:
            try:
                save_path = os.path.join(path, filename)
                with open(save_path, "wb") as file:
                    file.write(response.content)
                    path_list.append(save_path)
                print("Image Saved in {}".format(save_path))
            except BaseException:
                print("Cannot save image {}".format(filename))

        else:
            print("Cannot download image {} Status Code {}".format(filename, response.status_code))

    return path_list

def show_exif_meta_tags(paths):
    for path in paths:
        with open(path, "rb") as file:
            tags = exifread.process_file(file)
            for key, value in tags.items():
                print(path + " >> " + str(key) + ": " + str(value))



def main():
    url = "http://localhost/Test/Anistrike/image_blur.html"
    images = get_pic_urls(url)
    paths = download_images(images)
    show_exif_meta_tags(paths)

if __name__ == '__main__':
    main()

