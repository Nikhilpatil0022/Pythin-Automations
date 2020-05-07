from sys import *;

fd1 = open(argv[1],'r');
fd2 = open(argv[2],'r');

A = fd1.readlines();
B = fd2.readlines();

if(A == B):
    print("Contents of files are same")
else:
    print("Contents of files are NOT same")
