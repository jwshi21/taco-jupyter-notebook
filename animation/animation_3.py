import animation

data_matrix = [[6, 0, 9, 8], ["", "", "", ""], [5, 0, 0, 7]]

data_rows = [('pos_r', 'pos', [0, 2]),
             ('idx_r', 'idx', [0, 2])]
data_columns = [('size', 'size', [4])]  
values = [('vals', 'vals', [6, 0, 9, 8, 5, 0, 0, 7])]

labels = ['a00', 'a01', 'a02', 'a03', 'a20', 'a21', 'a22', 'a23']
instructions = ['010___0', '010___1', '010___2', '010___3', '011___4', '011___5', '011___6', '011___7']

animation.display_animation('3', data_matrix, [data_rows, data_columns, values], labels, instructions)