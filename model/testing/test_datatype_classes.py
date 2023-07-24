import re


class DateTime(str):
    def __new__(cls, val):
        if re.match(r"^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$", val):
            return super().__new__(cls, val)
        raise ValueError(f'"{val}" does not match DateTime pattern')


if __name__ == '__main__':
    for v in ('2023-04-13T11:15:00Z', 'Fred', 42, None):
        try:
            dt = DateTime(v)
            print(f'   OK: {dt}')
        except (ValueError, TypeError) as e:
            print(f'Error: {v}: {e}')
