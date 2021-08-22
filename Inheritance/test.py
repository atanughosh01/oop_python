
class OperateNumbers:
    
    def __init__(self):
        pass

    def get_squared_numbers(self, numbers: list) -> list:
        squared_numbers = []
        for n in numbers:
            squared_numbers.append(n*n)
        return squared_numbers


class OperateIntegers(OperateNumbers):
    
    def __init__(self):
        super().__init__()
        
    def calc_factorial(self, numbers: list) -> list:
        factorials = []
        for n in numbers:
            fact = 1
            while(n != 1):
                fact *= n
                n -= 1
            factorials.append(fact)
        return factorials


num_list = [2, 5, 8, 9, 6]
obj1 = OperateNumbers()
obj2 = OperateIntegers()

if __name__ == "__main__":
    squared_numlist = obj1.get_squared_numbers(num_list)
    factorial_list = obj2.calc_factorial(num_list)
    print("\nInput Number List\n->", num_list, 
          "\n\nSquared Number List\n->", squared_numlist,
          "\n\nFactorial List\n->", factorial_list)
