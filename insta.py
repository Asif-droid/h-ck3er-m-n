import requests
from bs4 import BeautifulSoup as bs
import json
import random
import os.path
# print("ok")
insta_url='https://www.instagram.com'
inta_username= input('enter username of instagram : ')
 
response = requests.get(f"{insta_url}/{inta_username}/")
# response=requests.get(f'https://www.instagram.com/elonmusk/')
print(response.ok)
if response.ok:
    html=response.text
 
    bs_html=bs(html, features="lxml")
    bs_html=bs_html.text
    index=bs_html.find('profile_pic_url_hd')+21
    print(bs_html)

 
    # remaining_text=bs_html[index:]
    # remaining_text_index=remaining_text.find('requested_by_viewer')-3
    # string_url=remaining_text[:remaining_text_index].replace("\\u0026","&")
    # if string_url != "":
    #     print(string_url, " downloading..........")

