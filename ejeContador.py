class Contador():

  def __init__(self, inicial=0):
    self.numero = inicial

  def getSiguiente(self):
    self.numero += 1
    return self.numero

  def getAnterior(self):
    self.numero -= 1
    return self.numero

  def setSiguiente(self):
    self.numero += 1
    return self.numero

  def setAnterior(self):
    self.numero -= 1
    return self.numero
  


cuenta= Contador()

for i in range(5):
   print(cuenta)