# 7- Crie um Arquivo Main (main.py): Crie um arquivo chamado main.py no mesmo diretório que suas classes.

from carro import Carro
from moto import Moto
from veiculo import Veiculo

carro1 = Carro('BMW', 'X6', 4)
carro2 = Carro('Audi', 'RS6', 4)
carro3 = Carro('Volkswagen', 'Gol', 2)

moto1 = Moto('Yamaha', 'XJ6', 'Esportiva')
moto2 = Moto('Honda', 'Cg 150', 'Casual')
moto3 = Moto('BMW', 'S1000RR', 'Esportiva')

# 8- Exiba as Informações: Para cada instância, imprima no console as informações utilizando o método __str__.

def main():
    print()
    print(carro1)
    print(carro2)
    print(carro3)
    print()
    print(moto1)
    print(moto2)
    print(moto3)
    print()

if __name__== '__main__':
    main()