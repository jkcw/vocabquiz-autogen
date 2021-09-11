import json

text_file = open("res.txt", "r")
res_file = open("res-no-blanks.txt", "w")
res = []

for vocab in text_file:
    vocab = vocab.strip("\n")
    vocab = vocab.strip("\f")
    print(vocab)
    if vocab != "" and vocab != "HEB IAL":
        res.append(vocab)

jsonString = json.dumps(res)
res_file.write(jsonString)

text_file.close()
res_file.close()
