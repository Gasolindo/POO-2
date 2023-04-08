from gato  import Gato
from dog import Dog


escolha=int(input("Escolha 1 para gato e 2 para cachorro:\n "))
if escolha == 1:
    nome = input("Digite o nome do gato:\n")
    idade= int(input("Digite a idade do gato:\n"))
    peso= float(input("Digite o peso do gato:\n"))
    cor_do_pelo=input("Digite a cor do pelo:\n")
    raça=input("Digite a raça:\n")
    gato=Gato(cor_do_pelo,raça,nome,idade,peso)

    print (gato.dormir())
    print (gato.mensagem())    

elif escolha == 2:
    nome = input("Digite o nome do cahorro:\n")
    idade= int(input("Digite a idade do cachorro:\n"))
    peso= float(input("Digite o peso do cachorro:\n"))
    cor_do_pelo=input("Digite a cor do pelo:\n")
    raça=input("Digite a raça:\n")
    dog=Dog(cor_do_pelo,raça,nome,idade,peso)

    print(dog.dormir())
    print(dog.mensagem())

     