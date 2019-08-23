import requests


url = 'https://coursehunter.net/course/asinhronnye-metody-i-primery-v-python'
headers = {
        'Host': 'coursehunter.net',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://coursehunter.net/sign-in',
        'Connection': 'keep-alive',
        'Cookie': 'locale=en; _ga=GA1.2.8342895.1564666488; CHUNTERS=a63a2524117cd4608dce03f368aafd39; locale=en; redirect_after_login=https://coursehunter.net/course/asinhronnye-metody-i-primery-v-python; user_ident=e307d0bf-118d-4283-a5c0-c2fa3a222557; accessToken=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsImp0aSI6IjRmMWcyM2ExMmFhIn0.eyJpc3MiOiJodHRwczpcL1wvY291cnNlaHVudGVyLm5ldCIsImF1ZCI6Imh0dHBzOlwvXC9jb3Vyc2VodW50ZXIubmV0IiwianRpIjoiNGYxZzIzYTEyYWEiLCJpYXQiOjE1NjY1NDUwNzcsIm5iZiI6MTU2NjU0NTEzNywiZXhwIjoxNTY3MTQ5ODc3LCJ1c2VyX2lkIjoiMzA4MDQiLCJlX21haWwiOiJ1Z3Rlcm5AZ21haWwuY29tIn0.NNNev1sJ9-8EaxdA69aXAOJxtm59GfefjMQqWgxF38Y; _gid=GA1.2.1659369943.1566370458; ch_quiz=0623c1b59a6fd0d431bb09a0a363bca3; _gat=1',
        'Upgrade-Insecure-Requests': '1',
        'Cache-Control': 'max-age=0',
    }

r = requests.get(url, headers=headers)
with open('test.html', 'w') as file:
    file.write(r.content.decode())
