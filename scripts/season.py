from nltk.tokenize import sent_tokenize, word_tokenize 
from nltk.corpus import stopwords
import pdb
import sys
x=sys.argv[1] 
stop_words = set(stopwords.words('english')) 
word_tokens = word_tokenize(x) 
filtered_sentence = [w for w in word_tokens if not w in stop_words] 
  
filtered_sentence = [] 
  
for w in word_tokens: 
    if w not in stop_words: 
        filtered_sentence.append(w)

if 'season' in filtered_sentence:
    print('true')
elif 'seasons' in filtered_sentence:
    print('true')
elif 'Season' in filtered_sentence:
    print('true')
elif 'Seasons' in filtered_sentence:
    print('true')
else:
    print('null')