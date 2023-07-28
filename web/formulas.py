class Formulas():
    def imc(peso,talla):
        imc = round((float(peso)/1000)/((float(talla)/100)**2),1)
        estado = ''
        if imc < 18.5:
            estado='Bajo Peso'
        elif imc >= 18.5 and imc <= 24.9:
            estado='Normal'
        elif imc >= 25 and imc <= 29.9:
            estado='Sobrepeso'
        elif imc >= 30 and imc <= 34.9:
            estado='Obesidad I'
        elif imc >= 35 and imc <= 39.9:
            estado='Obesidad II'
        elif imc >= 40 and imc <= 49.9:
            estado='Obesidad III'
        elif imc > 50 :
            estado='Obesidad IV'

        return [imc,estado]