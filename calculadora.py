class Calculadora():
    def __init__(self) -> None:
        self.operadores = {
            '*': self.multiplicar,
            '/': self.dividir,
            '+': self.somar,
            '-': self.subtrair,
        }
        
        self.oper1 = {
            '*': self.multiplicar,
            '/': self.dividir,
        }
        self.oper2 = {
            '+': self.somar,
            '-': self.subtrair,
        }


    def somar(self, num1, num2) -> int:
        return num1 + num2
    def subtrair(self, num1, num2) -> int:
        return num1 - num2
    def multiplicar(self, num1, num2) -> int:
        return num1 * num2
    def dividir(self, num1, num2) -> float:
        return num1 / num2
    
    def operar(self, num1, operador, num2) -> float:
        return self.operadores[operador](num1, num2)

    def separar(self, expressao) -> list:
        result = []
        tmp = ''
        
        for elemento in expressao:
            if elemento.isdigit():
                tmp += elemento
            if elemento in self.operadores.keys():
                result.append(int(tmp))
                tmp = ''
                result.append(elemento)
        result.append(int(tmp))
        
        return result
    
    def resolver(self, expressaoSeparada) -> float:
        conta = expressaoSeparada.copy()
        while len(conta) > 1:
            if "*" in conta or "/" in conta:
                for index, elemento in enumerate(conta):
                    if elemento in self.oper1.keys():
                        tmp = []

                        tmp.append(conta.pop(index -1))
                        tmp.append(conta.pop(index -1))
                        tmp.append(conta.pop(index -1))
                
                        conta.insert(index-1, self.operar(*tmp))

            if "+" in conta or "-" in conta:
                for index, elemento in enumerate(conta):
                    if elemento in self.oper2.keys():
                        tmp = []

                        tmp.append(conta.pop(index -1))
                        tmp.append(conta.pop(index -1))
                        tmp.append(conta.pop(index -1))
                        
                        conta.insert(index-1, self.operar(*tmp))
            
        return conta.pop()
    
    def calcular(self, expressao) -> float:
        return self.resolver(self.separar(expressao))






if __name__ == "__main__":

    calc = Calculadora()

    expressao = input("Expressao: ")

    print(calc.calcular(expressao))
    
