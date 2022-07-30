from sympy import NotInvertible
from Base_de_Perguntas import dicionario
import random

dic = dicionario()

continuar = True
while continuar == True:

    nome = input('Digite seu nome:')
    print(f'Ok {nome}, você tem direito a pular 3 vezes e 2 ajudas!\n As opções de resposta são "A", "B", "C", "D", "ajuda", "pula" e "parar"!')
    pulos = 3
    ajudas = 2
    ID = 1

    PREMIO = 0

    premios = 0

    jogos = 0
    
    if jogos < 4:
        nivel = 'facil'
    elif jogos < 7:
        nivel = 'medio'
    else:
        nivel = 'dificil'

    def sorteia_questao(dic, nivel):
        sorteio = random.choice(dic[nivel])
    
    print(sorteia_questao(dic[nivel]))
    
    #print (sorteio)

    f = ''
    b = '----------------------------------------\n'
    c = 'QUESTAO ' + str(ID) + '\n\n'
    d = sorteio['titulo'] +  '\n\n'
    e = 'RESPOSTAS:\n'
    for letra, texto in sorteio['opcoes'].items():
        f +=  (f'{letra}: {texto}' '\n')
    st =  b + c + d + e + f 
    print (st)

    resposta = input('Digite sua resposta')
    jogos += 1
    if resposta != dic['opcoes','letras'] or resposta != 'pula' or resposta != 'ajuda':
        print ('opção inexistente')        

    if resposta == 'pula' and pulos > 0:
        pulos -= 1
    elif resposta == 'ajuda' and ajudas > 0:
        # gera ajuda em questao
        ajudas -= 1
    elif resposta == dic['correta']:
        print('Você acertou! ')
        premios += 1
        if premios == 1:
            PREMIO += 1000    
        elif premios == 2:
            PREMIO += 5000
        elif premios == 3:
            PREMIO += 10000
        elif premios == 4:
            PREMIO += 30000
        elif premios == 5:
            PREMIO += 50000
        elif premios == 6:
            PREMIO += 100000
        elif premios == 7:
            PREMIO += 300000
        elif premios == 8:
            PREMIO += 500000
        elif premios == 9:
            PREMIO += 1000000
    elif resposta != dic['correta']:
        Continuar = input('Você perdeu! Deseja parar ou continuar? ')
        if Continuar == 'parar':
            continuar = False
            print ('Você recebeu o premio de {0}'.format(PREMIO))
        elif Continuar == 'continuar':
            PREMIO = 0
            continuar = True

    if PREMIO == 1000000:
        print ('Você recebeu o premio de {0}'.format(PREMIO))



