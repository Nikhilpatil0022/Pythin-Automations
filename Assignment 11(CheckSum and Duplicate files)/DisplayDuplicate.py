from sys import *
import os
import hashlib

def hashfile(path,blocksize = 1024):
    afile = open(path,'rb');
    hasher = hashlib.md5();                                                 # returns a hash-object in hasher
    buf = afile.read(blocksize)                                             # blocksize= total no of characters chosen at a time
    # print("My buf is ",buf);
    while(len(buf))>0:
        # print("buf for each cycle: ",buf);
        # print("hasher for each cycle: ", hasher);
        hasher.update(buf);                                                 # combines each hash-objects
        buf = afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()


def PrintDuplicate(dict1,mypath):
    results = list(filter(lambda x: len(x)>1,dict1.values()));
    mypath = mypath + "\log.txt";
    F = open(mypath, "w");
    if len(results)>0:
        print("Duplicate Found: ")
        print("Following Files are identical: ")
        F.write("Duplicate files are listed below:\n");
        icnt=0;
        for result in results:
            for subresult in result:
                icnt+=1;
                if icnt>=2:
                    print("\t\t",subresult)
                    F.write(subresult+"\n");
    else:
        F.write("No duplicate files found");
        print("No duplicate files found");
    F.close();


def FindDuplicate(path):
    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)
    exists = os.path.isdir(path)
    dups={};
    if exists:
        mypath = path;
        for dirName,subdirs,fileList in os.walk(path):
            # print("Current Folder is: "+dirName)
            for filen in fileList:
                path=os.path.join(dirName,filen)
                file_hash = hashfile(path)
                if file_hash in dups:
                    dups[file_hash].append(path);
                else:
                    dups[file_hash]=[path];
        PrintDuplicate(dups,mypath);

    else:
        print("Invalid Path")

def main():
    print("Display Duplicate files in given directory and save the names in log.txt")
    if(len(argv)!=2):
        print ("Error: Invalid no of arguments")
        exit()
    if(argv[1]=='-h') or (argv[1]=='-H'):
        print("This script is used to traverse specific directory and display checksum of files")
        exit();
    if (argv[1] == '-u') or (argv[1] == '-U'):
        print("Python ApplicationName AbsolutePathOfDirectory")
        exit();
    try:
        FindDuplicate(argv[1])

    except valuError:
        print("Error: Invalid datatype of Input")
    except Exception as E:
        print("Error: Invalid input ",E)


if __name__ == "__main__":
    main();