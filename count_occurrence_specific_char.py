def count_occurrence_specific_char(s,target):
  count=0
  for char in s:
    if char == target:
      count += 1
  return count
s='hello'
target='l'
result=count_occurrence_specific_char(s,target)
print(result)
