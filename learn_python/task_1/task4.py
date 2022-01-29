# 4. Create a set out of all the keys of dictionary created in step 2
file = open("mock_data.csv", "r")
# first_names_ids = []
#print(file)
id = []
index = 0
for line in file:
    if index != 0:
        row = line.split(",")
        # print (row)
        # print(row[4]) 
        if row[4] == "Female":
            # print(row[0])
            id += [row[0]]
            # print(id)
            s = set(id)
            # thisdict = {row[0]:row [1]}
            # print(thisdict)
            # print(row[0] + "->" + row[1])
            # first_names_ids += [row[0]]         
    if index == 50:
        break
    # print (x)
    index += 1
# print(first_names_ids)
print(s)