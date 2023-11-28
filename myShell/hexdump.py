import sys


[_, command] = sys.argv
where_to_save = None

if '>' in command:
    command = command.split(' > ')
    where_to_save = command[1]
    command = command[0]


file_path = command.split(' ')[1]

try:
    with open(file_path, 'rb') as file:
        data = file.read()
        hex_data = ' '.join(['{:02X}'.format(byte) for byte in data])
        print(hex_data)
    # keeping result to file
    if where_to_save is not None:
        with open(where_to_save, 'w') as f:
            f.truncate()  # deleting all file data
            f.write(hex_data)  # put data into temp results file

except FileNotFoundError:
    print(f"Error: File not found at path {file_path}")
except Exception as e:
    print(f"Error: {e}")
