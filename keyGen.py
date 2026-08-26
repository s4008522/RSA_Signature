# Import Libraries
import math
import hashlib

# RSA Signature Generator
print("\n---=== PROGRAM START ===---")
print("\nkeyGenerator.py is a simple RSA key generator. \nIt will generate the necessary keys for RSA digital signatures.") 

m = int(input("\nEnter the message:               "))
p = int(input("Enter the first prime number:    "))
q = int(input("Enter the second prime number:   "))

# Prime Factorials
n = p * q
on = (p - 1) * (q - 1)

# Parameter
print("You successfully entered both of the prime numbers!")

print("\nYou now need to enter a parameter that is: ")
print("1. Greater than 1")
print("2. Less than the prime factorial totient")
print("3. GCD(parameter, prime factorial totient) = 1")

print("\nTo find the GCD, you can use this website to help you: https://www.dcode.fr/gcd")
print(f"The prime factorial totient is: {on}")
print("For example you would put in 174008449523914080 11 and it would return 1.")

e = int(input("\nEnter the parameter:       "))

# Function to check if the parameter is valid
def check_parameter(parameter):
    if (parameter > 1) and (parameter < on) and (math.gcd(parameter, on) == 1):
        return True
    else:
        return False

# Condition for parameter
if check_parameter(e) == True:
    print(f"The parameter {e} is valid.")

while check_parameter(e) == False:
    print("Invalid parameter.")
    e = int(input("\nEnter the parameter: "))  # Update e, not parameter
    if check_parameter(e) == True:
        print(f"The parameter {e} is valid.")
        break

# Private Key
d = pow(e, -1, on)

# Hashing message into SHA-256
# result = hashlib.sha256(m.encode())
# hash = result.hexdigest()

# Convert hashed message from hex to decimal
# HEXA = int(hash, 16)
# print(f"\nMessage Hash Value:         {hash}") 

# Output
print("\n---=== RESULTS ===---")
print(f"\nMessage Plain Text:                         {m}")    
print("\nDon't share the private key with anyone else!\n")
print(f"Private key:                                {d}\n")     

if input("Do you want to sign the message? (y/n): ").lower() == "y":
    # Sign the decimal number
    s = pow(m, d, n)
    print("\n---=== SIGNATURE RESULTS ===---\n") 
    print(f"Send this to the others to verify your signature!")   
    print(f"\nMessage Plain Text:                         {m}") 
    print(f"Public key Parameter:                       {e}")  
    print(f"Public key Prime Factorial:                 {n}")   
    print(f"Signature:                                  {s}")  
    print("\n---=== PROGRAM ENDED ===---\n")  
else:
    print("\nYou chose not to sign the message.")
    print("\n---=== PROGRAM ENDED ===---\n") 
# End of code