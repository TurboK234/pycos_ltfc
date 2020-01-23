#! /usr/bin/env python3

from tkinter import *
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
        infowin = Tk()
        infowin.geometry('600x400')
        infowin.title('Directory error')
        dirfail_text = str('\nThe script fails to run as\n'
                           + 'the path provided as an argument\n'
                           + 'is not a valid location.\n\n'
                           + 'Please provide a valid location\n'
                           + 'as a parameter or run the script\n'
                           + 'without parameters to use the script\n'
                           + 'directory as the location of the\n'
                           + 'video files.\n\n'
                           + 'The script will exit when you click OK\n')
        ButtonPressed = StringVar()
        ButtonPressed.set('None')

        def f_okbtn():
            ButtonPressed.set('OK')
            infowin.destroy()
            return

        infowin_textlabel = Label(master=infowin, text=dirfail_text, font=('Arial', 10))
        infowin_textlabel.pack(side=TOP)
        ok_btn = Button(master=infowin, text='OK', command=lambda: f_okbtn(), font=('Arial', 14))
        ok_btn.focus_set()
        ok_btn.pack(side=TOP)
        infowin.mainloop()

        if ButtonPressed.get() == 'OK':
            ButtonPressed.set('None')
            end1()
        else:
            ButtonPressed.set('None')
            end1()
else:
    infowin = Tk()
    infowin.geometry('600x400')
    infowin.title('Parameter error')
    paramfail_text = str('\nThe script fails to run as\n'
                       + 'too many arguments were provided.\n\n'
                       + 'Please provide one parameter, or run\n'
                       + 'the script without parameters to use\n'
                       + 'the script directory as the location\n'
                       + 'of the video files.\n\n'
                       + 'The script will exit when you click OK\n')
    ButtonPressed = StringVar()
    ButtonPressed.set('None')

    def f_okbtn():
        ButtonPressed.set('OK')
        infowin.destroy()
        return

    infowin_textlabel = Label(master=infowin, text=paramfail_text, font=('Arial', 10))
    infowin_textlabel.pack(side=TOP)
    ok_btn = Button(master=infowin, text='OK', command=lambda: f_okbtn(), font=('Arial', 14))
    ok_btn.focus_set()
    ok_btn.pack(side=TOP)
    infowin.mainloop()

    if ButtonPressed.get() == 'OK':
        ButtonPressed.set('None')
        end1()
    else:
        ButtonPressed.set('None')
        end1()

###
    
infowin = Tk()
infowin.geometry('600x400')
infowin.title('Checking')
infowin_text = str('\nTag files in\n'
                   + os.path.join(converted_files_dir, 'pycos_log', 'log_data', '') + '\n'
                   + 'without source file counterpart in\n'
                   + os.path.join(converted_files_dir, '') + '\n'
                   + 'are about to be removed.\n\n'
                   + 'The process will start\n'
                   + 'automatically in 10 seconds.\n\n'
                   + 'Continue by selecting OK.\n\n'
                   + 'You can cancel the process by selecting Cancel.\n')
ButtonPressed = StringVar()
ButtonPressed.set('None')

def f_okbtn():
    ButtonPressed.set('OK')
    infowin.after_cancel(timeout)
    infowin.destroy()
    return

def f_cancelbtn():
    ButtonPressed.set('Cancel')
    infowin.after_cancel(timeout)
    infowin.destroy()
    return

infowin_textlabel = Label(master=infowin, text=infowin_text, font=('Arial', 10))
infowin_textlabel.pack(side=TOP)
ok_btn = Button(master=infowin, text='OK', command=lambda: f_okbtn(), font=('Arial', 14))
ok_btn.focus_set()
ok_btn.pack(side=LEFT)
cancel_btn = Button(master=infowin, text='Cancel', command=lambda: f_cancelbtn(), font=('Arial', 14))
cancel_btn.pack(side=RIGHT)
timeout = infowin.after(10000, f_okbtn)
infowin.mainloop()

if ButtonPressed.get() == 'OK':
    ButtonPressed.set('None')
elif ButtonPressed.get() == 'Cancel':
    ButtonPressed.set('None')
    end1()
else:
    ButtonPressed.set('None')
    end1()

###

