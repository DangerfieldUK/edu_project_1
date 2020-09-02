import fileinput

with fileinput.input("romeo_juliet_script.txt", True, '.bak') as file:
    for line in file:
        line = line.replace('Juliet', 'Karen').replace('JULIET', 'KAREN')
        print(line)
