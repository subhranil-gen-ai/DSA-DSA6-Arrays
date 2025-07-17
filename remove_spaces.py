def remove_spaces(s):
  result=""
  for ch in s:
    if ch != " ":
      result += ch
  return result
s='hello boy'
result=remove_spaces(s)
print(result)
