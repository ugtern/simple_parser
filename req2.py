import urllib.request
with open('./links_list.txt') as file:
    for url in file:
        urllib.request.urlretrieve(url, './course/{}'.format(url.split('/')[4].replace('\n', '')))
