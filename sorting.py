def flip(side, lst):
    if side == "R":
        lst.sort()
        print(lst)
        return lst
        
    else:
        lst.sort(reverse=True)
        print(lst)
        return lst
        

flip('R', [3, 2, 1, 2])
