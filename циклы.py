import time
print('▒▒▒▒▒▒▒▒▒▒▒▒')
print('  by r0w_')
print('▒▒▒▒▒▒▒▒▒▒▒▒')
print('')
a = input('Установить Grand Theft Auto V? Y/N? ')
if a == ('Y') or ('y'):
    i = 1
    while i<=100:
        print(str(i) + '%')
        i = i+1
        time.sleep(0.5)
    print('┌----------------------------┐')
    print('|Установка успешно завершена!|')
    print('└----------------------------┘')
    input('Нажми ENTER чтобы продолжить...')
elif a == ('N') or ('n'):
    print('Установка успешно прервана. Спасибо пользуетесь Installer от r0w_.')
    input('Нажми ENTER чтобы продолжить...')
else:
    print('Неизвестная команда.')
    input('Нажми ENTER чтобы продолжить...')
