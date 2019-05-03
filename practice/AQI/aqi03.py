import requests
from bs4 import BeautifulSoup

def main():
    city= input("请输入城市拼音：")
    print(parseAqi(city))

def parseAqi(citypath):
    responce = requests.get("http://pm25.in/"+citypath)
    soup = BeautifulSoup(responce.text,'lxml')

    div_list = soup.select(".span1")
    aqi = []
    for i in range(8):
        div = div_list[i]       
        caption = div.find('div',{'class':'caption'}).text.strip()
        value = div.find('div',{'class':'value'}).text.strip()
        aqi.append((caption,value))

    return aqi
  
if __name__ == "__main__":
    main()