import json
import requests
from bs4 import BeautifulSoup
import fake_useragent
from googletrans import Translator

def make_sentence(english_word):
    # fake_useragentを使ってUser-Agentを取得
    ua = fake_useragent.UserAgent()
    headers = {
        'User-Agent': ua.random
    }

    # 英単語を使って例文を取得
    url = f'https://sentence.yourdictionary.com/{english_word}'
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    sentence = soup.find_all('p', class_='sentence-item__text')
    if len(sentence) == 0:
        print('No sentence:', english_word)
        return 'No sentence'
    return sentence[0].text

def translate(sentence):
    translator = Translator()
    return translator.translate(sentence, src="en", dest='ja').text


# jsonファイルを読み込む
with open('./verbs.json', 'r') as f:
    words = json.load(f)

for i in range(109, len(words)):
    try:
        # 1つの単語に対して例文を取得
        word = words[i]
        sentence = make_sentence(word.get('word'))
        sentence_ja = translate(sentence)
    except:
        print('Pass by error:', word.get('word'))
        continue
    finally:
        # jsonファイルに追加して書き込む
        # もしすでにsentenceがある場合は無視する
        if 'sentence' in words[i]:
            print('Already exist:', word.get('word'))
            continue
        words[i]['sentence'] = sentence
        words[i]['sentence_ja'] = sentence_ja
        with open('./verbs.json', 'w') as f:
            json.dump(words, f, indent=2, ensure_ascii=False)