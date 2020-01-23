#! /usr/bin/env python3

import sys
import os
import shutil

PYTHON_MAJORVERSION_REQUIRED = 3
PYTHON_MINORVERSION_REQUIRED = 7
py_maj = sys.version_info[0]
py_min = sys.version_info[1]

def py_report():
    report = str('Python version is ' + str(py_maj) + '.' + str(py_min) +
                 ', Python ' + str(PYTHON_MAJORVERSION_REQUIRED) + '.' +
                 str(PYTHON_MINORVERSION_REQUIRED) + '+ required')
    return report

if py_maj < PYTHON_MAJORVERSION_REQUIRED:
    print(py_report() + ', quitting.')
    sys.exit()
elif py_maj == PYTHON_MAJORVERSION_REQUIRED:
    if py_min < PYTHON_MINORVERSION_REQUIRED:
        print(py_report() + ', quitting.')
        sys.exit()
    elif py_min >= PYTHON_MINORVERSION_REQUIRED:
        print(py_report() + ', continuing.')
else:
    print(py_report() + ', continuing.')

def end1():
    print('End of the script.')
    sys.exit()

###

print('The script file is: ' + __file__)
script_dir = os.path.dirname(os.path.realpath(__file__))
print('The script directory is: ' + script_dir)
print('The script arguments are: ')
print(sys.argv)
if len(sys.argv) == 1:
    print('No arguments were provided, assuming the script folder as the directory for the converted files.')
    converted_files_dir = script_dir
    print('The convereted file root directory is: ' + converted_files_dir)
elif len(sys.argv) == 2:
    print('One argument was provided, checking if the argument is an existing directory.')
    if (os.path.isdir(sys.argv[1])):
        print('The provided argument is an existing directory, using this as the location for the converted files.')
        converted_files_dir = sys.argv[1]
        print('The convereted file root directory is: ' + converted_files_dir)
    else:
        dirfail_text = str('\nThe script fails to run as the path provided as an argument'
                           + 'is not a valid location\n.'
                           + 'Please provide a valid location as a parameter or run'
                           + 'the script without parameters to use the script'
                           + 'directory as the location of the video files.\n'
                           + 'The script will exit when you press any button\n')
        print(dirfail_text)
        input('Press Enter to exit the script.')
        end1()
else:
    paramfail_text = str('\nThe script fails to run as'
                       + 'too many arguments were provided.\n'
                       + 'Please provide one parameter, or run'
                       + 'the script without parameters to use'
                       + 'the script directory as the location'
                       + 'of the video files.\n')
    print(paramfail_text)
    input('Press Enter to exit the script.')
    end1()

preinfo_text = str('\nTag files in ' + os.path.join(converted_files_dir, 'pycos_log', 'log_data', '')
                   + ' without source file counterpart in '
                   + os.path.join(converted_files_dir, '')
                   + ' are about to be removed.')
print(preinfo_text)
valid_answer = False
while not valid_answer:
    answer = input('\nContinue by entering Y.\nYou can cancel the process by entering N.\n(y/n):').lower().strip()
    if answer == 'y' or answer == 'n':
        valid_answer = True
if answer == 'y':
    print('Y was entered, continuing with the script.')
else:
    print('N was entered, exiting the script.')
    end1()
            
###

if not os.path.exists(os.path.join(converted_files_dir, 'pycos_log', 'log_data')):
    nofolder_text = str('\nThere seems to be no folder to clean, exiting.\n'
                       + '(Should be ' + os.path.join(converted_files_dir, 'pycos_log', 'log_data', '') + ' )')
    print(nofolder_text)
    input('\nPress Enter to exit the script.')
    end1()
            
###

def count_files(tagdir):
    number_of_files = len(os.listdir(tagdir))
    return number_of_files

def count_lone_files(tagdir, filedir):
    number_of_lone_files = 0
    for filename in os.listdir(tagdir):
        taggedfilename, txtext = filename.rsplit('.', 1)
        if os.path.exists('{}'.format(os.path.join(filedir, taggedfilename))) == True:
            continue
        else:
            number_of_lone_files = number_of_lone_files + 1
            continue
    return number_of_lone_files

# print('Total files in tag folder: ' + str(count_files(os.path.join(converted_files_dir, 'pycos_log', 'log_data'))))
# print('Total lone tag files: ' + str(count_lone_files(os.path.join(converted_files_dir, 'pycos_log', 'log_data'), converted_files_dir)))

firstcount_text = str('\nBefore cleaning, there are total of '
                     + str(count_files(os.path.join(converted_files_dir, 'pycos_log', 'log_data')))
                     + ' files in '
                     + os.path.join(converted_files_dir, 'pycos_log', 'log_data', '') + '\n'
                     + 'Of these files, '
                     + str(count_lone_files(os.path.join(converted_files_dir, 'pycos_log', 'log_data'), converted_files_dir))
                     + ' have no valid source file available and these lone tag files may be removed.\n'
                     + 'If there are no files left after the removal, the folder '
                     + os.path.join(converted_files_dir, 'pycos_log', '') + ' is also removed.')

print(firstcount_text)
valid_answer = False
while not valid_answer:
    answer = input('\nYou can remove the lone tag files now by entering Y.\nYou can cancel the process by entering N.\n(y/n):').lower().strip()
    if answer == 'y' or answer == 'n':
        valid_answer = True
if answer == 'y':
    print('Y was entered, continuing with the script.')
else:
    print('N was entered, exiting the script.')
    end1()

###

for tagfilename in os.listdir(os.path.join(converted_files_dir, 'pycos_log', 'log_data')):
    taggedfilename, txtext = tagfilename.rsplit('.', 1)
    if os.path.exists('{}'.format(os.path.join(converted_files_dir, taggedfilename))) == True:
        continue
    else:
        os.remove('{}'.format(os.path.join(converted_files_dir, 'pycos_log', 'log_data', tagfilename)))
        continue

if len(os.listdir(os.path.join(converted_files_dir, 'pycos_log', 'log_data'))) < 1:
    shutil.rmtree(os.path.join(converted_files_dir, 'pycos_log'))
    msg_tagfolder = '\nThe log folder pycos_log was left empty, and it was removed.'
else:
    msg_tagfolder = '\nThe log folder still has files and it was not removed.'
        
###

if not os.path.exists(os.path.join(converted_files_dir, 'pycos_log', 'log_data')):
    finalcount_text = str('\nAfter cleaning, there were no files left in '
                          + os.path.join(converted_files_dir, 'pycos_log', 'log_data', '') + '\n'
                          + msg_tagfolder)
else:
    finalcount_text = str('\nAfter cleaning, there are total of '
                          + str(count_files(os.path.join(converted_files_dir, 'pycos_log', 'log_data')))
                          + ' files in the directory '
                          + os.path.join(converted_files_dir, 'pycos_log', 'log_data', '') + '\n'
                          + 'Of these files, ' + str(count_lone_files(os.path.join(converted_files_dir, 'pycos_log', 'log_data'), converted_files_dir))
                          + ' is/are missing the corresponding source file.\n'
                          + msg_tagfolder)
print(finalcount_text)
input('\nPress Enter to exit the script.')
end1()
