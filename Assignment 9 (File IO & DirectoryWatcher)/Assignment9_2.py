name = input("Enter the name of the file: ");

fd =open(name,'r');
print ("Contents are: ")
print(fd.read());
fd.close();

