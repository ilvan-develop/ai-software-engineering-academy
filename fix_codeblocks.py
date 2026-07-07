"""Fix mis-closed code blocks in backend-architecture book.md."""
import re

with open(r'C:\Users\Ilvan\Desktop\GitHub Apps\AI Software Engineering Academy\knowledge-factory\products\books\backend-architecture\compiled\book.md', 'r', encoding='utf-8') as f:
    content = f.read()

lines = content.split('\n')
fixes = []
for i in range(len(lines)):
    line = lines[i].strip()
    if line == '```text':
        # Check if previous non-empty line looks like code (ends with bracket/semicolon)
        j = i - 1
        while j >= 0 and lines[j].strip() == '':
            j -= 1
        if j >= 0:
            prev = lines[j].strip()
            # Code blocks typically end with }, ), ;, or similar
            if prev.endswith('}') or prev.endswith(');') or prev.endswith(';') or '```' in prev or prev.endswith('>') or prev.endswith('/'):
                fix = (i, prev)
                fixes.append(fix)

for lineno, prev in fixes:
    lines[lineno] = lines[lineno].replace('```text', '```')

result = '\n'.join(lines)
with open(r'C:\Users\Ilvan\Desktop\GitHub Apps\AI Software Engineering Academy\knowledge-factory\products\books\backend-architecture\compiled\book.md', 'w', encoding='utf-8') as f:
    f.write(result)

print(f'Fixed {len(fixes)} code block closings')
for lineno, prev in fixes[:5]:
    print(f'  L{lineno}: prev=[{prev[:50]}]')
if len(fixes) > 5:
    print(f'  ... and {len(fixes)-5} more')
