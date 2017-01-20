import wikipedia
while True:
    query = input("Query :")
    wikipedia.set_lang("en")
    result = wikipedia.summary(query, sentences = 2).encode('utf-8')
    print (result)
