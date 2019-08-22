import requests, urllib.request
from bs4 import BeautifulSoup
from lxml import html


url = 'https://coursehunter.net/course/itvdn-python-essential'
headers = {
        'Host': 'coursehunter.net',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://coursehunter.net/sign-in',
        'Connection': 'keep-alive',
        'Cookie': 'locale=en; _ga=GA1.2.8342895.1564666488; CHUNTERS=a63a2524117cd4608dce03f368aafd39; locale=en; redirect_after_login=https://coursehunter.net/course/itvdn-python-essential; user_ident=2ef1e3b3-7991-4b3c-941c-1fce991b4f07; accessToken=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsImp0aSI6IjRmMWcyM2ExMmFhIn0.eyJpc3MiOiJodHRwczpcL1wvY291cnNlaHVudGVyLm5ldCIsImF1ZCI6Imh0dHBzOlwvXC9jb3Vyc2VodW50ZXIubmV0IiwianRpIjoiNGYxZzIzYTEyYWEiLCJpYXQiOjE1NjY0ODE2MDUsIm5iZiI6MTU2NjQ4MTY2NSwiZXhwIjoxNTY3MDg2NDA1LCJ1c2VyX2lkIjoiMzA4MDQiLCJlX21haWwiOiJ1Z3Rlcm5AZ21haWwuY29tIn0.HQuRn3sgycDZDuw-r930tXqm5wVtJ_Z3utWD2O6qhpg; _gid=GA1.2.1659369943.1566370458; ch_quiz=9ba4d680ce4485fbad89c4f30c31acc1; _gat=1',
        'Upgrade-Insecure-Requests': '1',
        'Cache-Control': 'max-age=0',
    }

finding = 'https://vs1.coursehunter.net/itvdn-python-essential/lesson1.mp4'

r = requests.get(url, headers=headers)
with open('test.html', 'w') as file:
    file.write(r.content.decode())

# r_content = r.content.decode().find(finding)
# print(r_content)
# print(r.content.decode()[r_content: (r_content+len(finding))])