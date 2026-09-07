import re
from pathlib import Path

build = Path('build')
build.mkdir(exist_ok=True)


def sub(m):
    lines = m.group(0).strip().split('\n')
    stmts = []
    for line in lines:
        stmt = line[1:]
        if stmt.startswith("'"):
            stmt = f'\\textit{{{stmt.removeprefix("'")}}}'
        else:
            for prefix, color in {'!': 'red', '*': 'green!75!black'}.items():
                if stmt.startswith(f'{prefix}'):
                    stmt = f'{{\\color{{{color}}}{stmt.removeprefix(f'{prefix}')}}}'
        stmts.append(stmt)
    return f'\\comment{{{'\\\\'.join(stmts)}}}\n'


for f in Path('content').glob('*.tex'):
    f_ = build / f.name

    # preprocess only changed files
    if True or not f_.is_file() or f.stat().st_mtime > f_.stat().st_mtime:
        text = f.read_text(encoding='utf-8')

        text = re.sub(r'(?:^%[^ ].+$\n?)+', sub, text, flags=re.MULTILINE)

        f_.write_text(text)
