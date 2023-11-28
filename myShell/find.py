import sys

print(111)
[_, command] = sys.argv
where_to_save = None
try:
    if '>' in command:
        command = command.split(' > ')
        where_to_save = command[1]
        command = command[0]

    file_path = command.split(' ')[1]
    string_to_find = command.split(' ')[2]


except Exception as e:
    print('Arguments Error:\nYour command should look like this:\n\nfind <file_path> <string_to_find>')

data = ''
lines = ''
line_number = 1
try:
    with open(file_path, 'r') as file:
        while True:
            data = file.readline()
            if string_to_find in data.lower():
                line = f"    {line_number}   : {data}"
                print(line)
                lines += line + '\n'
            elif not data:
                break
            line_number += 1

    # keeping result to file
    if where_to_save is not None:
        with open('temp_save.txt', 'w') as f:
            f.truncate()  # deleting all file data
            f.write(lines)  # put data into temp results file

except FileNotFoundError:
    print(f"Error: File not found at path {file_path}")
except Exception as e:
    print(f"Error: {e}")


