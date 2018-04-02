print('Welcome to FizzBuzz, A simple python shell program that prints numbers from 1 to 100, But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”.')
print('Enter the last number in the range')
maxNumber=int(input())
print('Enter the starting number')
i=int(input())
print('hello')
for i in range(i,maxNumber+1):
  if ((i%3==0) and (i%5==0)):
    print ('fizz buzz')
  elif i%3==0:
    print ('fizz')
  elif i%5==0:
    print ('buzz')
  else:
    print (i)
