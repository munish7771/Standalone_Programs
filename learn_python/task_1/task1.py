#Create a list of ids whose corresponding first_name starts with either 'A' or 'S'
file = open("mock_data.csv", "r")
first_names_ids = []
#print(file)
index = 0
for line in file:
    if index != 0:
        row = line.split(",")
        # if row[1][0] in ['A','S']:
        if row[1][0] == 'A' or row[1][0] == 'S':
            # print(row[0] + "->" + row[1])
            first_names_ids += [row[0]]
            # printing result 
    if index == 50:
        break
    # print (x)
    index += 1
print(first_names_ids)