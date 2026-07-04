#!/usr/bin/python3
"""Script that reads stdin line by line and computes metrics."""
import sys


def print_stats(total_size, status_codes):
    """Print accumulated statistics."""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code]:
            print("{}: {}".format(code, status_codes[code]))


def main():
    """Process log lines from standard input."""
    status_codes = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0
    }
    total_size = 0
    line_count = 0
    try:
        for line in sys.stdin:
            line_count += 1
            parts = line.split()
            try:
                total_size += int(parts[-1])
                code = parts[-2]
                if code in status_codes:
                    status_codes[code] += 1
            except (ValueError, IndexError):
                pass
            if line_count % 10 == 0:
                print_stats(total_size, status_codes)
    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise
    print_stats(total_size, status_codes)


if __name__ == "__main__":
    main()
