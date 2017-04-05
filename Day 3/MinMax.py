def find_max_min(a):
#First check that an argument is a list
  if type(a) is list:
    if max(a) == min(a):#If an argument is a list test whether max(list) is equal to min(list) if yes  print max(list)
        return [max(a)]
    else:#Else print min(a),max[a] as a list
        return [min(a),max(a)]
  else:
    return None
print(find_max_min([4, 4, 4, 4]))
