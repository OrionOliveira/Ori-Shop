themes = {
    'Light': [1, 1, 1, 1],
    'Dark': [0.1, 0.1, 0.1, 1],
    'Blue': [0.1, 0.1, 1, 1],
    'Red': [1, 0.1, 0.1, 1]}

def theme(in_tema):
    if in_tema == 'light':
        tema_light = themes['Light']
        print("Você escolheu  o tema Light")
        return tema_light
    elif in_tema == 'dark':
        tema_dark = themes['Dark']
        print("Você escolheu  o tema Dark")
        return tema_dark
    elif in_tema == 'blue':
        tema_blue = themes['Blue']
        print("Você escolheu  o tema Blue")
        return tema_blue
    elif in_tema == 'red':
        tema_red = themes['Red']
        print("Você escolheu  o tema Red")
        return tema_red
