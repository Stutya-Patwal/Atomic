import os

def open_file(file):
    f = open(file, "r")
    program = f.read()
    f.close()
    return program

def is_at(filepath):
    filename, extension = os.path.splitext(filepath)
    if extension.lower() == ".at":
        return True
    else:
        return False

def filemanagement(file):
    content = open_file(file)
    verification = is_at(file)
    if verification:
        return content
    else:
        return False


