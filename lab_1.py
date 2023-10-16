from prettytable import PrettyTable
name = ['x', 'y', 'z', '!x', '!y', '!z', '!x∨!y', 'z→(!x∨!y)', '(z→(!x∨!y))→!z', 'x↔y', '(x↔y)↔((z→(!x∨!y))→!z)', 'x∨y', '((x↔y)↔((z→(!x∨!y))→!z))↔(x∨y)']
q = [[True, True, True],
     [True, True, False],
     [True, False, True],
     [True, False, False],
     [False, True, True],
     [False, True, False],
     [False, False, True],
     [False, False, False]]
table = PrettyTable(name)
for i in q:
    i.append(not (i[0]))
    i.append(not (i[1]))
    i.append(not (i[2]))
    i.append((i[3]+i[4]) > 0)
    i.append(not(i[2] > i[6]))
    i.append(not(i[6] > i[5]))
    i.append(i[0] == i[1])
    i.append(i[8] == i[9])
    i.append((i[0] + i[1]) > 0)
    i.append(i[10] == i[11])
    table.add_row(i)
print(table)
