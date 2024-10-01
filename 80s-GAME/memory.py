import string
import os
import random
import time

os.system('cls||clear')

print('Mensagem Vital'
      '\n')

while True:
    D = int(input('Qual o seu nivel? (4-12)'))
    if D >= 4 and D <= 12:
     break

M = ''

for i in range(D):
    M += random.choice(string.ascii_uppercase)

os.system('cls||clear')

print('Mande esta mensagem:'
        '\n'
        '\n ', M)

time.sleep(0.5*D)
os.system('cls||clear')

N = input('')
if N == M:
    print('Parabéns, estamos à salvo!'
          '\n')
else:
    print('Você falhou'
          'sua mensagem deveria ser', M)

    time.sleep(0.5 * D)
    os.system('cls||clear')

    print('.'
          '.'
          '.'
          'A Guerra começará.')
