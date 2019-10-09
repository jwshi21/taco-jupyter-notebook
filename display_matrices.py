import matplotlib as mplt
import matplotlib.pyplot as plt

matrix = sp.sparse.csr_matrix.toarray(sparse_matrix)
vector1 = pt.to_array(x).reshape(x.shape[0], 1)
vector2 = pt.to_array(z).reshape(z.shape[0], 1)
result = pt.to_array(y).reshape(y.shape[0], 1)

aspect_ratio = 0.3 * 20 / A.shape[0]

plt.gcf().set_size_inches(15, 15, forward=True)
gridspec = mplt.gridspec.GridSpec(1, 7, width_ratios = [6, 1, 1, 1, 1, 2, 1]) 

plt.subplot(gridspec[0])
plt.imshow(matrix, cmap = 'binary') 

plt.subplot(gridspec[2])
plt.imshow(vector1, cmap = 'Blues', aspect = aspect_ratio) 
plt.gca().axes.get_xaxis().set_visible(False)

plt.subplot(gridspec[4])
plt.imshow(vector2, cmap = 'Blues', aspect = aspect_ratio) 
plt.gca().axes.get_xaxis().set_visible(False)

plt.subplot(gridspec[6])
plt.imshow(result, cmap = 'Greens', aspect = aspect_ratio)
plt.gca().axes.get_xaxis().set_visible(False)
