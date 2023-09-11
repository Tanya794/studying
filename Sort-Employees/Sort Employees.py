def sort_employees(employees, sort_by):
    def sort_index(item):
        lst = ["name", "age", "salary"]
        index = lst.index(sort_by)
        return item[index]
    
    new_lst = sorted(employees, key = sort_index)
    return new_lst
