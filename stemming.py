
import nltk
from nltk.corpus import wordnet
text = "feet cats wolves talked"

tokenizer = nltk.tokenize.TreebankWordTokenizer()
tokens = tokenizer.tokenize(text)

stemmer = nltk.stem.PorterStemmer()
print(" ".join(stemmer.stem(token) for token in tokens))

stemmer = nltk.stem.WordNetLemmatizer()
print(" ".join(stemmer.lemmatize(token) for token in tokens))
