from __future__ import annotations

import argparse
import ast
from typing import Sequence
from .util import current_branch, last_commit_id

MANIFEST_NAMES = ("__manifest__.py", "__openerp__.py")


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*')
    args = parser.parse_args(argv)

    for filename in [filename for filename in args.filenames if filename in MANIFEST_NAMES]:
        manifest = {}

        with open(filename, 'r', encoding='utf-8') as file:
            manifest = ast.literal_eval(file.read())
            file.close()

        manifest["version"] = last_commit_id() + "@" + current_branch()

        with open(filename, 'w', encoding='utf-8') as file:
            file.write(str(manifest))
            file.close()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
