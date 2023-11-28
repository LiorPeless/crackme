import sys
import os

[_, command, current_directory] = sys.argv
# print(command)
# print(current_directory)

contents = ''
command
command = command.split(' ')
if len(command) == 1:
    directory = current_directory
else:
    directory = command[1]

for i in os.listdir(directory):
    contents += i + '\n'
print(contents)

# keeping result to file
with open('temp_save.txt', 'w') as f:
    f.truncate()  # deleting all file data
    f.write(contents)  # put data into temp results file
