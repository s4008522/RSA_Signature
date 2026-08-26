print("\n---=== PROGRAM START ===---")
print("\nsignatureVerification.py is a simple RSA signature verification program. \nIt will verify the digital signature of a message.") 

# Inputs for the verification
m = int(input("\nEnter the message the person sent you:                                   "))                 
e = int(input("Enter the public key parameter the person sent you:                      "))  
n = int(input("Enter the public key prime factorial the person sent you:                "))           
s = int(input("Enter the signature the person sent you:                                 "))                  


# Perform RSA signature verification
mVerification = pow(s, e, n)
print(f"\nMessage verification:   {mVerification}")
print(f"Message:                {m}")

# Check if the verification is successful
if mVerification == m:
    print("\nMessage verification is successful!")
else:
    print("\nMessage verification is unsuccessful!")

print("\n---=== PROGRAM ENDED ===---\n")
# Hey