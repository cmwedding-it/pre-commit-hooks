from __future__ import annotations

import argparse
from typing import Sequence
import elevate
from .util import try_chmod

def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*')
    args = parser.parse_args(argv)

    for filename in args.filenames:
        if try_chmod(filename) == 1:
            elevate.elevate()
            if try_chmod(filename) == 1:
                return 1

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
