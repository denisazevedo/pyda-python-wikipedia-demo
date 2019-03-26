import wikipedia
import wolframalpha

while True:
    question = input("Question: ")

    try:
        # wolframalpha
        app_id = "VWTYR8-69K4JLGKL8"
        client = wolframalpha.Client(app_id)
        res = client.query(question)
        answer = next(res.results).text
        print("From Wolfram|Alpha: {}".format(answer))

    except:
        # wikipedia
        wikipedia.set_lang("pt")
        answer = wikipedia.summary(question, sentences=2)
        print("From Wikipedia: {}".format(answer))
        