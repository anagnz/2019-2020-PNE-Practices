user_sequence = input("Introduce the sequence: ")

count_A = 0
count_C = 0
count_G = 0
count_T = 0
for element in user_sequence:
    if element == "A":
        count_A += 1
    elif element == "C":
        count_C += 1
    elif element == "G":
        count_G += 1
    else:
        count_T += 1

print("Total lenght: ", len(user_sequence))
print("A:", count_A)
print("C:", count_C)
print("G:", count_G)
print("T:", count_T)
