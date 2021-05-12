# sine and cos wave

import matplotlib.pyplot as pl
import numpy as np

x = np.linspace(-np.pi, np.pi, 256, endpoint=True)
y = np.cos(x)
y1 = np.sin(x)

pl.plot(x, y)
pl.plot(x, y1)
pl.xlabel('x values from -pi to pi')  # string must be enclosed with quotes '  '
pl.ylabel('sin(x) and cos(x)')
pl.title('Plot of sin and cos from -pi to pi')
pl.legend(['sin(x)', 'cos(x)'])  # legend entries as separate strings in a list
pl.show()

x = np.arange(0, 4 * np.pi - 1, 0.1)  # start,stop,step
y = np.sin(x)
z = np.cos(x)

pl.plot(x, y, x, z)
pl.xlabel('x values from 0 to 4pi')  # string must be enclosed with quotes '  '
pl.ylabel('sin(x) and cos(x)')
pl.title('Plot of sin and cos from 0 to 4pi')
pl.legend(['sin(x)', 'cos(x)'])  # legend entries as separate strings in a list
pl.show()
