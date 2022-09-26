inp_str = input("Enter the Roman number : ")
di = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}
s = inp_str.upper()

n = len(inp_str) 
i= n-1     

def check_inp(s,i,di):
  
  while i>=0:
   if s[i] not in di:
    return False
    break
   else :
      i-=1
  return True

def Roman_to_Integer(s,n,i,di):
  output = 0
  while i>=0: #
    if i<n-1 and di[s[i]] < di[s[i+1]]:
       output -= di[s[i]]
    else:
       output += di[s[i]] 
    i-=1
  return output



if check_inp(s,i,di) == True :
  print(Roman_to_Integer(s,n,i,di))
else:
  print("Invalid input Value !!")
