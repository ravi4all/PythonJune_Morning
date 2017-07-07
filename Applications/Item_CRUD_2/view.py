import model

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
        "1" : model.add,
        "2" : model.read,
        "3" : model.update,
        "4" : model.delete,
        "5" : model.search,
        "6" : model.sorting,
        "7" : model.save,
        "8" : model.load,
        "9" : quit
    }

    user_choice = input("Enter your choice : ")

    todo.get(user_choice,model.errHandler)()
