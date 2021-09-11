# classes de negocio -> Pessoa e PessoaFisica
from negocio import *
# classes de persistencia -> PessoaFisicaDAO
from persistencia import *

str_menu = "1) cadastrar, 2) listar, 3) excluir, 4) editar 0) Sair\n"
menu = int(raw_input(str_menu))
pessoaFisicaDAO = PessoaFisicaDAO()

while menu != 0:		
	if menu == 1:	
		cpf = raw_input("cpf:")
		nome = raw_input("nome:")	
		# classe da camada de negocio
		pessoaFisica = PessoaFisica(cpf, nome)		
		# classe da camada de persistencia
		pessoaFisicaDAO.adicionar(pessoaFisica)		
		print "Pessoa Adicionada"	
	elif menu == 2:
		# listagem de todas as pessoas cadastradas
		vetPessoa = pessoaFisicaDAO.listar()
		print "==========================="	
		for p in vetPessoa:
			print p.getCpf()+";"+p.getNome()
		print "==========================="	
	elif menu == 3:
		# listagem de todas as pessoas cadastradas
		cpf = raw_input("cpf:").strip()		
		pessoaFisicaDAO.excluir(cpf)
	elif menu == 4:
		cpf = raw_input("cpf:").strip()
		novo_nome = raw_input("nome:").strip()					
		pessoaFisicaDAO.alterar(PessoaFisica(cpf, novo_nome))
		
	menu = int(raw_input(str_menu))
	
print "Obrigado por usar nosso software"	