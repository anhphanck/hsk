import re

with open(r'D:\hhhssskkk\index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

hex_chars = set('0123456789abcdefABCDEF')

for i, line in enumerate(lines, 1):
    # Find all \uXXXX patterns in the line
    pos = 0
    while True:
        idx = line.find('\\u', pos)
        if idx == -1:
            break
        # Check the 4 chars after \u
        seq = line[idx+2:idx+6]
        if len(seq) == 4:
            for j, ch in enumerate(seq):
                if ch not in hex_chars:
                    print(f"Line {i}, col {idx}: \\u{seq!r} - invalid char '{ch}' at pos {j}")
                    print(f"  Context: {line[max(0,idx-20):idx+30].strip()}")
                    break
        pos = idx + 1
