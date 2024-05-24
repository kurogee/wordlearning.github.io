import pandas as pd
import json

# csvファイルを読み込む
df = pd.read_csv('./histories.csv')
year = list(map(str, list(df["年"])))
event = list(df["出来事・用語"])
another_answer = list(map(lambda x: x.split("、") if type(x) is not float else [], list(df["別解"])))
detail = list(df["詳細"])

# jsonファイルに書き込む
data = []
for i in range(len(year)):
    data.append({
        "year": year[i],
        "event": event[i],
        "another_answer": another_answer[i],
        "detail": detail[i]
    })

with open('./histories.json', 'w') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
