import pandas as pd
import json
import MeCab
import math

# csvファイルを読み込む
df = pd.read_csv('./histories.csv')
year = list(map(str, list(df["年"])))
event = list(df["出来事・用語"])
another_answer = list(map(lambda x: x.split("、") if type(x) is not float else [], list(df["別解"])))
detail = list(df["詳細"])
era = list(df["時代"])
print(df["世紀"])
seiki = list(map(lambda x : "世紀" if x == "世紀" else "", list(df["世紀"])))
# detailを分かち書きすして、名詞や固有名詞のみを取り出す
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
for i in range(len(year)):
    data.append({
        "year": year[i],
        "century": seiki[i],
        "era": era[i],
        "event": event[i],
        "another_answer": another_answer[i],
        "detail": detail[i],
        "detail_wakati": detail_wakati[i]
    })

with open('./histories.json', 'w') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
