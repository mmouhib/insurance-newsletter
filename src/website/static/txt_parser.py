def text(path):
    with open(path) as f:
        content = f.readlines()
    return ''.join(content)  # converts list to str and returns it
