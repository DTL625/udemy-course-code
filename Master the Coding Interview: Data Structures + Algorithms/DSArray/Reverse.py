def reverse_str(input_str):
  res = '';
  for s in input_str[::-1]:
    res += s
  
  return res

input = "Hi I'm sean! nice to meet you"
result = input[::-1]
print(result)

result = reverse_str(input)
print(result)