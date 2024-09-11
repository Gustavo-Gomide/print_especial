from time import sleep
import string
# palavra para ser mostrada
palavra_alvo = 'carro1427!@'
# palavra inicial: lista de astericos multiplicado pelo tamanho da palavra alvo
palavra_inicial = ['*'] * len(palavra_alvo)  #['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*']
# letras (maiusculo e minusculo), números, espaço e caracteres especiais usando
chars = string.ascii_letters + string.digits + ' ' + string.punctuation
# loop de cada letra da palavra junto de sua posição
for pos, l in enumerate(palavra_inicial):
    # loop de cada caracter na variavel chars
    for char in chars:
        # controla o tempo do código
        sleep(.05)
        # subistitui a possição atual pelo caracter
        palavra_inicial[pos] = char
        # mostra cada caracter da palavra inicial depois de substituida, 
        # end='' para não quebrar a linha,
        # '\r' para reescrever a linha
        print('\r', ''.join(palavra_inicial), end='')
        # verifica se o caracter atual corresponde ao da mesma posição na palavra alvo, se sim encerra o loop e passa para o proxímo caracter
        if char == palavra_alvo[pos]:
            break