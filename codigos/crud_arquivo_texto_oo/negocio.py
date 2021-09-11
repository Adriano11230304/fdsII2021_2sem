class Pessoa:
	def __init__(self, nome):
		self.__nome = nome
	def getNome(self):
		return self.__nome
	def setNome(self, nome):
		self.__nome = nome	

class PessoaFisica(Pessoa):
	def __init__(self, cpf, nome):
		self.__cpf = cpf
		Pessoa.__init__(self, nome)

	def getCpf(self):
		return self.__cpf

	def setCpf(self, cpf):
		self.__cpf = cpf	