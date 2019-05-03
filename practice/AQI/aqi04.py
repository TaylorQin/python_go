import requests
from bs4 import BeautifulSoup
import csv

def main():

    city_list = parseCities()

    header = ['City','AQI','PM2.5/1h','PM10/1h','CO/1h','NO2/1h','O3/1h','O3/8h','SO2/1h']

    with open('china_city_aqi.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for i, city in enumerate(city_list):
            if (i+1) % 10 == 0:
                print('已处理{}条记录。（共{}条记录）'.format(i+1, len(city_list)))
            city_name = city[0]
            city_href = city[1]
            city_aqi = parseAqi(city_href)
            row = [city_name] + city_aqi
            writer.writerow(row)



def parseCities():
    responce = requests.get("http://pm25.in")
    soup = BeautifulSoup(responce.text,'lxml')
    city_list = []
    cities = soup.select(".all a")
    for city in cities:
        city_list.append((city.text, city.attrs['href']))
    return city_list      

def parseAqi(citypath):
    responce = requests.get("http://pm25.in/"+citypath)
    soup = BeautifulSoup(responce.text,'lxml')

    div_list = soup.select(".span1")
    aqi = []
    for i in range(8):
        div = div_list[i]       
        caption = div.find('div',{'class':'caption'}).text.strip()
        value = div.find('div',{'class':'value'}).text.strip()
        aqi.append(value)

    return aqi
  
if __name__ == "__main__":
    main()