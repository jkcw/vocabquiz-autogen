import requests
import json

# Load vocabulary list
text_file = open("ietls-vocab-list.txt", "r")
vocab_list = json.load(text_file)

last_vocab = "coffer"
last_vocab_index = vocab_list.index(last_vocab)

# Load tenses list
tenses_file = open('tenses-list.json', "rw")
tenses_list = json.load(tenses_file)
print(tenses_list)

d = dict()
for word in tenses_list:
    d[word[0]] = word
tenses_file.write(json.dumps(d))

class RequestVocabData:
    def __init__(self, vocab):
        self.vocab = vocab
        self.js_dict = []
        self.part_of_speech = []

    def api_request(self):
        api_request = requests.get('https://api.dictionaryapi.dev/api/v2/entries/en/' + self.vocab)
        js = api_request.json()
        self.js_dict = js[0]

    def get_all_part_of_speech(self):
        self.part_of_speech = self.js_dict["meanings"]


class RequestDefTest(RequestVocabData):
    def __init__(self, vocab):
        super().__init__(vocab)
        self.question = ""
        self.answer = ""
        self.blank = "__________________"

    def rm_answer_to_blank(self, sentence):
        sentence.replace(self.vocab, self.blank)

    def get_def_test(self):
        for pos in self.part_of_speech:
            definition = pos['definitions']['definitions']
            partOfSpeech = pos['partOfSpeech']


class RequestSynonymsTest(RequestVocabData):
    def __init__(self, vocab):
        super().__init__(vocab)


class RequestFillInTheBlanksTest(RequestVocabData):
    def __init__(self, vocab):
        super().__init__(vocab)
        self.question = ""
        self.answer = ""
        self.blank = "__________________"

    def rm_answer_to_blank(self, sentence):
        sentence.replace(self.vocab, self.blank)

    def get_def_test(self):
        for pos in self.part_of_speech:
            partOfSpeech = pos['partOfSpeech']

            # Since there are so many definitions of a part of speech,
            # we need to get all definitions using iteration
            for definition in pos['definitions']:
                temp_answer = definition['definition']
                question = definition['example']



# Get 10 words for definition test

# Get 5 words for synonyms test

# Get 25 words for fill-in-the-blanks test


text_file.close()
tenses_file.close()
