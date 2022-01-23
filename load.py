import time
import requests
def automate_update(url):
    respons = requests.get(url)
    half_link = respons.request.url.rpartition('_')[0]
    half_link += "_blue_Mobole"
    from bs4 import BeautifulSoup
    # with open('feed.xml', 'r' , encoding='utf-8', errors='ignore') as f:
    #     data = f.read()
    Bs_data = BeautifulSoup(respons.content, "xml")
    for postcode_tag in Bs_data.find_all("BaseURL"):
        postcode_tag.string = half_link
    with open("usman.mpd", "w") as outfile:
        outfile.write(Bs_data.prettify())

        