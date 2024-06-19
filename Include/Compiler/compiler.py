import re
from inquirer import prompt, List
from random import choice

mainprogram = "#@ Code - Stutya Patwal"
keywords = ("display","let")
built_in_functions = ("copy")

def putvalues(p,q):
    mcqdata = '''
    questions = [
        List('choice',
            message={q},
            choices={o},
            carousel=True),
    ]'''

def getvaluesofmcq(hello22):
    match = re.search(r"inquire\.mcq\(q=(.+?),o=(.+)\)", hello22)
    if match:
        q_value = match.group(1)
        o_values = [value.strip() for value in match.group(2).split(",")]
        return q_value, o_values
    else:
        return None

def valnum(text):
    lines = [line.strip() for line in text.split("\n")]

    def has_number(line):
        for i, char in enumerate(line):
            if not char.isdigit() and char != ':':
                return line[:i].strip(':')
        return line.strip(':')

    def get_number(line):
        num = has_number(line)
        return int(num) if num else float('inf')  # Use infinity for lines without numbers

    sorted_lines = sorted(lines, key=get_number)

    return "\n".join(line[len(has_number(line)) + 1:].strip() if has_number(line) else line for line in sorted_lines)

def addtab(s):
    lines = s.split('\n')
    indent_level = 0
    for i, line in enumerate(lines):
        if '{' in line:
            lines[i] = line.replace('{', ':')
            indent_level += 1
        elif '}' in line:
            if indent_level > 0:
                indent_level -= 1
            lines[i] = ''
        else:
            lines[i] = '  ' * indent_level + line.lstrip()
    return '\n'.join([line for line in lines if line.strip()])

def clear(program):
    program = re.sub(r'//.*?//', '', program)
    return program

def clear22(program):
    program = re.sub(r'".*?"', '', program)
    return program

def sentence_seg(program):
    output_list = program.split('\n')
    output_list = [item for item in output_list if item]
    return output_list

def append_to_program(new_content):
    global mainprogram
    mainprogram += '\n' + new_content

def compile_program(program):
    global mainprogram
    program = clear(program)
    program = valnum(program)
    program = addtab(program)
    programseg = sentence_seg(program)
    for line in programseg:
        line = re.sub(r'display\(([^)]*)\)', r'print(\1)', line)
        line = re.sub(r'out\(([^)]*)\)', r'print(\1)', line)
        line = re.sub(r'MAYBE', str(choice([False, True])), line)
        line = re.sub(r'inquire\.text\("(.*)"\)', r'input("\1")', line)
        line = re.sub(r'\&\&', 'and', line)
        line = re.sub(r'\!\!', 'not', line)
        line = re.sub(r'\|\|', 'or', line)
        line = re.sub(r'If (.*):', r'if \1:', line)
        line = re.sub(r'func (.*):', r'def \1:', line)
        line = re.sub(r'Or (.*):', r'elif \1:', line)
        line = re.sub(r'None:', r'else:', line)
        append_to_program(line)
    
    return mainprogram





