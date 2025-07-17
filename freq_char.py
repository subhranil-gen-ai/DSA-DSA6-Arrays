def freq_char(s):
  freq={}
  for char in s:
    freq[char]=freq.get(char,0) + 1
  return freq
s='hello'
result=freq_char(s)
print(result)
