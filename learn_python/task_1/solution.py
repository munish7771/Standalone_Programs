try:
    file = open("mock_data.csv", "r")
except:
    print ("File not found")
ids = []
thisdict = {}
ip = ()
i = []
x = []
index = 0
for line in file:
    if index != 0:
        line = line.strip()
        row = line.split(",")
        if row[1][0] == 'A' or row[1][0] == 'S': #step 1
            ids += [row[0]]           
        if row[4] == "Female": #step 2
           thisdict[row[0]] = row[1] # thisdict[key] = value # printing result
           i += [row[0]] #step 4
           s = set(i)
           def id(): #step 5
               global x
               x += [row[5]]
               return x
           id() # printing result
        if '7' in row[5] or '8' in row[5] or '9' in row[5]: #step 3
            ip += (row[0],) # printing result
    index += 1
print("List of ids whose corresponding first_name starts with either 'A' or 'S' are ->\r\n",  ids) #Create a list of ids whose corresponding first_name starts with either 'A' or 'S'
print("Dictionary containing the key = 'id' and value = 'first_name' of all the Females ->\r\n",  thisdict) # Create a dictionary containing the key = 'id' and value = 'first_name' of all the Females.
print("Tuple containing all the ids having numbers [7,8,9] in ip_address ->\r\n",  ip) # Create a tuple containing all the ids having numbers [7,8,9] in ip_address
print("Set of all the keys of dictionary created in step 2 ->\r\n",  s) # 4. Create a set out of all the keys of dictionary created in step 2
print("List containing ip_address of corresponding ids when called through a function ->\r\n",  x) # 5.Create a function that takes in parameter from step 4, returns a list containing ip_address of corresponding ids.
