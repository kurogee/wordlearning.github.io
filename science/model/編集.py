import pandas as pd
import json
import MeCab
import math

# csvファイルを読み込む
df = pd.read_csv('./science.csv')
grade = list(map(str, list(df['学年'])))
field = list(df['分野'])
word = list(df['用語'])
another_word = list(map(lambda x: x.split("、") if type(x) is not float else [], list(df["別解"])))
detail = list(df['詳細'])

# detailを分かち書きして、名詞や固有名詞のみを取り出す
detail_wakati = []
mecab = MeCab.Tagger("-d /usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ipadic-neologd")
for i in range(len(detail)):
    node = mecab.parseToNode(detail[i])
    detail_wakati.append([])
    while node:
        if node.feature.split(",")[0] == "名詞" and node.feature.split(",")[1] != "数" and node.feature.split(",")[1] != "非自立":
            # 「もの」や、「こと」などの名詞は除外
            if node.surface != "もの" and node.surface != "こと" and node.surface != "これ" and node.surface != "出来事" and len(node.surface) != 1:
                detail_wakati[i].append(node.surface.replace("。", ""))
        node = node.next

# jsonファイルに書き込む
data = []
for i in range(len(grade)):
    data.append({
        "grade": grade[i],
        "field": field[i],
        "word": word[i],
        "another_word": another_word[i],
        "detail": detail[i],
        "detail_wakati": detail_wakati[i]
    })

with open('./science.json', 'w') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

# 「数のこ」を「数」に直しておこう
