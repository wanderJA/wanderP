# -*- coding:UTF-8 -*-
import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    server = 'http://www.biqukan.com/'
    target = 'http://www.biqukan.com/1_1094'
    requests_target = requests.get(url=target)
    text = requests_target.text
    beautiful = BeautifulSoup(text).find_all('div', class_='listmain')
    a_bf = BeautifulSoup(str(beautiful[0]))
    a = a_bf.find_all('a')
    for each in a:
        print(each.string, server + each.get('href'))
    # print(beautiful[0].text.replace('\xa0' * 8, '\n\n'))
