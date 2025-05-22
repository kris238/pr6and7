import enum
class OP(enum.Enum):
    plus = "+"
    minus = "-"
    multiply = "*"
    divide = "/"
def calcul(a, b, operation):
    r = 0
    match operation:
        case OP.plus:
            r = a + b
        case OP.minus:
            r = a - b
        case OP.multiply:
            r = a * b
        case OP.divide:
            if a != 0:
                r = a / b
    return a, b, operation.value, r
a = 10
b = 5
operation = OP.plus
print(calcul(a, b, operation))
