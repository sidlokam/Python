# This is a program that will find the prime factors of a number
# By: Siddharth Lokam
# Date: 7-5-2017

# This is the main function that prints the prime factors of the Numbers
def print_factors(x):
   print("The prime factors of",x,"are:")
   for i in range(2, x + 1):
       if x % i == 0:
          for j in range(2, x + 1):
            if (x % j) == 0:
              is_prime(i)
              break

# Function to find if a number is prime or not
def is_prime(x):
  for i in range (2, x - 1):
    if x % i == 0:
      break
  else:  
    print(x)
    
num = int(input("Enter a number: "))

print_factors(num)
