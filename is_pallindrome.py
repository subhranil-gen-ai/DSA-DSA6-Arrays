def reverse_a_string(s):
  n=len(s)
  reversed_str=""
  for i in range(n-1,-1,-1):
    reversed_str +=s[i]
  return reversed_str

def is_pallindrome(s):
  a=reverse_a_string(s)
  if a==s:
    return True
  else:
    return False
s=input("enter a string: ")
result=is_pallindrome(s)
print(result)
