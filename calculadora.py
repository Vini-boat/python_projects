class Calculadora():
    def __init__(self) -> None:
        
        self.ordem_operadores = {
            0: {
                '*': self.multiplicar,
                '/': self.dividir
                },
            1: {
                '+': self.somar,
                '-': self.subtrair
            }
        }

        self.operadores = {}
        for d in self.ordem_operadores.values():
            self.operadores.update(d)



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
            for d in self.ordem_operadores:
                k = list(self.ordem_operadores[d].keys())
                while k[0] in conta or k[1] in conta:
                    for index, elemento in enumerate(conta):
                        if elemento in k:
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

    expressao = input('Espressão: ')

    print(calc.calcular(expressao))
    
