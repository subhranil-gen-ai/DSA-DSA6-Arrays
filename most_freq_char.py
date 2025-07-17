
def freq(s):
  freq={}
  for char in s:
    freq[char]=freq.get(char,0)+1
  return freq
def most_freq_char(s):
  a=freq(s)
  for char in a.values():
    for char in a:
      most_freq_count=max(a.values())
      if a[char]==most_freq_count:
        print(f"Most frequent character:{char} appears {most_freq_count} times")
        return char,most_freq_count
s='hello'
result=most_freq_char(s)
print(result)
