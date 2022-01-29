# Create a tuple containing all the ids having numbers [7,8,9] in ip_address
import ipaddress


file = open("mock_data.csv", "r")
ip = ()
#print(file)
index = 0
for line in file:
    if index != 0:
        row = line.split(",")
        if '7' in row[5] or '8' in row[5] or '9' in row[5]:
            ip += (row[0],)
        # if row[1][0] in ['A','S']:
        # if row[1][0] == 'A' or row[1][0] == 'S':
        #     print(row[0] + "->" + row[1])
        #     first_names_ids += [row[0]]
            # printing result 
    if index == 50:
        break
    # print (x)
    index += 1
print(ip)