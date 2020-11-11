import requests
import time
from bs4 import BeautifulSoup
from datetime import datetime

def link_generate(arg, amazon_link, last_part, page_num, f_header):
    replaced_arg = arg.replace(" ", "+")
    final_link = amazon_link+replaced_arg+last_part+str(page_num)
    print('\033[32m' + '[@] link Generated Successfuly: ' + '\033[39m' + final_link)
    request(final_link, f_header)

def request(link_to, header_to):
    response = requests.get(link_to, headers=header_to)
    soup = BeautifulSoup(response.content, 'html5lib')
    price = soup.findAll('span', {'class':'a-price-whole'})
    fraction = soup.findAll('span', {'class':'a-price-fraction'})
    product_link = soup.findAll('a', {'class':'a-link-normal a-text-normal'})
    filter(price, fraction, product_link)

def filter(price_ar, fraction_ar, product_ar):
    p_n = len(price_ar)
    f_n = len(fraction_ar)
    pr_n = len(product_ar)
    filterd_price = []
    filterd_fraciton = []
    filterd_product = []
    i = 0
    f_i = 0
    pr_i = 0
    while i < p_n:
        tmp = price_ar[i]
        filterd_price.append(tmp.text)
        i += 1
    while f_i < f_n:
        f_tmp = fraction_ar[f_i]
        filterd_fraciton.append(f_tmp.text)
        f_i += 1
    while pr_i < pr_n:
        n_tmp = product_ar[pr_i]
        filterd_product.append(n_tmp.get('href'))
        pr_i += 1
    printing(filterd_price, filterd_fraciton, filterd_product)

def printing(f_price, f_fraction, f_product):
    leng = len(f_price)
    i = 0
    while i < leng:
        print('$' + str(f_price[i]) + str(f_fraction[i]) + "      " + "\033[32m" + "https://www.amazon.com" + str(f_product[i]) + "\033[39m")
        i += 1

arg1 = input('the name of the product: ')
arg2 = input('how many pages you want to scrape: ')
link = 'https://www.amazon.com/s?k='
part_link = '&page='
fake_header = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0',
            'Accept-Language': 'en-US, en;q=0.5'})
num = 1
while num <= int(arg2):
    link_generate(arg1, link, part_link, num, fake_header)
    num += 1
