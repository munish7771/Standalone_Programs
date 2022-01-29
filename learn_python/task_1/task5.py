# 5. Create a function that takes in parameter from step 4, returns a list containing ip_address of corresponding ids.
file = open("mock_data.csv", "r")
#print(file)
x = []
index = 0
for line in file:
    if index != 0:
        line = line.strip()
        row = line.split(",")
        # print (row)
        if row[4] == "Female":
            def id():
                global x
                x += [row[5]]
                return x
            # print(id)  
            # thisdict = {row[0]:row [1]}
            # print(thisdict)
            # print(row[0] + "->" + row[1])
            # first_names_ids += [row[0]]
            id()
    if index == 50:
        break
    # print (x)
    index += 1
    # print(line)
print(x)