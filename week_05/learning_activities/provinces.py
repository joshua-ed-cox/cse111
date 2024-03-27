provinces_list = []


with open("learning_activities/provinces.txt", "rt") as provinces_file:
    
    # Go through each line in the provinces file and append it to our list
    # Each line in the file has one province 
    for province in provinces_file:
        provinces_list.append(province.strip())


print(provinces_list)
