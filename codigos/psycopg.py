import psycopg2

class Carro:
	def __init__(self, placa = "", modelo = "", marca = "", preco = 0):
		self.id = 0
		self.placa = placa
		self.modelo = modelo
		self.marca = marca
		self.preco = preco
	def imprime(self):
		print "==========\nPlaca:"+self.placa + "\n" + "Modelo:"+self.modelo+"\n" + "Marca:"+self.marca+"\n"+"Preco (R$):"+str(self.preco) + "\n==========="

class CarroDAO:
	def __init__(self):
		pass

	def obter(self, placa):
		conn = psycopg2.connect("dbname=concessionaria user=postgres password=postgres host=localhost")
		cur = conn.cursor()
		cur.execute("SELECT * FROM carro WHERE placa = %s", [placa])
		tupla = cur.fetchone()
		carro = Carro()				
		carro.id = int(tupla[0])
		carro.placa = tupla[1]
		carro.modelo = tupla[2]
		carro.marca = tupla[3]
		carro.preco = float(tupla[4])
		cur.close()
		conn.close()
		return carro


	def atualizar(self, carro):
		conn = psycopg2.connect("dbname=concessionaria user=postgres password=postgres host=localhost")
		cur = conn.cursor()
		cur.execute("UPDATE carro SET placa = %s, modelo = %s, marca = %s, preco = %s WHERE id = %s", [carro.placa, carro.modelo, carro.marca, carro.preco, carro.id])
		conn.commit()
		cur.close()
		conn.close()

	def adicionar(self, carro):
		conn = psycopg2.connect("dbname=concessionaria user=postgres password=postgres host=localhost")
		cur = conn.cursor()
		cur.execute("INSERT INTO carro (placa, modelo, marca, preco) VALUES(%s, %s, %s, %s);", [carro.placa, carro.modelo, carro.marca, carro.preco])
		conn.commit()
		cur.close()
		conn.close()

	def listar(self):
		conn = psycopg2.connect("dbname=concessionaria user=postgres password=postgres host=localhost")
		cur = conn.cursor()
		cur.execute("SELECT * FROM carro")
		vetTuplas = cur.fetchall()
		# conn.commit()
		vetCarro = []
		for tupla in vetTuplas:
			vetCarro.append(Carro(tupla[1], tupla[2], tupla[3], float(tupla[4])))				
		cur.close()
		conn.close()
		return vetCarro

	def excluir(self, placa):
		conn = psycopg2.connect("dbname=concessionaria user=postgres password=postgres host=localhost")
		cur = conn.cursor()
		cur.execute("DELETE FROM carro WHERE placa = %s;", [placa])
		conn.commit()
		cur.close()
		conn.close()

if __name__ == '__main__':
	# 3 camada
	carroDAO = CarroDAO()
	
	carro = carroDAO.obter("IXT7889")
	carro.marca = "chevrolet"
	carroDAO.atualizar(carro)	
	
	vetCarro = carroDAO.listar()
	for carroAux in vetCarro:
		carroAux.imprime()