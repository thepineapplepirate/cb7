

name1 = input("Enter the file to be read from: ")
name2 = input("Enter the file to be appended to: ")
file = open(name1, "r")
data2 = file.read()
file.close()
fout = open(name2, "a")
fout.write(data2)
fout.close()
