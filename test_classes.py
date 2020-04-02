class BorderPrint:  # этот класс обводит любой текст рамкой из символов #
    def __init__(self, text_inp):
        self.text_inp = text_inp
        border_line = len(text_inp) * '#'
        self.text_out = f'''
###{border_line}###
#  {self.text_inp}  #
###{border_line}###
        '''

    def cast(self):
        return self.text_out


class MirrorPrint:  # Этот класс зерклит любой текст
    def __init__(self, text_inp):
        self.text_inp = text_inp
        self.text_out = ''.join(reversed(self.text_inp))

    def cast(self):
        # print(self.text_out)
        return self.text_out


print(MirrorPrint('Hello Python!').cast())  # Текст выведет зеркально
print(BorderPrint('Hello Python').cast())  # Текст в рамке
print(BorderPrint(MirrorPrint('Hello Python!').cast()).cast())  # Текст в рамке и зеркально
