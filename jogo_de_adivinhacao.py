# jogo da adivinhação

#randint é um método do pacote ramdom retornar um número inteiro aleatório, incluindo as duas pontas [a,b] são inclusivos

#ramndom ( gera várias possibilidades de trazer números aleatórios) (randint gera um número aleatório inteiro)


from random import randint

print('********************************************')
print('Seja bem vindo ao jogo de adivinhação!')
print('********************************************')

print('\n')


numero_secreto = randint(1, 5) 
numero_escolhido = 0 

while True: 

    try:
        numero_escolhido = int(input ('Escolha um número de 1 a 5: '))
    except:
        print('Você escolheu um número inválido!!')
    else:
        if numero_escolhido not in (1,2,3,4,5):
            print('Número precisa estar entre 1 e 5!!')
            continue 
        elif numero_escolhido == numero_secreto:
            print(f'Parabéns!! Você acertou o número secreto: {numero_secreto}!!')
            break
        else:
            print('Você errou!')
            
