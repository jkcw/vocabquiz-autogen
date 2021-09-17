import requests
import json

import secretKey

secret_key = secretKey.secret_key

#vocab = "get"
#api_request = requests.get('https://www.dictionaryapi.com/api/v3/references/collegiate/json/' + vocab + '?key=' + secret_key)
#js = api_request.json()

file = open('vocab-cache.txt', "r")
js = json.load(file)
file.close()
#print(js[0]['def'][0]['sseq'])
#for i in js[0]['def'][0]['sseq']:
#    print(i)

for i in js[0]['def'][0]['sseq'][0]:
    definition = i[1]['dt'][0][1]
    # TODO: There might be more than one example
    example = i[1]['dt'][1][1][0]['t']
    print(definition)
    print(example)

class RequestVocabData:
    def __init__(self, vocab):
        self.vocab = vocab.lower()
        self.js_dict = []
        self.part_of_speech = []

    def http_api_request(self):
        api_request = requests.get('https://api.dictionaryapi.dev/api/v2/entries/en/' + self.vocab)
        js = api_request.json()
        try:
            self.js_dict = js[0]
            return True
        except:
            return False

    def get_all_part_of_speech(self):
        self.part_of_speech = self.js_dict["meanings"]