# log_util.py
# A homemade logger. The logging module felt like "too much magic" in 2013.

import time

LOG_LINES: list[str] = []   # global state, shared by everyone who imports this


def log(message: str) -> None:
    """Append a timestamped line to LOG_LINES and print it."""
    stamp = time.strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{stamp}] {message}"
    LOG_LINES.append(line)
    print(line)


def flush_log(path: str) -> None:
    """Write all buffered log lines to path and clear the buffer."""
    with open(path, "a") as f:
        for line in LOG_LINES:
            f.write(line + "\n")
    LOG_LINES.clear()
