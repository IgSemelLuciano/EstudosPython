import time
import os
import random
print(''''
      
      Decifra-me, ou te devoro.
      
      ''')
while True:
  corresposta=input('''
    Qual a cor do céu?: ''')
  corresposta=corresposta.lower()
  if corresposta=='azul':
      print('''
            Resposta Correta
            ''')
      time.sleep(3)
      os.system('cls')
      break
  else:
      print('''
            
            ''')
      frase1='  Minha Barriga Agradece'
      frase2='  Estava mesmo com fome'
      frase3='  Talvez na próxima vida'
      frase=random.choice([frase1, frase2, frase3,])
      print(' ',frase )
print('Segunda Pergunta')
while True:
      piramide=input('Oque anda com 4 patas durante o dia, 2 durante a tarde, e 3 durante a noite?: ')
      piramide=piramide.lower()
      if piramide=='homem':
            print('''
                  Resposta Correta
                  ''')
            time.sleep(3)
            os.system('cls')
            break
      else:
       print('''
            
            ''')
      frase4='  O sabor da idade é ótimo'
      frase5='  Estava mesmo com fome'
      frase6='  Obrigado pela comida.'
      frase=random.choice([frase4, frase5, frase6,])
      print(' ',frase )
      
print('Terceira e ultima pergunta, estou com fome')
while True:
      maparesposta=input('O que tem cidades, mas não casas, tem montanhas, mas não árvores, e tem água, mas não peixes? ')
      maparesposta=maparesposta.lower()
      if maparesposta=='mapa':
            print('Resposta Correta, a Pirâmide deixou você seguir seu caminho!')
            break
      else:  print('''
            
            ''')
      
      frase7='  Você vai se perder se continuar assim!'
      frase5='  Estava mesmo com fome.'
      frase8='  Você é Saboroso.'
      frase=random.choice([frase7, frase5, frase8,])
      print(' ',frase )
      
