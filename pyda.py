import wolframalpha

input = input("Question: ")
app_id = "VWTYR8-69K4JLGKL8"
client = wolframalpha.Client(app_id)

res = client.query(input)
answer = next(res.results).text

print(answer)