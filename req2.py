import urllib.request
import requests
from clint.textui import progress

with open('./links_list.txt') as file:
    for url in file:

        r = requests.get(url.replace('\n', ''), stream=True)

        # urllib.request.urlretrieve(url, './course2/{}'.format(url.split('/')[4].replace('\n', '')))
        # print('complete {}'.format(url))

        path = './{}'.format(url.split('/')[4].replace('\n', ''))

        print(path)

        with open(path, 'wb') as f:
            total_length = int(r.headers.get('content-length'))
            for chunk in progress.bar(r.iter_content(chunk_size=1024), expected_size=(total_length / 1024) + 1):
                if chunk:
                    f.write(chunk)
                    f.flush()

