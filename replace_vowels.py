def replace_vowels(s):
  for char in s:
    vow=char.lower() in 'aeiou'
    if vow:
      s=s.replace(char,'*')
  return s
s='hello'
result=replace_vowels(s)
print(result)
