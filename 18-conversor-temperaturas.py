# Define conversion fuctions
def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def fahrenheit_to_celsius(f): 
    return (f - 32) * 5/9

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

def kelvin_to_celsius(k):
    return k - 273.15

def celsius_to_fahrenheit(c):
    return c * 9/5 + 32 

def celsius_to_kelvin(c):
    return c + 273.15

# Define menu fuction
def menu():
    print("Temperature Conversion Menu:")
    print("1. Convert Fahrenheit to Kelvin")
    print("2. Convert Fahrenheit to Celsius")
    print("3. Convert Kelvin to Fahrenheit")
    print("4. Convert Kelvin  to Celsius")
    print("5. Convert Celsius to Fahrenheit")
    print("6. Convert Celsius to Kelvin")
    print("7. Exit")
    
    choice = int(input("Enter  your choice: "))

    if choice == 1:
        f = float(input("Enter temperature in Fahrenheit: "))
        k = fahrenheit_to_kelvin(f)
        print(f"{f}°F is equal to {k}°K")
        menu()
    elif choice == 2:
        f = float(input("Enter temperature in Fahrenheit: "))
        c = fahrenheit_to_celsius(f)
        print(f"{f}°F is equal to {c}°C")
        menu()
    elif choice == 3:
        k = float(input("Enter temperature in Kelvin"))
        f = kelvin_to_fahrenheit(k)
        print(f"{k} °K is equal to {f}°F")
        menu()
    elif choice == 4:
        k = float(input("Enter temperatute in Kelvin"))
        c = kelvin_to_celsius(k)
        print(f"{k}°K is equal to {c}°C")
        menu()
    elif choice == 5:
         c = float(input("Enter temperature in Celsius: "))
         f = celsius_to_fahrenheit(c)
         print(f"{c}°C is equal to {f}°F")
         menu()
    elif choice == 6:
        c = float(input("Enter temperature in Celsius: "))
        k = celsius_to_kelvin(c)
        print(f"{c}°C is equal to {k}°K")
        menu()
    elif choice == 7:
        print("Goodbye!")
    else:
        print("Invalid choice. Please try again.")
        menu()

# Call menu function
menu()