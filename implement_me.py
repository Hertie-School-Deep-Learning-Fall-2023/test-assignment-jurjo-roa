
def lcm(a, b):
  """compute Least Common Multiple between two integers."""

  # choose the greater number
  if a > b:
    greater = a
  else:
    greater = b

  while(True):
    if((greater % a == 0) and (greater % b == 0)):
      lcm = greater
      break
    greater += 1

  return lcm
  pass


lcm(4, 99)