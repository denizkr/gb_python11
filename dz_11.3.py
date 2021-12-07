class Error:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):

        self.my_list = [int(i) for i in input('Enter values separated by a space: ').split()]
        val = int(input('Enter values and press Enter - '))
        self.my_list.append(val)

        while True:
            try:
                val = int(input('Enter values and press Enter - '))
                self.my_list.append(val)
                print(f'Current list - {self.my_list} \n ')
            except:
                print(f"Invalid val - string and boolean")
                y_or_n = input(f'Try again? Y/N ')

                if y_or_n == 'Y' or y_or_n == 'y':
                    print(try_except.my_input())
                elif y_or_n == 'N' or y_or_n == 'n':
                    return f'You got out'
                else:
                    return f'You got out'


try_except = Error(1)
print(try_except.my_input())
