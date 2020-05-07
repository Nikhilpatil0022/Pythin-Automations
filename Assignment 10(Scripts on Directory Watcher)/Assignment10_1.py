from sys import *
import os


def FilesFinder(path, ext):
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
                if (Fl.endswith(ext)):
                    count = count + 1;
                    print(Fl)
        return count;
    else:
        print("Invalid path");


def main():
    print("Files Finder with given Extension");

    if (argv[1] == "-h" or argv[1] == "-H"):
        print("This Script is used to find all files with entered extension in given directory");
        exit();
    if (argv[1] == "-u" or argv[1] == "-U"):
        print("Usage command: python ApplicationName Argument(Name of Directory) Extension_of_File)");
        exit();
    if (len(argv) != 3):
        print("Invalid No of arguments");
        exit();

    try:
        count = FilesFinder(argv[1], argv[2]);
        if(count==0):
            print("No Files found with Extension ",argv[2]);
        else:
            print("Total Files found are ",count);

    except Exception as E:
        print("Error: " + E);


if __name__ == "__main__":
    main();