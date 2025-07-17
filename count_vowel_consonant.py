def count_vowel_consonant(s):
  count1 =0
  count2 =0
  for ch in s:
    if ch.isalpha():
      if ch.lower() in 'aeiou':
        count1 += 1
      else:
        count2 += 1
  return count1,count2

s=input("enter a string: ")
result=count_vowel_consonant(s)
print(result)
