import wikipedia
import wolframalpha

while True:
    inp_query = input("Query: ")
    try:
        app_id="AW8AWJ-GEGXVQVWLX"

        client = wolframalpha.Client(app_id)

        res = client.query(inp_query);

        answer = next(res.results).text
        print (answer)
    except:
        wikipedia.set_lang("en")
        result = wikipedia.summary(inp_query, sentences = 2).encode('utf-8')
        print (result)
