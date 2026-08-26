# Input values
m = int(input("\nEnter the message:             "))
p = int(input("Enter the first prime number:    "))
q = int(input("Enter the second prime number:   "))
k1 = int(input("Enter the first key:            "))
k2 = int(input("Enter the second key:           "))

# Calculate prime factorials
n = p * q
on = (p - 1) * (q - 1)

# Calculate the third key
k3 = pow((k1 * k2), -1, on)

# Person A signs first, and Person B signs second
s1 = pow(m, k1, n)
s2 = pow(s1, k3, n)

# Person C verifies the signature
mV = pow(s2, k2, n)

print(f"\nMessage verification:   {mV}")
print(f"Message:                {m}")

if mV == m:
    print("\nMessage verification is successful!")
else:
    print("\nMessage verification is unsuccessful!")