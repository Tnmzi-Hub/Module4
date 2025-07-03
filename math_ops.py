import math

while True:
    try:
        num = float(input("Enter a number: "))
        if num<= 0:
            print("Please enter a number greater than 0 for sqrt and log.")
            continue
        break
    except ValueError:
        print("Enter a valid number")
        
sqrt = math.sqrt(num)
log = math.log(num)
sine = math.sin(num)

print(f"Square root of number: {sqrt}")
print(f"Natural Log: {log}")
print(f"Sine in radians: {sine}")
