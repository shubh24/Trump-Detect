import urllib2
from bs4 import BeautifulSoup

def download_page(url):
    try:
        headers = {}
        headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
        req = urllib2.Request(url, headers = headers)
        response = urllib2.urlopen(req)
        page = response.read()
        return page
    except:
        return"Page Not found"

search = "donald trump"
url = 'https://www.google.com/search?q=donald%20trump&espv=2&biw=1366&bih=667&site=webhp&source=lnms&tbm=isch&sa=X&ei=XosDVaCXD8TasATItgE&ved=0CAcQ_AUoAg'
url.replace(" ","%20")

raw_html =  (download_page(url))
soup = BeautifulSoup(raw_html)
links = []

imgs = soup.findAll("img")
for img in imgs:
    links.append(img.get("data-src",""))
k = 0
for l in links:
    if l:
        req = urllib2.Request(l, headers={"User-Agent": "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"})
        response = urllib2.urlopen(req)
        output_file = open("./Script-Positive/" + str(k+1)+".jpg",'wb')

        data = response.read()

        output_file.write(data)
        response.close();

        print("completed ====> "+str(k+1))
        k += 1

