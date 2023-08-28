import string
from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

def preprocessing(sentence):
    sentence = sentence.strip() # remove white space
    sentence = sentence.lower() # lower characters
    sentence = ''.join(char for char in sentence if not char.isdigit()) # remove num
    for punctuation in string.punctuation:
        sentence = sentence.replace(punctuation, ' ') # remove punctuations
        word_tokens = word_tokenize(sentence) # tokenizeing

        stop_words = set(stopwords.words('english'))
        word_tokens=[w for w in word_tokens if not w in stop_words]
        

        verb_lemmatized = [                  
            WordNetLemmatizer().lemmatize(word, pos = "v") # v --> # Lemmatizing the verbs
            for word in word_tokens
        ]
    
        noun_lemmatized = [                 
            WordNetLemmatizer().lemmatize(word, pos = "n") # n --> # Lemmatizing the nouns
            for word in verb_lemmatized
        ]
    
        word_lemmatized=' '.join([w for w in verb_lemmatized])

    return word_lemmatized