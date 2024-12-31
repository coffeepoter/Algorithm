results = {"A": 0, "B": 0, "C": 0, "D": 0} 
emergency_count = 0

for _ in range(3):  
    symptom, temperature = input().split()
    temperature = int(temperature)

    if symptom == "Y" and temperature >= 37:
        results["A"] += 1
        emergency_count += 1
    elif symptom == "N" and temperature >= 37:
        results["B"] += 1
    elif symptom == "Y" and temperature < 37:
        results["C"] += 1
    else:
        results["D"] += 1

print(results["A"], results["B"], results["C"], results["D"], end=" ")

if emergency_count >= 2:
    print("E")
