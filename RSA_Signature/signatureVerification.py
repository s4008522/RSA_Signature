print("\n---=== PROGRAM START ===---")
print("\nThis program is a simple RSA signature verification.")

# Inputs for the verification
message = int(input("\nEnter the message decimal the person sent you:                          "))                 
publicKeyPrimeFactorial = int(input("Enter the public key prime factorial the person sent you:               "))    
publicKeyParameter = int(input("Enter the public key parameter the person sent you:                     "))         
signature = int(input("Enter the signature the person sent you:                                "))                  

# Perform RSA signature verification
messageVerification = pow(signature, publicKeyParameter, publicKeyPrimeFactorial)
print(f"\nMessage verification: {messageVerification}")
print(f"Message:              {message}")

# Check if the verification is successful
if messageVerification == message:
    print("\nMessage verification is successful!")
else:
    print("\nMessage verification is unsuccessful!")

print("\n---=== PROGRAM ENDED ===---\n")
# Hey