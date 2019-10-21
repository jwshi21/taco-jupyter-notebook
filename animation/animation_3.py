import animation

data_matrix = [[6, "", 9, 8], ["", "", "", ""], [5, "", "", 7]]

data_columns = [('size', 'size', [4])]  
data_rows = [('pos_1', 'pos', [0, 2, 2, 3, 5]),
             ('idx_1', 'idx', [0, 2, 0, 0, 2])]
values = [('vals', 'vals', [6, 5, 9, 8, 7])]

labels = ['a00', 'a20', 'a02', 'a03', 'a23']
instructions = ['___0100', '___0111', '___2322', '___3433','___3444']

animation.display_animation('3', data_matrix, [data_columns, data_rows, values], labels, instructions)