import random
nome = input('Digite seu nome:')
print(f'Ok {nome}, você tem direito a pular 3 vezes e 2 ajudas!\n As opções de resposta são "A", "B", "C", "D", "ajuda", "pula" e "parar"!')
pula = 3
dica = 2
ID = 1

nivel == 'facil'



sorteio = random.choice(dic['nivel'])
print (sorteio)

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
if resposta == 'pula':
    pula -= 1
elif resposta == 'dica':
    # gera ajuda em questao
    dica -= 1
elif resposta == dic['correta']:
    print('Você acertou! ')
