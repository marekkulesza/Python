# Testing multiple box sizes instead of just making one
size = list(range(5,20))
column = size
row = size

# This for loop checks out the numbers in the size list and sets them to the size
for element in size:
    size = element
    column = element
    row = element

    # This creates the boxes
    while row > 0:
        while column > 0:
            if column == element:
                print("+ " + "- "*(element) + "+")
            column -= 1
            print("| "+"  "*(element) + "|")
        row -= 1
    if row == 0:
        print("+ " + "- "*(element) + "+")
