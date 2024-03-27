import nltk
import json

# 英文を日本語の品詞に分解する
# 日本語と英語の品詞名対応辞書を作る
pos_dict = {
    'CC': '接続詞',
    'CD': '基数',
    'DT': '限定詞',
    'EX': '存在詞',
    'FW': '外来語',
    'IN': '前置詞',
    'JJ': '形容詞',
    'JJR': '形容詞比較級',
    'JJS': '形容詞最上級',
    'LS': 'リスト項目マーカ',
    'MD': '助動詞',
    'NN': '名詞',
    'NNS': '名詞複数形',
    'NNP': '固有名詞',
    'NNPS': '固有名詞複数形',
    'PDT': '前置限定詞',
    'POS': '所有格マーカ',
    'PRP': '人称代名詞',
    'PRP$': '所有代名詞',
    'RB': '副詞',
    'RBR': '副詞比較級',
    'RBS': '副詞最上級',
    'RP': '助詞',
    'SYM': '記号',
    'TO': 'to',
    'UH': '感嘆詞',
    'VB': '動詞',
    'VBD': '動詞過去形',
    'VBG': '動詞現在分詞',
    'VBN': '動詞過去分詞',
    'VBP': '動詞現在形',
    'VBZ': '動詞三人称単数現在形',
    'WDT': 'Wh-限定詞',
    'WP': 'Wh-代名詞',
    'WP$': '所有Wh-代名詞',
    'WRB': 'Wh-副詞',
    '.': "句点",
    ',': "読点",
    ':': "コロン",
    '``': "開き二重引用符",
    "''": "閉じ二重引用符",
    "$": "通貨記号",
}

# 英文を日本語の品詞に分解する
def pos_tagging(text):
    # 英文を単語に分解
    words = nltk.word_tokenize(text)
    # 単語の品詞を取得
    pos = nltk.pos_tag(words)
    # 品詞を日本語に変換
    pos_jp = []
    # json形式に整える
    for p in pos:
        pos_jp.append({"word": p[0], "pos": pos_dict[p[1]]})
    return pos_jp

# 行単位で重複を削除する
with open("./model/english_sentences.txt", "r") as f:
    text = f.readlines()
    text = list(set(text))
    with open("./model/english_sentences.txt", "w") as f:
        f.writelines(text)

with open("./model/english_sentences.txt", "r") as f:
    text = f.readlines()
    result = []
    for t in text:
        m = pos_tagging(t)
        result.append(m)
        print(m)
    with open("./model/sentences_and_pos.json", "w") as f:
        json.dump(result, f, ensure_ascii=False, indent=4)

# jsonファイルを読み込み、前置詞が文章に含まれていない文章をjsonから削除する
with open("./model/sentences_and_pos.json", "r") as f:
    data = json.load(f)
    result = []
    for d in data:
        flag = False
        for p in d:
            if p["pos"] == "前置詞":
                flag = True
                break
        if flag:
            result.append(d)
    with open("./model/sentences_and_pos.json", "w") as f:
        json.dump(result, f, ensure_ascii=False, indent=4)