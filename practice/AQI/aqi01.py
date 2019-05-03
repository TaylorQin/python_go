import requests
from bs4 import BeautifulSoup

def main():
    cities = parseCities()
    for city in cities:
        print(city.text)
        print(city.attrs['href'])

def parseCities():
    responce = requests.get("http://pm25.in")
    soup = BeautifulSoup(responce.text,'lxml')
    cities = soup.select(".hot a")
    for city in cities:
        print(city.text)
        print(city.attrs['href'])

    cities = soup.select(".all a")
    return cities

if __name__ == "__main__":
    main()