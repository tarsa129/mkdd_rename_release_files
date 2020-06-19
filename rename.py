import os
import shutil

def rename_file(file):
    if "coname" in file:
        return "track_name.bti"
    if "names" in file:
        return "track_small_logo.bti"
    return "track_big_logo.bti"
    

num_of_arcs = 0

#deal with individual files

#base_path = os.getcwd()


for file in os.scandir(os.getcwd()):
    if file.is_file():
        if(file.name.endswith(".ast")):
            if "final" in file.name.lower():
                os.rename(file, "lap_music_fast.ast")
            else:
                os.rename(file, "lap_music_normal.ast")
        elif(file.name.endswith(".arc")):
            num_of_arcs -= -1
            if "l" in file.name.lower():
                os.rename(file, "track_mp.arc")
            else:
                os.rename(file, "track.arc")
        elif(file.name.endswith(".json")):
            os.rename(file, "minimap.json")
        elif(file.name.endswith(".ght")):
            os.rename(file, "staffghost.ght")
    elif file.is_dir():
        os.rename(file, "course_images")
        folder = file.name
        os.chdir("./" + folder)
        
        languages = {"en" : "English", "ge" : "German", "sp":  "Spanish", "it":  "Italian", "fr" : "French"}
        
        for language in languages.values():
            os.mkdir(language)
        
        bti_files = os.listdir()
        for bti_file in bti_files:
            bti_file_l = bti_file.lower()
            if bti_file_l.endswith(".bti"):
                if "cop" in bti_file_l:
                    os.rename(bti_file, "track_image.bti")
                    for language in languages.values():
                        shutil.copy("track_image.bti", language)
                    os.remove("track_image.bti")
                else:
                    new_file_name = rename_file(bti_file_l)
                    for abbr in languages.keys():
                        if abbr in bti_file_l:
                            shutil.copyfile(bti_file, new_file_name);
                            shutil.move(new_file_name, languages[abbr]);
                            os.remove(bti_file);
                            
        leftover_files = [f for f in os.listdir() if os.path.isfile(f)]
        
        for remaining_file in leftover_files:
            new_file_name = rename_file(remaining_file)
            shutil.copyfile(remaining_file, new_file_name);
            shutil.move(new_file_name, "English");
            os.remove(remaining_file);
                            
        os.chdir("..")              


if num_of_arcs == 1:
    shutil.copyfile("track.arc", "track_mp.arc")
    

