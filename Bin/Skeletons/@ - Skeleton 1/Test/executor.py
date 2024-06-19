import re

keywords = ("show", "func", "def")
mainprogram = ""

def open_file(file):
    f = open(file, "r")
    program = f.read()
    f.close()
    return program

def clear(program):
    program = re.sub(r'//.*?//', '', program)
    return program

def interpret(program):
    global mainprogram
    mainprogram += "#Om Gan Gan Pataye Namah"
    for line in program.split('\n'):
        for keyword in keywords:
            if keyword in line:
                process(keyword, line)
                break  

def tokenization(sentence):
    tokens = []

    for word in sentence.split():
        tokens.append(word)

    return tokens

def process(keyword, line):
    global mainprogram
    if keyword == "show":
        tokens = tokenization(line)
        int_token = tokens[0].replace(":","")
        try:
            place = int(int_token)
            valueint = True
        except:
            valueint = False
        if valueint:
            line = line.replace(":","")
            line = line.replace(int_token,"")
            line = line.replace("(","")
            line = line.replace("show","")
            line = line.replace(")","")
            if '"' in line:
             line = line.replace('"','')
             line = f'print("{line}")'
            else:
                line = f'print({line})'
            index = 0
            for char in line:
                if char != '  ':
                    break
                index += 1
            line = line[index:]
            insert_at_line = place  
            lines = mainprogram.split('\n')

            if insert_at_line <= len(lines):
                lines.insert(insert_at_line - 1, line)
            else:
                lines.append(line)
            mainprogram = '\n'.join(lines)
        else:
            line = line.replace("(","")
            line = line.replace("show","")
            line = line.replace(")","")
            if '"' in line:
                 line = line.replace('"','')
                 line = f'print("{line}")'
            else:
                line = f'print({line})'
            line = f'\n{line}'
            mainprogram += line     
    elif keyword == "def":
        tokens = tokenization(line)
        int_token = tokens[0].replace(":","")
        try:
            place = int(int_token)
            valueint = True
        except:
            valueint = False
        if valueint:
            line = line.replace(":","")
            line = line.replace(int_token,"")
            line = line.replace("def","")
            index = 0
            for char in line:
                if char != ' ':
                    break
                index += 1
            line = line[index:]
            insert_at_line = place  
            lines = mainprogram.split('\n')

            if insert_at_line <= len(lines):
                lines.insert(insert_at_line - 1, line)
            else:
                lines.append(line)
            mainprogram = '\n'.join(lines)
        else:
            line = line.replace("def","")
            mainprogram += f"\n{line}"
    elif keyword == "func":
        tokens = tokenization(line)
        int_token = tokens[0].replace(":","")
        try:
            place = int(int_token)
            valueint = True
        except:
            valueint = False
        if valueint:
            name = tokens[2]
            line = line.replace(":","")
            line = line.replace(int_token,"")
            line = line.replace("func","def")
            index = 0
            for char in line:
                if char != ' ':
                    break
                index += 1
            line = line[index:]
            insert_at_line = place  
            lines = mainprogram.split('\n')

            if insert_at_line <= len(lines):
                lines.insert(insert_at_line - 1, line)
            else:
                lines.append(line)
            mainprogram = '\n'.join(lines)
        else:
            line = line.replace("def","")
            mainprogram += line


interpret(clear(open_file("example.txt")))
print(mainprogram)
exec(mainprogram)











