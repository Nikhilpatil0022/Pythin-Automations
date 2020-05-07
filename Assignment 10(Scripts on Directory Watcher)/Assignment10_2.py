from sys import *
import os


def ExtChanger(path, ext1, ext2):
    flag = os.path.isabs(path);

    if flag == False:
        path = os.path.abspath(path);
    exists = os.path.isdir(path);
    count =0;
    if exists:
        for Folder, SubFolder, Files in os.walk(path):
            # print("Current folder is: ",Folder);
            #for subf in SubFolder:
                #print("Subfolder of ",Folder," is ",subf);
            for Fl in Files:
                #print("File inside ", Folder, " is ", Fl);
                if (Fl.endswith(ext1)):
                    count = count + 1;
                    my_file =path+'/'+Fl;
                    base = os.path.splitext(my_file)[0]
                    os.rename(my_file, base + ext2)
    else:
        print("Invalid path");
    return count;

def main():
    print("Extension changer to given extension");

    if(len(argv) == 2):
        if (argv[1] == "-h" or argv[1] == "-H"):
            print("This Script is used to find all files with entered extension in given directory and rename those files to given new extension");
            exit();
        if (argv[1] == "-u" or argv[1] == "-U"):
            print("Usage command: python ApplicationName Argument(Name of Directory) Extension_tobe_renamed New_Ext");
            exit();
    if (len(argv) != 4):
        print("Invalid No of arguments");
        exit();

    try:
        count = ExtChanger(argv[1], argv[2], argv[3]);
        if(count==0):
            print("No Files found with Extension ",argv[2]);
        else:
            print("Total Files found and renamed are ",count);

    except Exception as E:
        print("Error: " + E);


if __name__ == "__main__":
    main();