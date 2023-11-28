import getpass
import os
import subprocess
import sys


def do_command(command, current_directory, isPipe=False):
    '''

    :param command: command to perform (string)
    :param current_directory: current directory where shell is aimed to
    :param isPipe: is second command in pipe = means that it gets input from file
    :return: current directory of working
    '''
    if command.startswith("hello"):
        # Get the current username
        username = getpass.getuser()
        # print hello msg to the screen
        to_print = f"Hello {username}"
        print(to_print)
        # keeping result to file
        if '>' in command:
            filename = command.split(' > ')[1]
            with open(filename, 'w') as f:
                f.truncate()  # deleting all file data
                f.write(to_print)  # put data into temp results file


    elif command.startswith('cd'):
        new_dir = command.split(" ")
        if len(new_dir) == 1:
            # in that case we stay in the same directory
            print(current_directory)
        else:
            new_dir = new_dir[1]
            current_directory = new_dir
            print(current_directory)

    elif command.startswith('ls'):
        command_to_run = ['ls.bat', command, current_directory]
        subprocess.call(command_to_run)


    elif command.startswith('hexdump'):
        # if in second spot in pipe no file will be given
        if len(command.split(' ')) == 1:
            command = f'hexdump temp_save.txt'
        # ruining the bat file
        command_to_run = ['hexdump.bat', command]
        subprocess.call(command_to_run)

    elif command.startswith('find'):
        # if in second spot in pipe no file will be given
        if len(command.split(' ')) == 2:
            command = command.split(' ')
            command = f'{command[0]} temp_save.txt {command[1]}'
        # ruining the bat file
        command_to_run = ['find.bat', command]
        subprocess.call(command_to_run)

    elif command == 'exit':
        sys.exit()

    return current_directory


if __name__ == '__main__':
    current_directory = os.getcwd()
    print("Current Directory:", current_directory)

    while True:
        command = (input(f'\n{current_directory}>>>')).lower()
        if '|' in command:
            command = command.split(' | ')
            cmd1 = command[0] + ' > temp_save.txt'
            cmd2 = command[1]

            current_directory = do_command(cmd1, current_directory)
            current_directory = do_command(cmd2, current_directory, True)


        else:
            current_directory = do_command(command, current_directory)



