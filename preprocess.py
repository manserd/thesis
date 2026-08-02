import re
from pathlib import Path

build = Path('build')
build.mkdir(exist_ok=True)

for f in Path('content').glob('*.tex'):
    f_ = build / f.name

    # preprocess only changed files
    if not f_.is_file() or f.stat().st_mtime > f_.stat().st_mtime:

        f_.write_text(re.sub(
            r'^% (.*)$',
            r'\\comment{\1}',
            f.read_text(encoding='utf-8'),
            flags=re.MULTILINE
        ), encoding='utf-8')
