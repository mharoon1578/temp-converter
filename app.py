def c_to_f(celsius):
    return (celsius * 9/5) + 32

def f_to_c(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    print("Welcome to Temperature Converter!")
    print("25°C in Fahrenheit:", c_to_f(25))
    print("77°F in Celsius:", f_to_c(77))

if __name__ == "__main__":
    main()
