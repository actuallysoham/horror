# importing os module 
import os
import re
import csv

#s = "abc123AUG|GAC|UGAasdfg789"
pattern = 'Stoker_Bram_([0-9]*)-(.*?)\"'
author = "Bram Stoker"
lovecraft_table = []

# Get the list of all files and directories
# in the root directory
path = "canons/stoker"
dir_list = os.listdir(path)
for file in dir_list:
	title = file.strip(".txt")
	file_reader = open(path+"/"+file,"r")
	print(path+"/"+file)
	text = file_reader.read()
	row = [text, title, author]
	print(row)
	lovecraft_table.append(row)

print(len(lovecraft_table))
print(len(lovecraft_table[0]))
		
header = ['text', 'title', 'author']

with open('canons/stoker.csv', 'wb') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write the data
    writer.writerows(lovecraft_table)