
import nltk
text = "This is Andrew's text, isn't it"

def printToken(text):
    print(text)

tokenizer = nltk.tokenize.WhitespaceTokenizer()
printToken(tokenizer.tokenize(text))

tokenizer = nltk.tokenize.TreebankWordTokenizer()
printToken(tokenizer.tokenize(text))

tokenizer = nltk.tokenize.WordPunctTokenizer()
printToken(tokenizer.tokenize(text))