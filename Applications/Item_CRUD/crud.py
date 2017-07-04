item_list = []

def add():
    item_name = input("Enter Item Name : ")
    item_price = input("Enter Item Price : ")
    item_desc = input("Enter Item Description : ")

    item_list.append([item_name,item_price,item_desc])
    # print(item_list)
    # for item in item_list:
    #     print(item)
    read()

def read():
    counter = 0
    for item in item_list:
        counter += 1
        print(counter,item)

def update():
    pass

def delete():
    to_delete = int(input("Enter Item ID : "))
    del(item_list[to_delete-1])

    read()

def search():
    pass

def sorting():
    pass

def save():
    pass

def load():
    pass

def errHandler():
    print("Wrong Choice, Try Again....")

while True:
    print("""
    1. Add Item
    2. Read Item
    3. Update Item
    4. Delete Item
    5. Search Item
    6. Sort Item
    7. Save Item
    8. Load Item
    9. Exit
    """)

    todo = {
        "1" : add,
        "2" : read,
        "3" : update,
        "4" : delete,
        "5" : search,
        "6" : sorting,
        "7" : save,
        "8" : load,
        "9" : quit
    }

    user_choice = input("Enter your choice : ")

    todo.get(user_choice,errHandler)()
