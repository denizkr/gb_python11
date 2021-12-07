class MyZeroDivisionError(ZeroDivisionError):

    def init(self, txt):
        self.txt = txt


if __name__ == '__main__':
    try:
        numb_1 = int(input('enter the numerator: '))
        numb_2 = int(input('enter the denominator: '))
        if numb_2 == 0:
            raise MyZeroDivisionError('entering zero is not allowed')
    except MyZeroDivisionError as z:
        print(z)
    else:
        result = numb_1 / numb_2

print(f'{result}')
