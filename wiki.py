# https://pypi.org/project/wikipedia/1.4.0/
import wikipedia

while True:
    question = input("Question: ")
    wikipedia.set_lang("pt")
    res = wikipedia.summary(question, sentences=2)
    print(res)
