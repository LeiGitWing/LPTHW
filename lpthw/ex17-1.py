from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying form {from_file} to {to_file}")

# we could do these two on one line, how?
in_file = open(from_file)
indata = in_file.read()

# print(f"The input file is {len(indata)} bytes long")

# print(f"Does the output file exist? {exists(to_file)}")
# print("Read, hit REATURN to continue, command-c to abort.")
# input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alrigth, all done.")                                                                                                                                                      
# the purpose of close() is to make sure changes persist
out_file.close()
in_file.close()