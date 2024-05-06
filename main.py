import fibonacci

def main():
    print("Starting main...")
    number = int(input("Enter the length of fibonacci sequence: "))
    
    series = fibonacci.get_fibonacci_series(number)

    print(series)
    if series is False:
        print("Invalid inpur, please enter positive number")
main()