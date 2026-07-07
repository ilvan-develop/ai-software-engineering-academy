"""Fix mis-closed code blocks in individual chapter files."""
import os

base = r'C:\Users\Ilvan\Desktop\GitHub Apps\AI Software Engineering Academy\knowledge-factory\products\books\backend-architecture\compiled'
files = [f'capitulo-{i:02d}.md' for i in range(1, 9)]

total = 0
for fname in files:
    path = os.path.join(base, fname)
    if not os.path.exists(path):
        print(f'{fname}: not found')
        continue
    
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    lines = content.split('\n')
    fixes = 0
    for i in range(len(lines)):
        line = lines[i].strip()
        if line == '```text':
            j = i - 1
            while j >= 0 and lines[j].strip() == '':
                j -= 1
            if j >= 0:
                prev = lines[j].strip()
                if prev.endswith('}') or prev.endswith(');') or prev.endswith(';') or '```' in prev or prev.endswith('>') or prev.endswith('/'):
                    lines[i] = lines[i].replace('```text', '```')
                    fixes += 1
    
    if fixes:
        with open(path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(lines))
        print(f'{fname}: fixed {fixes} blocks')
        total += fixes
    else:
        print(f'{fname}: no issues')

print(f'Total: {total} fixes across all chapter files')
