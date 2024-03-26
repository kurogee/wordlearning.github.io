import json
from pattern.en import conjugate, PAST, PARTICIPLE

def generate_past_tense(verb):
    past_tense = conjugate(verb, tense=PAST)
    return past_tense

# 過去分詞形を生成する
def generate_past_participle(verb):
    past_participle = conjugate(verb, tense=PAST, aspect=PARTICIPLE)
    return past_participle

# jsonファイルを読み込む
with open('./verbs.json', 'r') as f:
    words = json.load(f)

for i in range(len(words)):
    word = words[i]['word']
    past_form = generate_past_tense(word)
    words[i]['past_form'] = past_form
    print(f'{word} - {past_form}')

# jsonファイルに書き込む
with open('./verbs_past.json', 'w') as f:
    json.dump(words, f, indent=4, ensure_ascii=False)