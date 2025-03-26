temperature = input("Enter temperature: ")
temperature = float(temperature)

if temperature > 40:
    print("It's a hot day")
elif temperature > 20:
    print("It's a warm day")
elif temperature > 10:
    print("It's a cold day")
else:
    print("It's a freezing day")