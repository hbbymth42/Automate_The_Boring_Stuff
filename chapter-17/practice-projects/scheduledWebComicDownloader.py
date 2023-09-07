#! python3 
# scheduledWebComicDownloader.py - Downloads every new XKCD comic

import requests, os, bs4, re

url = 'https://xkcd.com'            # starting url
os.makedirs('xkcd', exist_ok=True)  # store comics in ./xkcd
# Download the page.
print('Getting page %s...' % url)
res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')

# Find the URL of the comic image.
comicElem = soup.select('#comic img')
if comicElem == []:
    print('Could not find comic image.')
else:
    comicUrl = 'https:' + comicElem[0].get('src')
    comicFileName = re.findall("[\w\d]+\.png", comicUrl)[0]
    if comicFileName in os.listdir('./xkcd'):
        print('Image already downloaded')
    else:
        # Download the image.
        print('Downloading image %s...' % (comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()
        # Save the image to .xkcd/.
        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
        print('Done.')