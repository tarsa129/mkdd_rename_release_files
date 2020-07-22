import os 
import shutil

if __name__ == "__main__":
    
    original_directory = os.getcwd()
    
    import argparse
    parser = argparse.ArgumentParser()

    parser.add_argument("input",
                        help= "Base folder containing mod files")
    parser.add_argument("--output", default = None,
                        help = "Outputted .zip file with the mods")
    parser.add_argument("--author", default = None, 
                        help="Author of the mod")
    parser.add_argument("--ini_file", default = None,
                        help="Path to the .ini file to be used")
                        
    args = parser.parse_args()
    
    if args.output is None:
        output = args.input
    else:
        output = args.output
        if output.endswith(".zip"):
            output = output[:-4]
        
    
    folder = args.input + " patch" #aka the finished product
    orig_folder = args.input
    
    #shutil.copytree(orig_folder, folder)
    
    #make the base folder
    
    os.mkdir(folder)
    
    if args.ini_file is None:
        f = open("modinfo.ini", "w+")
        f.write("[Config]\n")
        f.write("author = Unknown\n")
        f.write("modname = Character Mod\n")
        f.write("description = Character Mod\n")
        f.close()
        
        shutil.move("modinfo.ini", folder)
    else:
        shutil.copy(args.ini_file, folder)
    
    os.chdir(folder)
    
    if not args.ini_file is None:
        for file in os.scandir(os.getcwd()):
           os.rename(file, "modinfo.ini")
    
    os.makedirs("files/MRAM.arc/mram/driver")
    os.makedirs("files/MRAM.arc/mram/kart")
    os.makedirs("files/race2d.arc/mram_race2d/timg")
    os.makedirs("files/SceneData/English/menu.arc/menu/timg")
    
    
    languages = {"en" : "English", "ge" : "German", "sp":  "Spanish", "it":  "Italian", "fr" : "French", "de": "German", "es" : "Spanish", "jp" : "Japanese"}
    shortlang = ["German", "Spanish", "Italian", "French", "Japanese"]
            
    for language in shortlang:
        shutil.copytree("files/SceneData/English", "files/SceneData/" + language);
    
    shortlang.insert(0, "English")
    
    #move in the mods
    
    for file in os.scandir(orig_folder):
        if file.name == "bti_files": #parse the .bti images
        
            bti_folder = orig_folder + "/bti_files/"
            
            for bti_file in os.listdir(orig_folder + "/bti_files"): #get all the name of the .bti files
                
                bti_file_l = bti_file.lower(); #make the file name lowercase
              
                if "chaname_" in bti_file_l:
                    found_language = False
                    for abbr in languages.keys(): #if a language, sort 
                        annoying_path = "files/SceneData/" + languages.get(abbr) + "/menu.arc/menu/timg/"
                        new_file_name = bti_file_l.replace("_" + abbr, "")
                        if bti_file_l.endswith("_" + abbr + ".bti"):                     
                            print(bti_file_l + " to become " + new_file_name)
                            shutil.copyfile(bti_folder + bti_file, annoying_path + new_file_name)
                            found_language = True
                    print(bti_file + ": " + str(found_language))
                    if not found_language: #use default .bti
                        print("a default .bti is " + bti_file)
                        for language in shortlang:
                            annoying_path = "files/SceneData/" + language + "/menu.arc/menu/timg/"
                            try:
                                shutil.copyfile(bti_folder + bti_file, annoying_path + bti_file_l)
                            except:
                                print("already exists")
                     
                else: 
                    shutil.copyfile(bti_folder + bti_file, "files/race2d.arc/mram_race2d/timg/" + bti_file_l)
        elif file.name.endswith("_all"):
            shutil.copytree(orig_folder  + "/"+ file.name, "files/MRAM.arc/mram/kart/" + file.name)
        else:
            shutil.copytree(orig_folder + "/"+  file.name, "files/MRAM.arc/mram/driver/" + file.name)
    
    os.chdir("..")
    shutil.make_archive(output, "zip", folder)
    shutil.rmtree(folder)
    
    
    
  
    
 