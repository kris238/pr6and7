class Calculation:
    def __init__(self, calculationLine=0):
        self.calculationLine = calculationLine
    def SetCalculationLine(self, a):
        self.calculationLine = a
    def SetLastSymbolCalculationLine(self, b):
        self.calculationLine += b
    def GetCalculationLine(self):
        return self.calculationLine
    def GetLastSymbol(self):
        if self.calculationLine:
            return self.calculationLine[-1]
    def DeleteLastSymbol(self):
        if self.calculationLine:
            self.calculationLine = self.calculationLine[:-1]
calc = Calculation()
calc.SetCalculationLine("241")
print(calc.GetCalculationLine())
calc.SetLastSymbolCalculationLine("7")
print(calc.GetCalculationLine())
print(calc.GetLastSymbol())
calc.DeleteLastSymbol()
print(calc.GetCalculationLine())
