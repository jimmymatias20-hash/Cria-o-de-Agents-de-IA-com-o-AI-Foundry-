import os


listas_temas  =  ['aula 1', 'aula 2', 'aula 3', 'aula 4','aula 5' ,'aula 6', 'aula 7', 'aula 8', 'aula 9','aula 10', 
 'aula 11',  'aula 12',  'aula 13'  ]


for i, nomes in enumerate(listas_temas):
    os.makedirs(f"aula {nomes} - {i}", exist_ok=True)