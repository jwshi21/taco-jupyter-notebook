import matplotlib as mplt
import matplotlib.pyplot as plt

def convert(tensor, mask = True):
    temp = pt.to_array(tensor).reshape(tensor.shape[0], 1)
    if mask:
        return maskZero(temp)
    return temp

def maskZero(m): 
    return np.ma.masked_where(m == 0, m)

color_scheme = plt.cm.Blues
color_scheme.set_bad(color ='white') # Color zero values white. 
matrix = maskZero(sp.sparse.csr_matrix.toarray(sparse_matrix))
vector1 = convert(x)
vector2 = convert(z)

result = convert(y, False)

aspect_ratio = 0.3 * 20 / A.shape[0]

plt.gcf().set_size_inches(15, 15, forward=True)
gridspec = mplt.gridspec.GridSpec(1, 7, width_ratios = [6, 1, 1, 1, 1, 2, 1]) 

plt.subplot(gridspec[0])
plt.imshow(matrix, cmap = color_scheme)

plt.subplot(gridspec[2])
plt.imshow(vector1, cmap = color_scheme, aspect = aspect_ratio) 
plt.gca().axes.get_xaxis().set_visible(False)

plt.subplot(gridspec[4])
plt.imshow(vector2, cmap = color_scheme, aspect = aspect_ratio) 
plt.gca().axes.get_xaxis().set_visible(False)

plt.subplot(gridspec[6])
plt.imshow(result, cmap = 'Greens', aspect = aspect_ratio)
plt.gca().axes.get_xaxis().set_visible(False)
