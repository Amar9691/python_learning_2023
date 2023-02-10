import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
pd.options.display.max_rows = 9999
myvar = pd.read_csv('data.csv')
myvar.plot(kind="scatter",x='Duration',y='Pulse')
plt.show()

#Amar89@!^&*78