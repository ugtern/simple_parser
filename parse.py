from bs4 import BeautifulSoup

items = []

with open('./test.html') as file:
    soup = BeautifulSoup(file)
    our_list = soup.findAll('li', {'class': 'lessons-item'})
    for item in our_list:
        items.append(item.findAll('link')[3].get('href'))
    # film_list = soup.find('li', {'class': 'lessons-item'}).findAll('link')[3].get('href')
with open('links_list.txt', 'w') as file:
    for item in items:
        file.write(item+'\n')