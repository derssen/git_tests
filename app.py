total_protocols = int(input('Сколько записей вносится в протокол? '))
notes = []
scores = {}
best_score = 0
best_name = ''

print('Записи (результат и имя):')
for i_num in range(total_protocols):
    score, nickname = input(f'{i_num + 1}--я запись: ').split()
    notes.append([nickname, int(score)])

for i in range(1, 4):
    for i_name, i_sco in notes:
        if i_sco > best_score:
            scores[i] = {i_name: i_sco}
            best_name = i_name
            best_score = i_sco
    for i_name_delete, i_sco_delete in notes:
        if i_name_delete == best_name:
            notes.remove([i_name_delete, i_sco_delete])
    best_score = 0

for i_place, i_result in scores.items():
    for i_n, i_s in i_result.items():
        print(f'{i_place}-е место. {i_n} ({i_s})')

print('Протокол заполнен!.')
print('-----')
