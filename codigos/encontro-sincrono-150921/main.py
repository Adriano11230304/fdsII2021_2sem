
class Carro:
    def __init__(self, modelo = "", marca = "", preco = 0.0):
        self.modelo = modelo
        self.marca = marca
        self.preco = preco       

class CarroDAO:
    def __init__(self, dbname = ""):
        self.dbname = dbname        
    def listar(self):
        vetCarro = [] 
        arquivo = open(self.dbname, "r")
        for linha in arquivo.readlines():
            carroAux = linha.split(";")
            vetCarro.append(Carro(carroAux[0], carroAux[1], float(carroAux[2])))            
        arquivo.close()
        return vetCarro
    def adicionar(self, carro):
        arquivo = open(self.dbname, "a")
        arquivo.write(carro.modelo+";"+carro.marca+";"+str(carro.preco)+";\n")
        arquivo.close()
    def excluir(self, modelo):
        vetCarro = self.listar()
        vetCarroResult = []
        for c in vetCarro:
            if (c.modelo != modelo):
                vetCarroResult.append(c)
        arquivo = open(self.dbname, "w")
        arquivo.close()
        for c in vetCarroResult:
            self.adicionar(c)
    def atualizar(self, carro):
        vetCarro = self.listar()
        vetCarroResult = []
        for c in vetCarro:
            if (c.modelo == carro.modelo):
                vetCarroResult.append(carro)
        arquivo = open(self.dbname, "w")
        arquivo.close()
        for c in vetCarroResult:
            self.adicionar(c)

if __name__ == '__main__':
    carroDAO = CarroDAO("carros.csv")        
    carroDAO.atualizar(Carro("Fiesta","Ford",5))
    vetCarro = carroDAO.listar()    
    for c in vetCarro:
        print(c.modelo + ":"+str(c.preco))    
    