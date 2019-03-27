import midi
import os
import sys

z_out = open('0.txt', 'w')
o_out = open('1.txt', 'w')
t_out = open('2.txt', 'w')
error_out = open('error.txt', 'w')

write_dict = {
        '0': z_out.write,
        '1': o_out.write,
        '2': t_out.write,
        'error': error_out.write
    }

try:
    print('data dir: %s' % sys.argv[1])
except IndexError:
    print('[!] no directory passed')
    print('valid usage: python midi_check <data_dir>')
    sys.exit()

for root, subdir, files in os.walk(sys.argv[1]):
    for f in files:
        path = root.split(os.sep)
        file_path = os.path.join(root, f)
        if(file_path.endswith('.mid')):
            try:
                m_type = midi.read_midifile(file_path).format
            except (Warning, TypeError, AssertionError):
                write_dict['error'](file_path + '\n')
                continue
            #print((file_path, m_type))
            write_dict[str(m_type)](file_path + '\n')

