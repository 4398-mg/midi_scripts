import os
import sys

try:
    data_dir = sys.argv[1]
    file_list = open(sys.argv[2], 'r')
except IndexError:
    print('[!] invalid usage')
    print('valid usage: python remove_files.py <working_dir> <file_list>')
    print('example usage: python remove_files.py ./ errors.txt')
    sys.exit(0)

for line in file_list.readlines():
    os.remove(os.path.join(data_dir, line.strip()))
file_list.close()
