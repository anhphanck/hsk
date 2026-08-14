with open(r'D:\hhhssskkk\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix 1 & 3: \u01co -> \u01ce (letter 'o' instead of digit '0' in position 4)
# Affects lines 3132 and 3154: li\u01coji\u011b -> li\u01ceoji\u011b
content = content.replace('\\u01coji', '\\u01ceoji')

# Fix 2: \u00fo -> \u00f9 (letter 'o' instead of digit '9' in position 4)
# Affects line 3138: x\u00fons -> x\u00f9ns
content = content.replace('\\u00fons', '\\u00f9ns')

with open(r'D:\hhhssskkk\index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done! Fixed all invalid Unicode escapes.")

# Verify no more invalid escapes
hex_chars = set('0123456789abcdefABCDEF')
errors = []
for i, line in enumerate(content.splitlines(), 1):
    pos = 0
    while True:
        idx = line.find('\\u', pos)
        if idx == -1:
            break
        seq = line[idx+2:idx+6]
        if len(seq) == 4:
            for j, ch in enumerate(seq):
                if ch not in hex_chars:
                    errors.append(f"Line {i}: \\u{seq!r} invalid at pos {j}")
                    break
        pos = idx + 1

if errors:
    print("Still found errors:")
    for e in errors:
        print(e)
else:
    print("No more invalid Unicode escapes found!")
