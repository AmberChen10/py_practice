s = str(input('Enter a string of lower case characters'))
A = 'abcdefghijklmnopqrstuvwxyz'

for i in range(len(s)):
  for j in range(len(A)):
    if s[i] == A[j]:
      current_num = j
   
  if i == 0:
   previous_num = current_num
   temp = str(s[0])
   previous_string = temp
    
  elif (current_num >= previous_num) and (i != len(s)-1):
   temp = temp + str(s[i])
   previous_num = current_num
  
  elif (current_num >= previous_num) and (i == len(s)-1):
   temp = temp + str(s[i])
   if len(previous_string) < len(temp):
    previous_string = temp
   
  elif len(previous_string) < len(temp):
   previous_string = temp
   temp = str(s[i])
   previous_num = current_num
   
  else:
   temp = str(s[i])
   previous_num = current_num
        
print('Longest substring in alphabetical order is: ' + previous_string)