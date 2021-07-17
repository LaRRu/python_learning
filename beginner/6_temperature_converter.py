'''Make a Temperature/Measurement Converter.
Write a script that can convert
Fahrenheit to Celcius and back,
or inches to centimeters and back, etc.
How far can you take it?

For all projects at beginner level user input validation is not performed.
'''


def convert_temperature(temp):
    '''formula (0 °C × 9/5) + 32 = 32 °F'''

    #  Another convention for handling input
    value = float(temp.split()[0])

    if 'C' in temp:
        converted_temp = celsius_to_fahrenheit(value)
        return f'{converted_temp} °F'
    if 'F' in temp:
        converted_temp = fahrenheit_to_celsius(value)
        return f'{converted_temp} °C'


def celsius_to_fahrenheit(temp: float) -> float:
    return (temp * 9/5) + 32


def fahrenheit_to_celsius(temp: float) -> float:
    return (temp - 32) * 5/9
