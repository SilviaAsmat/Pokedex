# importing csv module
import csv
import os
import glob



# csv file name
filename = "pokemon.csv"

# initializing the titles and rows list
fields = []
rows = []

# reading csv file
with open(filename, 'r') as csvfile:
	# creating a csv reader object
	csvreader = csv.reader(csvfile)
	
	# extracting field names through first row
	fields = next(csvreader)

	# extracting each data row one by one
	for row in csvreader:
		rows.append(row)

	# get total number of rows
	print("Total no. of rows: %d"%(csvreader.line_num))

# printing the field names
#print('Field names are:' + ', '.join(field for field in fields))

print("Pokedex\n")
print("Welcome Pokemon Lovers\n")
print("Search for a pokemon\n")
letterChoice = input("<A>Search by pokemon name\n<B>Search by pokemon ID\n(select A or B)\n")
letterChoice.upper()

if(letterChoice == "A"):
    print("Enter the name of the pokemon")
    name = input()
    name.lower().strip()
    dt = filename[:].where(filename['pokemon']==name)
    st = dt[dt['id'].notnull()]    
    idx = dt.index[dt['pokemon'] == name]
    
    for i in st.columns:
      print(i, " : ", st[i][idx[0]])
    
    
elif(letterChoice == "B"):
    print("Enter the ID of the pokemon")
    ID = int(input())
    tt = filename[:].where(filename['id'] == ID)
    idx1 = tt.index[tt['id'] == ID]
    qt = tt[tt['id'].notnull()]
    for i in qt.columns:
        print(i," : ",qt[i][idx1[0]])

