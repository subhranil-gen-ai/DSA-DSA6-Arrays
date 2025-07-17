def reverse_a_string_loop(s):
  n=len(s)
  reversed_str=""
  for i in range(n-1,-1,-1):
    reversed_str +=s[i]
  return reversed_str
s="hello"
result=reverse_a_string_loop(s)
print(result)
