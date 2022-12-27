import paralleldots
paralleldots.set_api_key('ELcXEO5UrUPXcJshAyxOyp4g1okeNA2ukPtXYK45tmA')

def ner(text):
    ner = paralleldots.ner(text)
    return ner

def Sentiment(text):
    sentiments = paralleldots.sentiment(text)
    return sentiments
