# mkdd_rename_release_files
 A script for renaming mkdd track release files to fit with Yoshi2's mkdd .iso patcher found here: https://github.com/RenolY2/mkdd-track-patcher

# Usage 
Put the .py file (and the .bat file, if wanted) in the same directory as the folder with the release files.
Dragging the folder onto the .py file will create a .zip file with the same name as the folder. This .zip file can be used with the editor.
Be sure to use rename.py for course folders, and make_folders.py for character mods.
The .bat files can be used to easily specify the name of the output.zip file.
.ini files in the input folders will be automatically detected.

# Naming files
Make sure that the release files have the same name as the in-game files that they are replacing.

Both .py files require a "bti_images" folder with all various .bti files. They should have their in-game name with a tag at the end to specify a specific language. Images with no tags will be considered the default images, and will be used for languages without with their own file. For example, "Peach_name.bti" will be seen as the default large Peach Beach logo, but "Peach_name_es.bti" will be seen as the large Peach Beach logo in Spanish. If there is no "Peach_name_fr.bti", then "Peach_name.bti" will be used in its place.<br/>
Here are the tags: English: "_en", German: "_de" and "_ge", Spanish: "_sp" and "_es", French: "_fr", Italian: "_it"

If you have a track mod that is replacing Peach Beach, then:<br/>
-Your track .arc file should be named "Peach.arc"<br/>
-Your course name files should be named "coname_peach_beach.bti"<br/>
-Your regular speed course audio should be named "COURSE_CIRCUIT_0.x.32.c4.ast"<br/>
and so on.
If you are making a course, don't forget to make a track.ini file for the patcher.
If there is only one .arc file in the folder, this program will copy that .arc for multiplayer mode. 

If you have a character mod, your release folder can have:<br/>
-driver folders (with the same name as the folders used in root -> MRAM.arc -> driver)<br/>
-kart folders (with the same name as the folders used in root -> MRAM.arc -> kart)<br/>
-selectAnm (with the name selectAnm) <br/>
-item (with the name item) <br/>
-flat images (all within the folder bti_files)

# Command-line Options:

rename.py:<br/>
input: the name of the folder with the release files<br/>
output: the name of the .zip file that is created<br/>

make_folders.py:<br/>
--output: the name of the .zip file that is created<br/>
--author: the name that you want the files to be released with




