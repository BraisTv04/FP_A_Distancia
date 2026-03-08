import random

from faker import Faker

usuarios = []

for i in range(15):
    fake = Faker()
    usuario = {
        "cdg": i,
        "nome": fake.name(),
        "direccion": fake.address(),
        "email": fake.email(),
        "telefono": fake.phone_number()
    }
    usuarios.append(usuario)


print(f"O usuario chamado {random.choice(usuarios)['nome']} foi o afortunado!")