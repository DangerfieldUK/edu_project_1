import fileinput

with fileinput.input("romeo_juliet_script.txt", True, '.bak') as file:
    for line in file:
        line = line.replace('Karen', 'Juliet').replace('KAREN', 'JULIET')
        print(line)
