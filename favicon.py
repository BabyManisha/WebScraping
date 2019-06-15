import requests
from bs4 import BeautifulSoup

urls = ["http://babymanisha.com/", "https://www.google.com/", "https://www.linkedin.com", 
        "https://in.yahoo.com", "https://4iq.com/", "https://www.aviso.com/", "https://v1.vuejs.org",
        "https://www.facebook.com/", "https://twitter.com", "https://instagram.com"]

# url = "http://babymanisha.com/"
# url = "https://www.google.com/"
# url = "https://www.linkedin.com"
# url = "https://in.yahoo.com"
# url = "https://4iq.com/"
# url = "https://www.aviso.com/"
# url = "https://v1.vuejs.org"
# url = "https://www.facebook.com/"
# url = "https://twitter.com"
# url = "https://instagram.com"

faviconLink = []
for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    faviconTag = soup.find("link", rel="icon")
    # print(faviconTag)
    faviconTagString = str(faviconTag)
    for el in faviconTagString.split("\""):
        if "https://" in el:
            faviconLink.append(el)
            break
        elif ".png" in el or ".ico" in el or ".jpg" in el:
            faviconLink.append(url + el)
            break
print("Working - " + str(len(faviconLink)) + "/" + str(len(urls)))
print(faviconLink)
# faviconResponse = requests.get(faviconLink)
# print(faviconResponse.text)
