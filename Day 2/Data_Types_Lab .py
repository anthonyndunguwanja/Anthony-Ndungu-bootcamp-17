def data_type(x):
  if type(x) is int:
    if x < 100:
        print('less than 100')
    elif x == 100:
        print('equal to 100')
    else:
        print('more than 100')
  elif type(x) is None:
    print('no value')
  elif type(x) is bool:
    print(bool(x))
  elif type(x) is str:
    print(len(x))
  elif type(x) is list:
    if not x:
        print("None")
    else:
        print(x[2])
