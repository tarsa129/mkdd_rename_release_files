import os
import shutil

def rename_file(file):
    print("file is: " + file)
    if "mozi" in file:
        return "track_name.bti"
    elif "coname" in file: 
        return "track_name.bti"
    elif "names" in file:
        return "track_small_logo.bti"
    
    return "track_big_logo.bti"

def process_folder(directory_name):
    num_of_arcs = 0

    os.chdir(directory_name)
    print("current in: " + os.getcwd())
    for file in os.scandir(os.getcwd()):
        if file.is_file():
            if(file.name.endswith(".ast")):
                if "final" in file.name.lower():
                    os.rename(file, "lap_music_fast.ast")
                else:
                    os.rename(file, "lap_music_normal.ast")
            elif(file.name.endswith(".arc")):
                num_of_arcs -= -1
                if file.name.lower().endswith("l.arc"):
                    os.rename(file, "track_mp.arc")
                else:
                    os.rename(file, "track.arc")
            elif(file.name.endswith(".json")):
                os.rename(file, "minimap.json")
            elif(file.name.endswith(".ght")):
                os.rename(file, "staffghost.ght")
            elif(file.name.endswith(".ini")):
                if not file.name.lower() == "trackinfo.ini":
                    os.rename(file, "trackinfo.ini")
        elif file.is_dir():
            print("Images folder: " + file.name)
            os.rename(file, "course_images")
            #folder = file.name
            os.chdir("./" + "course_images")
            
            languages = {"en" : "English", "ge" : "German", "sp":  "Spanish", "it":  "Italian", "fr" : "French", "de": "German", "es" : "Spanish", "jp" : "Japanese"}
            shortlang = ["English", "German", "Spanish", "Italian", "French", "Japanese"]
            
            for language in shortlang:
                if not os.path.isdir(language):
                    os.mkdir(language)
            
            bti_files = os.listdir()
            for bti_file in bti_files:
                bti_file_l = bti_file.lower()
                if bti_file_l.endswith(".bti"):
                    #print(bti_file_l)
                    if "cop" in bti_file_l or "snap" in bti_file_l:
                        os.rename(bti_file, "track_image.bti")
                        for language in shortlang:
                            shutil.copy("track_image.bti", language)
                        os.remove("track_image.bti")
                    else:
                        new_file_name = rename_file(bti_file_l)
                        
                        for abbr in languages.keys():
                            if bti_file_l.endswith("_" + abbr + ".bti"):
                                print(bti_file_l + " to " + new_file_name + " into " + languages[abbr])
                                shutil.copyfile(bti_file, new_file_name);
                                shutil.move(new_file_name, languages[abbr]);
                                os.remove(bti_file);
                                
            leftover_files = [f for f in os.listdir() if os.path.isfile(f)]
            
            for remaining_file in leftover_files:
                new_file_name = rename_file(remaining_file)
                for language in shortlang:
                    if not os.path.exists(language + "/" + new_file_name):
                        shutil.copyfile(remaining_file, language + "/" + new_file_name);

                    
                os.remove(remaining_file);
                                
            os.chdir('..')              


    if num_of_arcs == 1:
        shutil.copyfile("track.arc", "track_mp.arc")
    
if __name__ == "__main__":
    
    import argparse
    parser = argparse.ArgumentParser()

    parser.add_argument("input",
                        help="Filepath to .gci file to be converted into .ght")
    parser.add_argument("output", default=None, nargs = '?',
                        help="Filepath to .zip file with course files")     
                        
    args = parser.parse_args()
    
    print("Will change files in: " + args.input + "_copy")
    
    shutil.copytree(args.input, args.input + "_copy")
    
    #print(os.exists(args.input + "_copy"))
    
    if args.output is None:
        output = args.input
        print("Will write to: " + output + ".zip")
    else:
        output = args.output
        
    process_folder(args.input + "_copy")
     
    os.chdir("..")
    print(os.getcwd())
    
    shutil.make_archive(output, 'zip', args.input + "_copy")
    shutil.rmtree(args.input + "_copy")
        
        
    
