# !/usr/bin/python3
# 4-hidden_discovery.py
# Julius Okeyo <jaykopiyo@gmail.com>

if __name__ == "__main__":
    """Print all names defined by hidden_4 module."""
    from hidden import hidden_4

    names = dir(hidden_4)
    for name in names:
        if name[0] != '_':
            print(name)
