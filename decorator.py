# lOS DECORADORES son funciones que reciben como parametro una funcion
# y retornan una funcion. Se ocupan para ejecutar una funcion unicamente cuando
# esta es realmente necesita ejecutarse

def validator(func):
    def validate_password(password):
        if password =='Platzi':
            return func()
        else:
            print('Contraseña Incorrecta')
    return validate_password



@validator
def open_system():
    print('La contraseña es correcta')



if __name__ == "__main__":
    password = str(input('Please enter your password'))
    open_system(password)