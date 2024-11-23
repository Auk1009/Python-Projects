import requests
from bs4 import BeautifulSoup
import nltk

nltk.download('punkt')
from nltk.tokenize import sent_tokenize

url = 'https://www.freecodecamp.org/news/python-projects-for-beginners/'

response = requests.get(url)

if response.status_code == 200:

    soup = BeautifulSoup(response.text,'html.parser')
    titles = soup.find("h2",id="heading-python-projects-you-can-build")
    paragraphs = soup.find_all('p')
    
    for title in titles:
        print(title.text.strip())

    all_text = " ".join(paragraph.text.strip() for paragraph in paragraphs)

    sentence = sent_tokenize(all_text)
    num_sen = 3
    summary = ' '.join(sentence[:num_sen])
    print('summary of the article')
    print(summary)
else:
    print(f'failed status code: {response.status_code}')