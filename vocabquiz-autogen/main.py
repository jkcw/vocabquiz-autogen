import requests
import json

# Load vocabulary list
text_file = open("ietls-vocab-list.txt", "r")
vocab_list = json.load(text_file)

last_vocab = "coffer"
last_vocab_index = vocab_list.index(last_vocab)

# Load tenses list
tenses_file = open('tenses-list.json', "r")
tenses_dict = json.load(tenses_file)


class RequestVocabData:
    def __init__(self, vocab):
        self.vocab = vocab.lower()
        self.js_dict = []
        self.part_of_speech = []

    def http_api_request(self):
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
        # Check if the vocabulary is a verb
        try:
            tenses = tenses_dict[self.vocab]
            for tense in tenses:
                if tense in sentence:
                    sentence = sentence.replace(tense, self.blank)
                    return {"tense": tense, "question": sentence}
            return {"tense": "error:rm_answer_to_blank", "question": "error:rm_answer_to_blank"}

        except:
            sentence = sentence.replace(self.vocab, self.blank)
            return {"tense": self.vocab, "question": sentence}

    def json_to_readable_text(self):
        # Since there are so much part of speech,
        # we need to get all part of speech using iteration
        for pos in self.part_of_speech:
            partOfSpeech = pos['partOfSpeech']

            # Since there are so many definitions of a part of speech,
            # we need to get all definitions using iteration
            for definition in pos['definitions']:
                try:
                    question = definition['example']
                except:
                    continue

                # Remove the answer to blanks
                removed_ans_dict = self.rm_answer_to_blank(question)

                question = removed_ans_dict['question'] + "\n"
                temp_answer = removed_ans_dict['tense'] + "/" + partOfSpeech + "/" + definition['definition'] + "\n"
                self.question += question
                self.answer += temp_answer

    def get_fill_in_the_blanks_test(self):
        self.http_api_request()
        self.get_all_part_of_speech()
        self.json_to_readable_text()
        return {
            'question': self.question,
            'answer': self.answer
        }


test = RequestFillInTheBlanksTest("get")
res = test.get_fill_in_the_blanks_test()
print("Question:\n" + res['question'])
print("Answer:\n" + res['answer'])



# Get 10 words for definition test

# Get 5 words for synonyms test

# Get 25 words for fill-in-the-blanks test


text_file.close()
tenses_file.close()
