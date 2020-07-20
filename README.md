# mkdd_rename_release_files
 A script for renaming mkdd track release files to fit with Yoshi2's mkdd .iso patcher 

# Usage 
Put the .py file (and the .bat file, if wanted) in the same directory as the folder with the release files.
Dragging the folder onto the .py file will create a .zip file with the same name as the folder. This .zip file can be used with the editor.
Be sure to use rename.py for course folders, and make_folders.py for character mods.
The .bat files can be used to easily specify the name of the output.zip file.

# Naming files
Make sure that the release files have the same name as the in-game files that they are replacing.
For example, if your track is replacing Peach Beach, then:<br/>
-Your track .arc file should be named "Peach.arc"<br/>
-Your course name files should be named "coname_peach_beach.bti"<br/>
-Your regular speed course audio should be named "COURSE_CIRCUIT_0.x.32.c4.ast"<br/>
and so on.
If you are making a course, don't forget to make a track.ini file for the patcher

# Command-line Options:

rename.py:<br/>
input: the name of the folder with the release files<br/>
output: the name of the .zip file that is created<br/>

make_folders.py:<br/>
input: the name of the folder with the release files<br/>
--output: the name of the .zip file that is created<br/>
--ini_file: the name of a .ini file that is necessary for the editor. if not specified, a generic .ini file will be automatically created<br/>



