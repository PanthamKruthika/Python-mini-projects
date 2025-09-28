
while(True):
  print("-----MENU-----")
  print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Exit")
  ch=int(input("Enter your choice: "))
  if ch==1:
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    print("Result=",a+b)
  elif ch==2:
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    print("Result=",a-b)
  elif ch==3:
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    print("Result=",a*b)
  elif ch==4:
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    if b==0:
      print("Division by zero- not possible")
    else:
      print("Result=",a/b)
  elif ch==5:
    break
  else:
    print("invalid choice")