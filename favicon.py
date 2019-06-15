import requests
from bs4 import BeautifulSoup

urls = ["http://babymanisha.com/", "https://www.google.com/", "https://www.linkedin.com", 
        "https://in.yahoo.com", "https://4iq.com/", "https://www.aviso.com/", "https://v1.vuejs.org",
        "https://www.facebook.com/", "https://twitter.com", "https://instagram.com"]

faviconLinks = []

for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    faviconTag = soup.find("link", rel="icon")
    faviconLinks.append({
        'URL' : url,
        'Favicon-Link' : None
    })
    # print(faviconTag)
    faviconTagString = str(faviconTag)
    for el in faviconTagString.split("\""):
        if "https://" in el:
            faviconLinks[len(faviconLinks)-1]['Favicon-Link'] = el
            break
        elif ".png" in el or ".ico" in el or ".jpg" in el:
            faviconLinks[len(faviconLinks)-1]['Favicon-Link'] = url + el
            break
print(faviconLinks)


# Output will be like below
# [{'URL': 'http://babymanisha.com/', 'Favicon-Link': 'http://babymanisha.com/images/star.png'}, {'URL': 'https://www.google.com/', 'Favicon-Link': None}, {'URL': 'https://www.linkedin.com', 'Favicon-Link': 'https://static.licdn.com/scds/common/u/images/logos/favicons/v1/favicon.ico'}, {'URL': 'https://in.yahoo.com', 'Favicon-Link': 'https://s.yimg.com/os/mit/media/p/common/images/favicon_new-7483e38.svg'}, {'URL': 'https://4iq.com/', 'Favicon-Link': 'https://4iqstaging.com/wp-content/uploads/2017/08/Header-4iQ-Logo-q.png'}, {'URL': 'https://www.aviso.com/', 'Favicon-Link': None}, {'URL': 'https://v1.vuejs.org', 'Favicon-Link': 'https://v1.vuejs.org/images/logo.png'}, {'URL': 'https://www.facebook.com/', 'Favicon-Link': 'https://static.xx.fbcdn.net/rsrc.php/yz/r/KFyVIAWzntM.ico'}, {'URL': 'https://twitter.com', 'Favicon-Link': 'https://twitter.com//abs.twimg.com/favicons/favicon.ico'}, {'URL': 'https://instagram.com', 'Favicon-Link': 'https://instagram.com/static/images/ico/favicon-192.png/68d99ba29cc8.png'}]
