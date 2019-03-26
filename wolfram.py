import wolframalpha

question = input("Question: ")
app_id = "VWTYR8-69K4JLGKL8"
client = wolframalpha.Client(app_id)

res = client.query(question)
answer = next(res.results).text

print(answer)