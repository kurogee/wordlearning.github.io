import json
import requests
from bs4 import BeautifulSoup
import fake_useragent
from googletrans import Translator

def make_sentence(english_word):
    url = 'https://www.oxfordlearnersdictionaries.com/definition/english/' + english_word
    response = requests.get(url, headers={'User-Agent': fake_useragent.UserAgent().random})
    soup = BeautifulSoup(response.text, 'html.parser')
    sentence = soup.find('span', {'class': 'x'}).text
    return sentence

def translate(sentence):
    translator = Translator()
    return translator.translate(sentence, src="en", dest='ja').text


# jsonファイルを読み込む
with open('./verbs.json', 'r') as f:
    words = json.load(f)

for i in range(len(words)):
    # 1つの単語に対して例文を取得
    word = words[i]
    sentence = make_sentence(word.get('word'))
    sentence_ja = translate(sentence)

    # jsonファイルに追加して書き込む
    words[i]['sentence'] = sentence
    words[i]['sentence_ja'] = sentence_ja
    with open('./verbs.json', 'w') as f:
        json.dump(words, f, indent=2, ensure_ascii=False)