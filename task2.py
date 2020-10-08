'''2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.'''

with open('second.txt', 'w', encoding='utf-8') as f:
    f.writelines('Несколько строк\n для подсчета\n количества\n строк и слов\n в каждой строке')

f = open('second.txt', 'r', encoding='utf-8')
for line, value in enumerate(f.readlines(), 1):
    print(f'В {line}й строке {len(value.split())} слова')
print(f'Общее количество строк составит: {line} ')
f.close()
