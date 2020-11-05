import os
import requests
import bs4
import shutil

SAVE_FOLDER = 'amirkhan_imgs'

def main():
    if not os.path.exists(SAVE_FOLDER):
        os.mkdir(SAVE_FOLDER)
    download_images()

def download_images():
    url = input("enter the url: ")
    response = requests.get(url)
    filename = "temp.html"
    bs = bs4.BeautifulSoup(response.text, "html.parser")
    formatted_text = bs.prettify()

    try:
        with open(filename, "w+") as f:
            f.write(formatted_text)
    except Exception as e:
        print(e)

    list_imgs = bs.find_all('img', {'alt':'Aamir Khan'})
    no_of_imgs = len(list_imgs)

    print("Number of images: ", no_of_imgs)

    j = 1
    for imgTag in list_imgs:
        try:
            imgLink = imgTag.get('src')
            ext = imgLink[imgLink.rindex('.'):]
        
            if ext.startswith(".png"):
                ext = ".png"
            elif ext.startswith(".jpeg"):
                ext = ".jpeg"
            elif ext.startswith(".jpg"):
                ext = ".jpg"
            elif ext.startswith(".svg"):
                ext = ".svg"
            

            filen = SAVE_FOLDER + '/' +str(j)+ext
            res = requests.get(imgLink,stream=True)

            with open(filen,"wb") as file:
                shutil.copyfileobj(res.raw,file)
        except Exception as e:
            print(e)

        j = j+1    
    print("Done")
main()