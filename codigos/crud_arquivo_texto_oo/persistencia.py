from negocio import *

class PessoaFisicaDAO:
	def __init__(self):
		pass
	def limpar(self):
		temp = open("database.txt","w")
		temp.close()	
	def adicionar(self, pessoaFisica):	
		nome = pessoaFisica.getNome()
		cpf = pessoaFisica.getCpf()
		temp = open("database.txt","a+")
		temp.write(cpf.strip()+";"+nome.strip()+"\n")
		temp.close()		
	def alterar(self, pessoaFisica):
		vetPessoa = self.listar()
		self.limpar()
		i = 0 
		while i < len(vetPessoa):
			pFisica = vetPessoa[i]
			if (pFisica.getCpf().strip() != pessoaFisica.getCpf().strip()):
				self.adicionar(pFisica)
			else:
				self.adicionar(pessoaFisica)	
			i = i + 1	
	def excluir(self, cpf):
		vetPessoa = self.listar()
		self.limpar()
		i = 0 
		while i < len(vetPessoa):
			pessoaFisica = vetPessoa[i]
			if (pessoaFisica.getCpf().strip() != cpf.strip()):
				self.adicionar(pessoaFisica)
			i = i + 1
	def listar(self):
		vetPessoa = []
		temp = open("database.txt","r")
		vetLinha = temp.readline().strip().split(";")
		while len(vetLinha) == 2:
			cpf = vetLinha[0]
			nome = vetLinha[1]
			pessoaFisica = PessoaFisica(cpf, nome)
			vetPessoa.append(pessoaFisica)
			vetLinha = temp.readline().strip().split(";")
		temp.close()	
		return vetPessoa	