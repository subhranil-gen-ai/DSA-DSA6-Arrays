def freq(s):
  freq={}
  for char in s:
      freq[char] =freq.get(char,0)+1
  return freq
def unique_char(s):
  a=freq(s)
  for count in a.values():
    if count>1:
      return False
  return True
s='hello'
result=unique_char(s)
print(result)
