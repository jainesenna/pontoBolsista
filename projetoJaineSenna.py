#!/usr/bin/python
# -*- coding: utf-8 -*-
print('*'*35)
print('FREQUÊNCIA DE BOLSISTA DO CERES/UFRN')
print('*'*35)


import os #Biblioteca para limpar a tela
from datetime import datetime
	
# //-- PEGANDO DATA E HORA DO SISTEMA --//
def data(): 
	now = datetime.now()
	dia = ("%d/%d/%d" %(now.day,now.month,now.year))
	return dia

def hora():
	now = datetime.now()
	hora = ("%d:%d:%d" %(now.hour,now.minute,now.second))
	return hora
	
def datahora(): 
	print(data())
	print(hora())

Bolsistas = {'cod' : [], 'nome' : [], 'mat' : [], 'local' : [], 'tutor' : [], 'tel' : []}


numBolsistas = 0
	
aux = True
while aux:

    # //-- Menu Inicio --//
	print ("")
	print ("1 - Menu Bolsista")
	print ("2 - Registrar ponto")
	print ("3 - Sair")

	menu = input("Digite o numero da opçao desejada: ")
    
    # //-- Fecha Programa --//
	if menu == '3':
		aux = False
     
    # //-- Menu Bolsista --//
	if menu == '1':

		aux1 = True
		while aux1:
			print("")
			print("1 - Inserir novo bolsista")
			print("2 - Consultar dados de um bolsista")
			print("3 - Atualizar cadastro de um bolsista")
			print("4 - Remover um bolsista")
			print("5 - Imprimir lista de bolsista")
			print("6 - Voltar para o Menu Inicío")
			
			menuBolsista = input ("\nDigite o numero da opçao desejada: ")
			os.system("cls")
            # //-- Sair do menu Bolsista --//
			if menuBolsista == '6':
				aux1 = False
			    
            # //-- 1- Inserir novo bolsista --//
			if menuBolsista == '1':

				if numBolsistas < 10: 
                    
					cod = input ("\nInforme o codigo do bolsista: ")
					nome = input ("Informe o nome do bolsista: ")
					mat = input ("Informe o numero da matricula do bolsista: ")
					local = input ("Informe o local de atividade: ")
					tutor = input ("Informe o nome do Tutor: ")
					tel = input ("Informe o telefone do bolsista: ")
				
					os.system("cls")

				
					Bolsistas['cod'].append(cod)
					Bolsistas['nome'].append(nome)
					Bolsistas['mat'].append(mat)
					Bolsistas['local'].append(local)
					Bolsistas['tutor'].append(tutor)
					Bolsistas['tel'].append(tel)
					
					numBolsistas += 1

				else:
					print("\nNumero maximo de Bolsista atingido!!")
                    
                # //-- 2- Consultar dados de um bolsista --//
			if menuBolsista == '2':
                
				consultar = input ("\nInforme o codigo do bolsista: ")
				consultarV = consultar in Bolsistas['cod']
								
				if consultarV == True:
					pos = Bolsistas['cod'].index(consultar)
					
					print("Codigo:",Bolsistas['cod'][pos],
						"\nNome:",Bolsistas['nome'][pos],
						"\nMatricula:",Bolsistas['mat'][pos],
						"\nLocal da Atividade:",Bolsistas['local'][pos],
						"\nTutor:",Bolsistas['tutor'][pos],
						"\nTelefone:",Bolsistas['tel'][pos])
					
				else:
					print("Codigo invalido!!!")
                 
                # //-- 3- Atualizar cadastro de um bolsista --//
			if menuBolsista == '3':
                
				consultar = input ("\nInforme o codigo do bolsistas: ")
				consultarV = consultar in Bolsistas['cod']
								
				if consultarV == True:
					
					cod1 = input ("\nInforme o codigo do bolsista: ")
					nome1 = input ("Informe o nome do bolsista: ")
					mat1 = input ("Informe o numero da matricula do bolsista: ")
					local1 = input ("Informe o local de atividade: ")
					tutor1 = input ("Informe o nome do Tutor: ")
					tel1 = input ("Informe o telefone do bolsista: ")
					os.system("cls")
                    
                    										
					pos = Bolsistas['cod'].index(consultar)
										
					Bolsistas['cod'][pos] = cod1
					Bolsistas['nome'][pos] = nome1
					Bolsistas['mat'][pos] = mat1
					Bolsistas['local'][pos] = local1
					Bolsistas['tutor'][pos] = tutor1
					Bolsistas['tel'][pos] = tel1
					
					print("\nDados atualizados!!!\n")

				else:
					print("Codigo invalido!!!")
                
                # //-- 4 - Remover um Bolsista --//
			if menuBolsista == '4':
                
				consultar = input ("\nInforme o codigo do Bolsista ")
				consultarV = consultar in Bolsistas['cod']
								
				if consultarV == True:
					pos = Bolsistas['cod'].index(consultar)
					Bolsistas['cod'].pop(pos) # POP remove
					Bolsistas['nome'].pop(pos)
					Bolsistas['mat'].pop(pos)
					Bolsistas['local'].pop(pos)
					Bolsistas['tutor'].pop(pos)
					Bolsistas['tel'].pop(pos)
															
					numBolsistas = numBolsistas - 1

					print("Removido com sucesso")

				else:
					print("Codigo invalido!!!")

				# //-- 5 - Imprimir lista de bolsistas --//
			if menuBolsista == '5':
               
								
				for i in range(numBolsistas):              
                    
					print("Codigo:",Bolsistas['cod'][i],
						"\nNome:",Bolsistas['nome'][i],
						"\nMatricula:",Bolsistas['mat'][i],
						"\nLocal da Atividade:",Bolsistas['local'][i],
						"\nTutor:",Bolsistas['tutor'][i],
						"\nTelefone:",Bolsistas['tel'][i])
					
    # //-- FIM do Menu Bolsista --//
    
    # //-- Menu Registro --//
	if menu == '2':
        
		aux2 = True
		while aux2:

			print("")
			print("1 - Registrar Entrada")
			print("2 - Registrar Saída")
			print("3 - voltar")
				   

			Menu = input("\nDigite o numero da opçao desejada: ")
						
			if Menu == '3':
				aux2 = False

			if Menu == '1':

				consultar = input ("\nInforme o codigo do bolsista que quer registrar a entrada: ")
				consultarV = consultar in Bolsistas['cod']
								
				if consultarV == True:
                    
					pos = Bolsistas['cod'].index(consultar)
					
					print("ENTRADA")
					ent = datahora()
					
											                  
				else:
					print ("Bolsista não existe!!")
			if Menu == '2':

				consultar = input ("\nInforme o codigo do bolsista que quer registrar a saida: ")
				consultarV = consultar in Bolsistas['cod']
								
				if consultarV == True:
                    
					pos = Bolsistas['cod'].index(consultar)
					
					print("SAIDA")
					sai =  datahora()
					
					
																				                 
				else:
					print ("Conta nao existe!!")
print ("Finalizado")
