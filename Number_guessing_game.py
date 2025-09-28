import random

i=random.randint(1,100)
cnt=0
while(True):
  n=int(input("Guess the number: "))
  cnt=cnt+1
  if(n==i):
    print("Number is correct")
    break
  elif(n<i):
    print("Entered number is less than original number")
  else:
    print("Entered number is more than original number")
print("Number of attempts: ",cnt)