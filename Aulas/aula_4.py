def print_one_letter_per_line(x):
    for i in x:
        print(i)


# ou

def print_one_letter_per_line_2(x):
    i = 0
    while i != len(x):
        print(x[i])
        i += 1


def modulus(x):
    return (x.real ** 2 + x.imag ** 2) ** 0.5


def print_one_letter_per_line_inverted(x):
    for i in reversed(x):
        print(i)


# ou

def print_one_letter_per_line_inverted_2(x):
    i = -1
    while i != -len(x) - 1:
        print(x[i])
        i -= 1


def todas_as_letras_sao_maiusculas(x):
    return x.isupper()


# Jogo da Forca


def get_mask(palavra):
    i = 0
    mask = ''
    while i < len(palavra):
        mask += '_'
        i += 1
    return mask


def letter_to_mask(palavra, mask, letra):
    i = 0
    new_mask = ''
    while i < len(palavra):
        if palavra[i] == letra:
            new_mask += palavra[i]
        else:
            new_mask += mask[i]
        i += 1
    return new_mask


def play_hangman(palavra, vidas):
    mask = get_mask(palavra)
    while vidas > 0:
        print('Advinhe a palavra: ', mask)
        letra = input('Letra: ')
        if palavra.count(letra) > 0:
            mask = letter_to_mask(palavra, mask, letra.upper())
            if mask == palavra:
                print('Parabéns, acertou a palavra --> ', palavra)
                return
        else:
            vidas -= 1
            if vidas > 1:
                print('Errou, tente novamente')
                print('Ainda tem ', vidas, 'vidas')
            elif vidas == 1:
                print('Já só tem 1 vida restante', '\n')
            elif vidas == 0:
                print('\n', 'Perdeu')
    print('A palavra era: ', palavra)
