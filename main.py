def main():
    """
    ##################################################
    # Comlete your code here
    Use the same variables: celsius fahrenheit 
    ##################################################
    """
    def fahrenheit_converter(x):
        return ((9/5)*x)+32

    celsius = int(input("Please enter a Celsius tempature: \t"))

    fahrenheit = fahrenheit_converter(celsius)
    print(f'Fahrenheit: \t {fahrenheit:.2f}')

    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return celsius, fahrenheit


if __name__ == '__main__':
    main()
