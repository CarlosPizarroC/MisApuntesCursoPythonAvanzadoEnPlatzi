def is_palidrome(string: str) -> bool:
    string = string.replace(" ", "") #Limpiamos espacios vacíos.
    string = string.lower() #Lo ponemos en minúsculas.
    return string == string[::-1]

def run():
    print(is_palidrome(1000))


if __name__ == '__main__':
    run()
