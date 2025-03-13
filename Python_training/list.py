def list_to_string(lst):
    if len(lst) == 0:
        return ""
    elif len(lst) == 1:
        return lst[0]
    else:
        return ", ".join(lst[:-1]) + " and " + lst[-1]
    


products = ['apples', 'bananas', 'milk', 'tofu', 'cats']
result = list_to_string(products)
print(result)