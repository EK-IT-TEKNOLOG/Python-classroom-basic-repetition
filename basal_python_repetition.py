import pytest

# lav funktionen return_hello, så at testen fuldføres

def test_return_hello():
    assert return_hello() == "Hello, World!"

# lav funktionen average_of_two_numbers, så at testen fuldføres

def test_average_of_two_numbers():
    assert average_of_two_numbers(10, 20) == 15

# lav funktionen rectangle_area, så at testen fuldføres
def test_rectangle_area():
    assert rectangle_area(10, 40) == 400

# Lav funktionen så at testen fuldføres brug: T(°F) = T(°C) × 9/5 + 32
def test_fahrenheit_to_celsius():
    assert fahrenheit_to_celsius(108)

# Lav funktionen så at testen fuldføres brug: T(°C) = (T(°F) - 32) × 5/
def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(108)

# Skriv en funktion, der tager en streng som parameter. 
# Navngiv funktionen "echo" Den skal returnere de første tre tegn fra strengen, gentaget tre gange. 
# Hvis der er mindre end tre tegn i strengen, skal den returnere hele strengen tre gange.

# sørg for at de to tests fuldføres
def test_echo(echo_string):
    assert echo("Python") == "PytPytPyt"

def test_echo_less_than_3_chars(echo_string):
    assert echo("Na") == "NaNaNa"