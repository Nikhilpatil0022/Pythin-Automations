fname = input("Enter file name: ")
word = input("Enter word to be searched:")
count = 0

fd = open(fname, 'r')
for line in fd:
    words = line.split()
    for i in words:
        if (i == word):
            count = count + 1
print("Frequency of the word:")
print(count);