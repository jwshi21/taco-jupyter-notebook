import animation

data_matrix = [[6, "", 9, 8], ["", "", "", ""], [5, "", "", 7]]

data_rows = [('pos_0', 'pos', [0, 2]),
             ('idx_0', 'idx', [0, 2])]
data_columns = [('pos_1', 'pos', [0, 3, 5]),
                ('idx_1', 'idx', [0, 2, 3, 0, 3])]  
values = [('vals', 'vals', [6, 9, 8, 5, 7])]

labels = ['a00', 'a02', 'a03', 'a20', 'a23']
instructions = ['0100100', '0100111', '0100122', '0111233', '0111244']

animation.display_animation('4', data_matrix, [data_rows, data_columns, values], labels, instructions)