from flask import Flask
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/')
def getSaludo():
		return 'Hola mundo'

@app.route('/factorial/<float:numero1>')
def getFactorial(numero1):
		factorial = 1
		for i in range(1, numero1 + 1):
			factorial = factorial * i
		return str(factorial)

@app.route('/suma/<float:numero1>/<float:numero2>')
def getSuma(numero1,numero2):
		return str(numero1+numero2)

@app.route('/resta/<float:numero1>/<float:numero2>')
def getResta(numero1,numero2):
		return str(numero1-numero2)

@app.route('/multiplicacion/<float:numero1>/<float:numero2>')
def getMultiplicacion(numero1,numero2):
		return str(numero1*numero2)

@app.route('/division/<float:numero1>/<float:numero2>')
def getDivision(numero1,numero2):
		if numero2 == 0:
			return 'No se puede dividir entre 0'
		return str(numero1/numero2)

@app.route('/potencia/<float:numero1>/<float:numero2>')
def getPotencia(numero1,numero2):
		return str(numero1**numero2)

@app.route('/raiz/<float:numero1>')
def getRaiz(numero1):
		if numero1 < 0:
			return 'No se puede sacar raiz cuadrada de un numero negativo'
		return str(numero1**0.5)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=81, debug=True)