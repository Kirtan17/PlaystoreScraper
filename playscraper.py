import requests
from bs4 import BeautifulSoup

def appname (results):
    name = "NULL"
    try:
        src = results.content
        soup = BeautifulSoup(src, 'lxml')
        h1_tag = soup.find_all('h1', {'class': 'AHFaub'})
            #print(h1_tag)
        name = h1_tag[0].text
    except:
        name = "Couldn't fetch name"
    return name

def devsite (results):
    site = "NULL"
    try:
        src = results.content
        soup = BeautifulSoup(src, 'lxml')
        links = soup.find_all("a")
        for link in links:
            if "Visit website" in link.text:
                site = link.attrs['href']
    except:
        site = "Couldn't fetch dev site"
    return site

def appcat (results):
    category = "NULL"
    try:
        src = results.content
        soup = BeautifulSoup(src, 'lxml')
        span_tag = soup.find_all('span', {'class' : 'T32cc UAO9ie'})
        category = span_tag[1].text
    except:
        category = "Couldn't fetch dev category"
    return category

def appstars (results):
    stars = "NULL"
    try:
        src = results.content
        soup = BeautifulSoup(src, 'lxml')
        div_tag = soup.find_all('div', {'class' : 'BHMmbe'})
        stars = div_tag[0].text
    except:
        stars = "Couldn't fetch ratings"
    return stars

def display (name,site,category,stars):
    print(f"Name: {name}\tDeveloper website: {site}\tCategory: {category}\t Rating: {stars} \n")

def main (idslist):
    for id in idslist:
        concat = "https://play.google.com/store/apps/details?id=" + id
        results = requests.get(concat)
        name = appname(results)
        site = devsite(results)
        cat = appcat(results)
        rating = appstars(results)
        display(name,site,cat,rating)

if __name__ == '__main__':
    #ids = ['com.adobe.reader','com.linkedin.android','com.google.android.apps.meetings','com.facebook.mlite']
    ids = list(input("Please enter comma separated appids: ").split(","))
    main(ids)