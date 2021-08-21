import requests

word = 'hello'
test = requests.get('https://api.dictionaryapi.dev/api/v2/entries/en/' + word)
js = test.json()
js_dict = js[0]
print(js_dict["meanings"][2]["definitions"])
