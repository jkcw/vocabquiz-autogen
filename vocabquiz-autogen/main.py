import requests
import json
import random

from . import secretKey

print(secret_key)

# TODO: get some of questions only, not all.
# TODO: present tense, verbs with "s"
# TODO: full stop of each sentence
# TODO: will print the error msg out "error:rm_answer_to_blank"
# TODO: quality of the dictionary is too low

# Load vocabulary list
text_file = open("temp/ietls-vocab-list.txt", "r")
vocab_list = json.load(text_file)

last_vocab = "yield"
last_vocab_index = vocab_list.index(last_vocab)
print(last_vocab_index)

# Load tenses list
tenses_file = open('temp/tenses-list.json', "r")
tenses_dict = json.load(tenses_file)





# TODO
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


# TODO
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
                if tense in sentence.split():
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
        if not self.http_api_request():
            return {
                'question': "Error:" + self.vocab,
                'answer': "Error:" + self.vocab
            }
        self.get_all_part_of_speech()
        self.json_to_readable_text()
        return {
            'question': self.question,
            'answer': self.answer
        }

"""
index_list = random.sample(range(500, last_vocab_index), 40)

temp_qes = ""
temp_ans = ""
n = 1
for index in index_list:
    print(n)
    request_obj = RequestFillInTheBlanksTest(vocab_list[index])
    result = request_obj.get_fill_in_the_blanks_test()

    if len(result['question']) > 0:
        temp_qes += result['question']
        temp_ans += result['answer']

    n += 1

print("Question:\n" + temp_qes)
print("Answer:\n" + temp_ans)
"""



# Get 10 words for definition test

# Get 5 words for synonyms test

# Get 25 words for fill-in-the-blanks test


text_file.close()
tenses_file.close()
