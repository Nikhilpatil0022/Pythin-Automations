from sys import *;

fd = open(argv[1],'r');
fd1 = open("Demo.txt",'w');

fd1.write(fd.read());

print("new file created as Demo.txt in the same directory with contents of ",argv[1]);
fd1.close();
fd.close();