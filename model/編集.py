import pandas as pd
import json

# # csvファイルを読み込む
# df = pd.read_csv('./eiken_2.csv')
# word = list(df["word"])
# meaning = list(df["meaning"])
# 
# # jsonファイルに書き込む
# data = []
# for i in range(len(word)):
#     data.append({
#         "id" : "e2:" + str(i),
#         "word": word[i],
#         "meaning": meaning[i]
#     })
# 
# with open('./eiken_2.json', 'w') as f:
#     json.dump(data, f, ensure_ascii=False, indent=4)

filename = "jhs_all_words"

# jsonファイルのすべてのデータにidを追加する
with open(f'./{filename}.json', 'r') as f:
    data = json.load(f)

for i in range(len(data)):
    data[i]["id"] = "jaw3:" + str(i)

with open(f'./{filename}.json', 'w') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)