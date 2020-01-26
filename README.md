# pycos_ltfc
## pycos Lone Tag File Cleaner
This is a small maintenance script to be used with pycos. Pycos converts video files to another format and location. The script keeps "log" of converted files by creating a folder for tag files, one tag file (in sourceroot/pycos_log/log_data/ ) for each converted file.
It can happen, that the user decides to move or delete some of the video files in the source folder. This would leave the lone tag files in the tag folder.
As the user should not neet to manually keep track of the converted files, and especially not their tag files, pycos has an option to check for these lone files and delete them when necessary.
This script does the same thing, without running the whole pycos. I.e. this script checks that every file in the log_data -folder has a corresponding file available. If not, it deletes the lone tag files.
## Requirements
* Python 3.7 or higher (might work with 3.5+, not tested)
* tkinter installed (only GUI version needs this). This is included in the standard version of Python 3.7 and higher, but might be missing, if OS was installed with minimal options (such as Ubuntu 18.04 LTS)
* Tested in both Windows 10 and GNU/Linux environment (Debian), should work.
## Usage
```
python pycos_LTFC_NOUGUI.py [optional: source file root folder]
```
If you have Python 2 as default, you might be more lucky using:
```
python3 path/to/pycos_LTFC_NOGUI.py [optional: source file root folder]
```
You can place the script in the same folder as the video files, especially if the files reside in a shared folder and you need to run it using different access methods (e.g. SSH, virtual desktop, direct desktop). The more "program-like" approach is to run the script using the source video path as the parameter (Note: the parameter is NOT the tag file folder!).
The NOGUI-version runs in a shell, but I also created a GUI (using Tk), mostly as a rehearsal for creating simple GUI's. Both versions give information about the found tag files (how many?) and ask for user confirmation before doing anything.
