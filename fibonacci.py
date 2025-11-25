def fibonacci(n):
  first=0
  second=1
  while (n>0):
    third=first+second
    first=second
    second=third
    n-=1
  print(third)

n= int(input("Enter a number: "))
fibonacci(n)
