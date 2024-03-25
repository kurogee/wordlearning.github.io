import json
import pandas as pd

# 動詞集.csvを読み込む
df = pd.read_csv('熟語.csv')
# 動詞集.csvの中身をjson形式に変換
words = df.to_dict(orient='records')

print(words)
# simple.jsonにwordsを書き込む
with open('idioms.json', "w") as f:
    json.dump(words, f, indent=4, ensure_ascii=False)