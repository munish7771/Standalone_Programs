# Create a dictionary containing the key = 'id' and value = 'first_name' of all the Females.
file = open("mock_data.csv", "r")
thisdict = {}
# first_names_ids = []
#print(file)
index = 0
for line in file:
    if index != 0:
        row = line.split(",")
        # print (row)
        # print(row[4]) 
        if row[4] == "Female":
            # print(row[4])
            thisdict[row[0]] = row[1] # thisdict[key] = value
            # thisdict = {row[0]:row [1]}
            # print(thisdict)
            # print(row[0] + "->" + row[1])
            # first_names_ids += [row[0]]         
    if index == 50:
        break
    # print (x)
    index += 1
# print(first_names_ids)
print(thisdict)