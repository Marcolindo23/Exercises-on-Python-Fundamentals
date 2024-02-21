r1 = int(input("il valore di r1 è:"))
r2 = int(input("il valore di r2 è:"))
r3 = int(input("il valore di r3 è:"))
h = int(input("il valore di h è:"))
π = 3.1415

S1=π*(r1**2)
S2=π*(r2**2)
S3 =π*(r3**2)
V = 1/6*h*(S1+(4*S2)+S3)
print(f"il valore del volume è: {V}")


