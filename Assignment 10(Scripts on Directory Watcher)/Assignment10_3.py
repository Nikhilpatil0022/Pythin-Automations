from sys import *
import os
import shutil


def CopyFiles(dir1, dir2):
    flag = os.path.isabs(dir1);

    if flag == False:
        dir1 = os.path.abspath(dir1);
    exists = os.path.isdir(dir1);


    flag = os.path.isabs(dir2);

    if flag == False:
        dir2 = os.path.abspath(dir2);
    if(os.path.isdir(dir2)):
        print("Directory already exists hence cannot copy")
        print (dir2);
        return 0;
    else:
        os.makedirs(dir2);

    if exists:
        for Folder, SubFolder, Files in os.walk(dir1):
            # print("Current folder is: ",Folder);
            #for subf in SubFolder:
                #print("Subfolder of ",Folder," is ",subf);
            for Fl in Files:
                #print("File inside ", Folder, " is ", Fl);
                Fl=dir1+'/'+Fl;
                shutil.copy(Fl,dir2,follow_symlinks=True);


    else:
        print("Invalid path");
    return 1;

def main():
    print("File copier to given directory");

    if(len(argv) == 2):
        if (argv[1] == "-h" or argv[1] == "-H"):
            print("This Script is used to find all files with entered extension in given directory and rename those files to given new extension");
            exit();
        if (argv[1] == "-u" or argv[1] == "-U"):
            print("Usage command: python ApplicationName Argument(Name of Directory) Extension_tobe_renamed New_Ext");
            exit();
    if (len(argv) != 3):
        print("Invalid No of arguments");
        exit();

    try:
        count = CopyFiles(argv[1], argv[2]);
        if(count==0):
            print("New folder cannot be created");
        else:
            print("Files are successfully copied");

    except Exception as E:
        print(E);




if __name__ == "__main__":
    main();