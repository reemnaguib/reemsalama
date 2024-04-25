import nltk 
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
file=open('paragraphs.txt','r')
text=file.read()
print(text)
nltk.download('stopwords')
stop_words=set(stopwords.words('english'))
print(stop_words)
nltk.download('punkt')
main_words=word_tokenize(text)
type(main_words)
for word in main_words:
    print(word)
tokenized_words_without_stop_words=[]
for word in main_words:
    if word not in stop_words:
        tokenized_words_without_stop_words.append(word)
for word in tokenized_words_without_stop_words:
    print(word+" "+str(tokenized_words_without_stop_words.count(word)))
# docker build -t b 'path'
#docker run --name 'container' b