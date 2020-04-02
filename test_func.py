def border_print(text_inp):
    border_line = len(text_inp) * '#'
    text_out = f'''
###{border_line}###
#  {text_inp}  #
###{border_line}###
            '''
    return text_out


def mirror_print(text_inp):
    text_out = ''.join(reversed(text_inp))
    return text_out


text_inp = 'Hello World!'
print(mirror_print(text_inp))   # Вывожу текст зеркально
print(border_print(text_inp))   # Вывожу текст в рамке
print(border_print(mirror_print(text_inp)))  # Вывожу зеркальный тест в рамке

