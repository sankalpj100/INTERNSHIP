
def isRotate(s1, s2):
  if len(s1) != len(s2):
    return False
  print(isSubstring(s1 + s1, s2))
  
def isSubstring(s1, s2):
  for i in range(len(s2)):
    substring_present = True
    for j in range(len(s2)):
      if s1[i + j] != s2[j]:
        substring_present = False
        break
    if substring_present:
      return True
  return False

s1 = input("Enter the String:")
s2 = input("ENter the Rotated version:")
isRotate(list(s1), list(s2))