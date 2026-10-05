import re
from pathlib import Path

content = Path('content')
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


PARTS = {
    'front': [
        # '0-front'
    ],
    'center': [
        '1-intro',
        '2-background',
        '3-theory',
        '4-impl',
        # '5-res'
    ]
}

for key in PARTS:
    processed = []
    for name in PARTS[key]:
        source = content / f'{name}.tex'
        text = source.read_text(encoding='utf-8')
        text = re.sub(r'(?:^%[^ ].+$\n?)+', sub, text, flags=re.MULTILINE)
        processed.append(text)
    (build / f'_{key}.tex').write_text('\n'.join(processed), encoding='utf-8')
