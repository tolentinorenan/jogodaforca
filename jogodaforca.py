secreto = 'a palavra secreta'
digitadas = []
chances = 3
while True:

    if chances <= 0:
        print('VOCE PERDEU')
        break
    letra = input(f' ( JOGO DA FORCA ) - Você tem apenas {chances} chances.  Digite uma letra: ')

    if len(letra) > 1:
        print('Digite apenas um carácter')
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f'A letra {letra} existe na palavra secreta')
    else:
        print(f'Essa letra {letra} NÃO EXISTE')
        digitadas.pop()
        chances = chances - 1

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'


    if secreto_temporario == secreto:
        print('Voce Ganhou ! ')
        break
    else:
        print(f'A palavra secreta está assim {secreto_temporario}')