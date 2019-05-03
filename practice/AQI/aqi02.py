import requests
from bs4 import BeautifulSoup

def main():
    print(parseTh("shanghai"))

    cities = parseCities()
    for city in cities:
        print(city.text)
        print(city.attrs['href'])
        trs = parseTr(city.attrs['href'])
        for tr in trs:
            print(tr)


def parseCities():
    responce = requests.get("http://pm25.in")
    soup = BeautifulSoup(responce.text,'lxml')
    cities = soup.select(".hot a")
    for city in cities:
        print(city.text)
        print(city.attrs['href'])

    cities = soup.select(".all a")
    return cities

def parseTh(citypath):
    responce = requests.get("http://pm25.in/"+citypath)
    soup = BeautifulSoup(responce.text,'lxml')

    keys = soup.select("#detail-data thead th")
    headtexts = []
    for key in keys:        
        headtexts.append(key.text)

    head = str.join(",", headtexts)
    return head

def parseTr(citypath):
    trs = []
    responce = requests.get("http://pm25.in/"+citypath)
    soup = BeautifulSoup(responce.text,'lxml')

    values = soup.select("#detail-data tbody tr")

    for value in values:        
        tds = value.findAll("td", {})
        columntexts = []
        for td in tds:
            columntexts.append(td.text)
        trs.append(str.join(",", columntexts))

    return trs
  
if __name__ == "__main__":
    main()