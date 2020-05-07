from sys import *
import os


def DirectoryWatcher(path, name):
    flag = os.path.isabs(path);

    if flag == False:
        path = os.path.abspath(path);
    exists = os.path.isdir(path);
    if exists:
        for Folder, SubFolder, Files in os.walk(path):
            # print("Current folder is: ",Folder);
            for subf in SubFolder:
                if (subf == name):
                    print(name, " found inside the folder ", Folder)
                    return 1;
                else :
                    return 0;
            for Fl in Files:
                if (Fl == name):
                    print(name," found inside the folder ",Folder)
                    #print("File inside ", Folder, " is ", Fl);
                    return 1;
                else:
                    return 0;
    else:
        print("Invalid path");


def main():
    print("Directory watcher");

    if (argv[1] == "-h" or argv[1] == "-H"):
        print("This Script is used to traverse a specific directory");
        exit();
    if (argv[1] == "-u" or argv[1] == "-U"):
        print("Usage command: python ApplicationName Argument(Name of Directory) File_Name(to be searched)");
        exit();
    if (len(argv) != 3):
        print("Invalid No of arguments");
        exit();

    try:
        status = DirectoryWatcher(argv[1], argv[2]);
        if status != 1:
            print(argv[2]," is not present in the Directory ",argv[1]);

    except Exception as E:
        print("Error: " + E);


if __name__ == "__main__":
    main();