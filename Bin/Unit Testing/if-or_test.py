def convert_brackets_to_colon(s):
    lines = s.split('\n')
    for i, line in enumerate(lines):
        if '{' in line:
            lines[i] = line.replace('{', ':')
            lines[i+1:] = ['    ' + l for l in lines[i+1:]]
    if lines[-1].strip() == '}':
        lines[-1] = ''
    return '\n'.join([line for line in lines if line.strip()])

input_string = '''display("hi")
if x == 5{
print("x is 5")
out("ok?")
}'''
output_string = convert_brackets_to_colon(input_string)
print(output_string)