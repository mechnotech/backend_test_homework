class BorderPrint:  # Тут это будет родительский класс
    def __init__(self, text_inp):
        self.text_inp = text_inp
        border_line = len(text_inp) * '#'
        self.text_out = f'''
        ###{border_line}###
        #  {self.text_inp}  #
        ###{border_line}###
        '''

    def cast(self):  # возвращаю результат чере метод .cast()
        return self.text_out


class MirrorPrint(BorderPrint):  # Этот класс будет дочерним
    def __init__(self, text_inp):
        super().__init__(text_inp)
        self.text_out = ''.join(reversed(super().cast()))

    def cast(self):  # возвращаю результат чере метод .cast()
        # print(self.text_out)
        return self.text_out


text_inp = 'Hello world!'
print(BorderPrint(text_inp).cast())
print(MirrorPrint(text_inp).cast())
