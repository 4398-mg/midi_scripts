# midi_scripts
helper scripts for midi files and all their intricacies

## midi_check usage
to use the midi_check script you have to be using python2

Here are the steps to run `midi_check.py`

1. run `pip install python-midi`
2. identify the path of the data directory (the folder that has all your midi files)
3. run `python midi_check.py <data_dir>`
*Note: the output of this program will be 3-4 files that contain paths to their respective midi types (1.txt contains type 1 midi files) . files in error.txt inidicate that there is something wrong with the midi file and these files should be removed using `remove_files.py`*

example usage:
```
python midi_check.py my_data/
```

## remove_files usage
basically this script removes the files that are listed in a specific file

when you run `midi_scripts.py` it will generate 3-4 files, the ones we defintely don't want are the files in `2.txt` and `error.txt` (`2.txt` will commonly be empty). the usage of the command is shown below

```
python remove_files <directory that has the data directory in it> <file_list>
```

the directory that has the data directory will almost always be `./` if you run `midi_check.py` one directory above the data directory.

let me know if you have questions about this

an example usage is shown below
```
python remove_files ./ error.txt
```
