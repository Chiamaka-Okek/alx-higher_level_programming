#!/usr/bin/python3
def element_at(my_list, idx):
    number = len(my_list)
    if idx < 0 and idx >= number:
        return None
    else:
        return(my_list[idx])
