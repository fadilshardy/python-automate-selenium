def get_first_user_with_status_none_from_table(window: object) -> list:
    """
    get first NIK with status NONE by filtering datalist from table GUI
    """
    
    datalist = window['-TABLE-'].get()
        
    user = next(x for x in datalist if(x[2] == "NONE"))
    
    return user
    
    
def update_gui_table(datalist, user, status, window) -> None:
    """
    update GUI table
    """   
    
    userIndex = datalist.index(user)
    
    datalist[userIndex][2] = status.upper()
    
    window['-TABLE-'].update(values=datalist)


    
    
