item_list = []
items = {}

def add():
    item_name = input("Enter Item Name : ")
    item_price = input("Enter Item Price : ")
    item_desc = input("Enter Item Description : ")

    items["Name"] = item_name
    items["Price"] = item_price
    items["Description"] = item_desc

    # item_list.append([item_name,item_price,item_desc])
    # print(item_list)
    # for item in item_list:
    #     print(item)

    item_list.append(items.copy())

    read()

def read():
    counter = 0
    for item in item_list:
        counter += 1
        print(counter,item)

def update():
    to_update = int(input("Enter Product id to update : "))
    print("You want to update ",item_list[to_update-1])
    update_choice = input("What do you want to update?? Name or Price : ")
    if update_choice == "Name":
        updated_Name = input("Enter Updated Name : ")
        new_data = item_list[to_update-1]
        new_data["Name"] = updated_Name
        # print(new_data)
        print("Updated List")
        read()
    elif update_choice == "Price":
        updated_Price = input("Enter Updated Price : ")
        new_data = item_list[to_update-1]
        new_data["Price"] = updated_Price
        # print(new_data)
        print("Updated List")
        read()
    else:
        print("Wrong Choice...")

def delete():
    to_delete = int(input("Enter Item ID : "))
    del(item_list[to_delete-1])

    read()

def search():
    pass

def sorting():
    newlist = sorted(item_list, key=lambda k: k['Name'])
    print("Sorted List")
    for n in newlist:
        print(n)

def save():
    file = open("Item_List.txt",'a')
    print("Writing Data....")
    # file.write(str(item_list))
    for data in item_list:
        file.write(str(data)+"\n")
    print("Successfully written...")
    # print(str(item_list))
    file.close()

def load():
    file = open("Item_List.txt",'r')
    data = file.readlines()
    for i in data:
        item_list.append(i)
    #item_list.append(file.readlines())
    read()
    file.close()

def errHandler():
    print("Wrong Choice, Try Again....")