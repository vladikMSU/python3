obj = eval(input())

lst = [field for field in dir(obj) if type(eval("obj."+field)) is int]

print(len(lst))