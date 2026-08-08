# -*- coding: utf-8 -*-
import sys, os, json, re
sys.stdout.reconfigure(encoding='utf-8')
import openpyxl

def clean_pinyin(p):
    if not p:
        return ""
    # Remove surrounding slashes like /ānwèi/
    p = str(p).strip()
    p = re.sub(r'^/', '', p)
    p = re.sub(r'/$', '', p)
    return p.strip()

def clean_str(v):
    if v is None:
        return ""
    return str(v).strip()

def parse_excel(filename, level):
    wb = openpyxl.load_workbook(filename)
    ws = wb.worksheets[0]  # first sheet
    
    vocab = []
    uid = 1
    
    for row in ws.iter_rows(min_row=3, values_only=True):
        stt = row[0]
        if stt is None or not str(stt).strip().isdigit():
            continue
        
        word = clean_str(row[1])
        pinyin = clean_pinyin(row[2])
        pos = clean_str(row[3])
        meaning = clean_str(row[5])
        ex_sent = clean_str(row[6])
        ex_pin = clean_pinyin(row[7])
        ex_meaning = clean_str(row[8])
        
        if not word:
            continue
        
        meanings = [m.strip() for m in meaning.split('\n') if m.strip()]
        if not meanings:
            meanings = [meaning] if meaning else []
        
        examples = []
        if ex_sent:
            examples.append({
                "sentence": ex_sent,
                "pinyin": ex_pin,
                "meaning": ex_meaning
            })
        
        vocab.append({
            "id": uid,
            "word": word,
            "pinyin": pinyin,
            "pos": pos,
            "meanings": meanings,
            "examples": examples
        })
        uid += 1
    
    return vocab

files = [
    ("File Excel luyện gõ từ vựng HSK 1.xlsx", 1, "vocab_hsk1.js"),
    ("File Excel luyện gõ từ vựng HSK 2.xlsx", 2, "vocab_hsk2.js"),
    ("File Excel luyện gõ từ vựng HSK 3.xlsx", 3, "vocab_hsk3.js"),
    ("File Excel luyện gõ từ vựng HSK 4.xlsx", 4, "vocab_hsk4.js"),
    ("File Excel luyện gõ từ vựng HSK 5.xlsx", 5, "vocab_hsk5.js"),
    ("File Excel luyện gõ từ vựng HSK 6.xlsx", 6, "vocab_hsk6.js"),
]

base = r"d:\hhhssskkk"
for fname, level, outname in files:
    path = os.path.join(base, fname)
    outpath = os.path.join(base, outname)
    data = parse_excel(path, level)
    js = f"const VOCAB_HSK{level} = " + json.dumps(data, ensure_ascii=False, separators=(',', ':')) + ";"
    with open(outpath, 'w', encoding='utf-8') as f:
        f.write(js)
    print(f"HSK{level}: {len(data)} từ -> {outname}")

print("Done!")