if not os.path.exists(os.path.join(converted_files_dir, 'pycos_log', 'log_data')):
    infowin = Tk()
    infowin.geometry('600x400')
    infowin.title('No tag folder found')
    infowin_text = str('\nThere seems to be no folder\n'
                       + 'to clean, exiting.\n\n'
                       + '(Should be\n'
                       + os.path.join(converted_files_dir, 'pycos_log', 'log_data', '') + ' )\n\n'
                       + 'Click OK to exit.\n\n')

    ButtonPressed = StringVar()
    ButtonPressed.set('None')

    def f_okbtn():
        ButtonPressed.set('OK')
        infowin.destroy()
        return

    infowin_textlabel = Label(master=infowin, text=infowin_text, font=('Arial', 10))
    infowin_textlabel.pack(side=TOP)
    ok_btn = Button(master=infowin, text='OK', command=lambda: f_okbtn(), font=('Arial', 14))
    ok_btn.focus_set()
    ok_btn.pack(side=TOP)
    infowin.mainloop()

    if ButtonPressed.get() == 'OK':
        ButtonPressed.set('None')
        end1()
    else:
        ButtonPressed.set('None')
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

print('Total files in tag folder: ' + str(count_files(os.path.join(converted_files_dir, 'pycos_log', 'log_data'))))
print('Total lone tag files: ' + str(count_lone_files(os.path.join(converted_files_dir, 'pycos_log', 'log_data'), converted_files_dir)))

infowin = Tk()
infowin.geometry('600x400')
infowin.title('Count before cleaning')
infowin_text = str('\nBefore cleaning, there are\n'
                   + 'total of ' + str(count_files(os.path.join(converted_files_dir, 'pycos_log', 'log_data'))) + ' files in the directory\n'
                   + os.path.join(converted_files_dir, 'pycos_log', 'log_data', '') + '\n\n'
                   + 'Of these files, ' + str(count_lone_files(os.path.join(converted_files_dir, 'pycos_log', 'log_data'), converted_files_dir)) + ' have no valid\n'
                   + 'source file available and these lone tag files may be removed.\n\n'
                   + 'If there are no files left after the removal, the folder\n'
                   + os.path.join(converted_files_dir, 'pycos_log', '') + ' is also removed\n\n'
                   + 'You can remove the lone tag files now by selecting OK.\n\n'
                   + 'You can cancel the process by selecting Cancel.\n')

ButtonPressed = StringVar()
ButtonPressed.set('None')

def f_okbtn():
    ButtonPressed.set('OK')
    infowin.destroy()
    return

def f_cancelbtn():
    ButtonPressed.set('Cancel')
    infowin.destroy()
    return

infowin_textlabel = Label(master=infowin, text=infowin_text, font=('Arial', 10))
infowin_textlabel.pack(side=TOP)
ok_btn = Button(master=infowin, text='OK', command=lambda: f_okbtn(), font=('Arial', 14))
ok_btn.focus_set()
ok_btn.pack(side=LEFT)
cancel_btn = Button(master=infowin, text='Cancel', command=lambda: f_cancelbtn(), font=('Arial', 14))
cancel_btn.pack(side=RIGHT)
infowin.mainloop()

if ButtonPressed.get() == 'OK':
    ButtonPressed.set('None')
elif ButtonPressed.get() == 'Cancel':
    ButtonPressed.set('None')
    end1()
else:
    ButtonPressed.set('None')
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
    msg_tagfolder = 'The log folder pycos_log was left empty, and it was removed.'
    print(msg_tagfolder)
else:
    msg_tagfolder = 'The log folder still has files and it was not removed.'
    print(msg_tagfolder)
        
###

infowin = Tk()
infowin.geometry('600x400')
infowin.title('Final count')
if not os.path.exists(os.path.join(converted_files_dir, 'pycos_log', 'log_data')):
    infowin_text = str('\nAfter cleaning, there were no files left in\n'
                       + os.path.join(converted_files_dir, 'pycos_log', 'log_data', '') + '\n\n'
                       + msg_tagfolder + '\n\n')
else:
    infowin_text = str('\nAfter cleaning, there are\n'
                       + 'total of ' + str(count_files(os.path.join(converted_files_dir, 'pycos_log', 'log_data'))) + ' files in the directory\n'
                       + os.path.join(converted_files_dir, 'pycos_log', 'log_data', '') + '\n\n'
                       + 'Of these files, ' + str(count_lone_files(os.path.join(converted_files_dir, 'pycos_log', 'log_data'), converted_files_dir)) + ' is/are missing\n'
                       + 'the corresponding source file.\n\n'
                       + msg_tagfolder + '\n\n')

ButtonPressed = StringVar()
ButtonPressed.set('None')

def f_okbtn():
    ButtonPressed.set('OK')
    infowin.destroy()
    return

infowin_textlabel = Label(master=infowin, text=infowin_text, font=('Arial', 10))
infowin_textlabel.pack(side=TOP)
ok_btn = Button(master=infowin, text='OK', command=lambda: f_okbtn(), font=('Arial', 14))
ok_btn.focus_set()
ok_btn.pack(side=TOP)
infowin.mainloop()

if ButtonPressed.get() == 'OK':
    ButtonPressed.set('None')
    end1()
else:
    ButtonPressed.set('None')
    end1()
