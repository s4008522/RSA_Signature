# Import Libraries
import math
import hashlib

# RSA Signature Generator
print("\n---=== PROGRAM START ===---")
print("\nThis program is a simple RSA signature generator. \nIt will hash your message in SHA-256 and digitally sign it.") 
message = input("\nEnter the message:             ")
prime1 = int(input("Enter the first prime number:  "))
prime2 = int(input("Enter the second prime number: "))

# Prime Factorials
primeFactorial = prime1 * prime2
primeFactorialn = (prime1 - 1) * (prime2 - 1)

# Parameter
print("You successfully entered both of the prime numbers!")
print("\nYou now need to enter a parameter that is: ")
print("1. Greater than 1")
print("2. Less than the prime factorial totient")
print("3. GCD(parameter, prime factorial totient) = 1")
print("\nTo find the GCD, you can use this website to help you: https://www.dcode.fr/gcd")
print(f"The prime factorial totient is: {primeFactorialn}")
print("For example you would put in 174008449523914080 11 and it would return 1.")
parameterNumber = (int(input("\nEnter the parameter: ")))

# Function to check if the parameter is valid
def check_parameter(parameter):
    if (parameter > 1) and (parameter < primeFactorialn) and (math.gcd(parameter, primeFactorialn) == 1):
        return True
    else:
        return False

# Condition for parameter
if check_parameter(parameterNumber) == True:
    print(f"The parameter {parameterNumber} is valid.")

while check_parameter(parameterNumber) == False:
    print("Invalid parameter.")
    parameterNumber = int(input("\nEnter the parameter: "))  # Update parameterNumber, not parameter
    if check_parameter(parameterNumber) == True:
        print(f"The parameter {parameterNumber} is valid.")
        break

# Private Key
privateKey = pow(parameterNumber, -1, primeFactorialn)

# Hashing message into SHA-256
result = hashlib.sha256(message.encode())
hash = result.hexdigest()

# Convert hashed message from hex to decimal
HEXA = int(hash, 16)

# Sign the deciaml number
signature = pow(HEXA, privateKey, primeFactorial)

# Output
print(f"\nMessage Hash Value:         {hash}")              
print("")
print(f"Send this to the others to verify your signature!")
print(f"Message Decimal:            {HEXA}")                       
print(f"Public key Prime Factorial: {primeFactorial}")      
print(f"Public key Parameter:       {parameterNumber}")      
print(f"Siganature:                 {signature}")           
print("\nDon't share the private key with anyone else!")
print(f"Private key:                {privateKey}")          
print("\n---=== PROGRAM ENDED ===---\n")
# End of code