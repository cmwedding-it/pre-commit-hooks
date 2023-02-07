from __future__ import annotations

import subprocess
from typing import Any

def current_branch() -> str:
    cmd = ('git', 'branch', '--show-current', '--no-color')
    out = cmd_output(*cmd).strip()

    if not out or len(out) == 0:
        raise RuntimeError

    return out

def last_commit_id() -> str:
    cmd = ('git',  'log',  '-1', '--pretty=format:%h')
    out = cmd_output(*cmd).strip()

    if not out:
        raise RuntimeError

    if len(out) != 8:
        cmd = ('git', 'config', '--global', 'core.abbrev', '8')
        subprocess.Popen(cmd)
        return last_commit_id()

    print(out, len(out))
    return out

def cmd_output(*cmd: str, retcode: int | None = 0, **kwargs: Any) -> str:
    kwargs.setdefault('stdout', subprocess.PIPE)
    kwargs.setdefault('stderr', subprocess.PIPE)
    proc = subprocess.Popen(cmd, **kwargs)
    stdout, stderr = proc.communicate()
    stdout = stdout.decode()
    if retcode is not None and proc.returncode != retcode:
        raise RuntimeError(cmd, retcode, proc.returncode, stdout, stderr)
    return stdout