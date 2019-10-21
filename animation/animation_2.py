import animation

data_matrix = [[6, "", 9, 8], ["", "", "", ""], [5, "", "", 7]]

data_rows = [('size', 'size', [3])]
data_columns = [('pos_1', 'pos', [0, 3, 3, 5]),
                ('idx_1', 'idx', [0, 2, 3, 0, 3])]  
values = [('vals', 'vals', [6, 9, 8, 5, 7])]

labels = ['a00', 'a02', 'a03', 'a20', 'a23']
instructions = ['___0100', '___0111', '___0122', '___2333', '___2344']

animation.display_animation('2', data_matrix, [data_rows, data_columns, values], labels, instructions)