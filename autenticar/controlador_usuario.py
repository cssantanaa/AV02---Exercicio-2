usuarios = [
{
    "username": "admin",
    "password": "senha"
},
{
    "username": "admin1",
    "password": "senha1" 
},
{
    "username": "admin2",
    "password": "senha2"
},
{
    "username": "admin3",
    "password": "senha3"

},
]

def autenticar(login, senha):
    for usuario in usuarios:
        if usuario["username"] == login and usuario["password"] == senha:
            return True
        return False
