#Código para identificar si un número es primo con tipado estático

def isprimo(numero: int) -> str:
    for i in range(2, numero):
        if numero%i == 0:
            return f'\n{numero} no es un número primo'

    return f'{numero} es un número primo'

def run():
    respuesta: str
    numero: int
    while True:

        try:
            respuesta = input('Digita un número: ')
            assert respuesta.isnumeric()
            numero = int(respuesta)
            print(isprimo(numero))
            break
        except AssertionError:
            print('Por favor digite un número.')


if __name__ == '__main__':
    run()

    
