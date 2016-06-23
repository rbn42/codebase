import scipy.misc
import numpy as np
i = np.zeros((480, 540, 3), dtype='uint8')
scipy.misc.imsave('./out.png', i)
print('end')
