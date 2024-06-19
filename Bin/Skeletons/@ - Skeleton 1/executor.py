import os
import re

global mainprogram
mainprogram = "#Om Gan Gan Pataye"

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

def clear(program):
    program = re.sub(r'//.*?//', '', program)
    return program

def append_to_program(new_content):
    global mainprogram
    mainprogram += '\n' + new_content

def enclose_word_after_double_ampersand(string):   
    index_of_double_ampersand = string.find('&&')
    
    if index_of_double_ampersand != -1:
        start_index = index_of_double_ampersand + 2
        end_index = start_index
        while end_index < len(string) and string[end_index].isalnum():
            end_index += 1
        new_string = string[:start_index] + '{' + string[start_index:end_index] + '}' + string[end_index:]

        new_string = new_string.replace("&&","")
        
        return new_string
    else:
        return string

def compile_program(program,program_sen):
    for line in program_sen:
        imp_line = re.sub(r'".*?"', '', line)
        if "display" in imp_line and not "&&" in line:
            line = line.replace("display","print")
            append_to_program(line)
        if " = " in imp_line and not "get" in imp_line:
            #tokenization_ = tokenization(line)
            #name = tokenization_[0] 
            #value = tokenization_[2]
            append_to_program(line)
        if "&&" in line: 
            line = enclose_word_after_double_ampersand(line)
            line = line.replace("display(","print(f")
            line = line.replace('"}',"")
            append_to_program(line)
        if "Requires" in imp_line:
            line = line.replace("Requires","import")
            append_to_program(line)
        if "get" in imp_line:
            line = line.replace("get","input") 
            append_to_program(line)

    print(mainprogram)
    return mainprogram
        

def execution(file):
    program = open_file(file)
    program = clear(program)
    program = normalize(program)
    program_sen = sentence_seg(program)
    python_program = compile_program(program, program_sen)


def sentence_seg(program):
    output_list = program.split('\n')
    output_list = [item for item in output_list if item]
    return output_list


def tokenization(sentence):
    tokens = []

    for word in sentence.split():
        tokens.append(word)

    return tokens

def normalize(variable_x):
    lines = variable_x.split('\n')

    def get_number(line):
        if ':' in line:
            try:
                return int(line.split(':')[1].split()[0])
            except ValueError:
                return float('inf')
        else:
            return float('inf')
    sorted_lines = sorted(lines, key=get_number)
    sorted_lines = [line.split(':', 1)[-1].strip() if ':' in line and line.split(':')[1].strip() else line for line in sorted_lines]
    sorted_string = '\n'.join(sorted_lines)
    return sorted_string





def main():
    file = "program.at"
    if is_at(file):
        execution(file)
    else:
        print("Only .at (@) files")

    
main()
