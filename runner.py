from Include.Compiler import compiler
from Include.File_Managment import filemanagment

def main(file):
    program = filemanagment.filemanagement(file)
    pyprogram = compiler.compile_program(program)
    print(pyprogram)

if __name__ == '__main__':
    main(file=r'Include\Compiler\Example\example1.at')
    