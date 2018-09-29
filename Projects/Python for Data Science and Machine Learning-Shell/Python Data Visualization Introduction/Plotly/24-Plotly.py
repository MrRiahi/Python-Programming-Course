import numpy as np
import pandas as pd
from plotly import __version__
import cufflinks as cf
from plotly.offline import download_plotlyjs, init_notebook_mode, iplot
import matplotlib.pyplot as plt


print(__version__)

init_notebook_mode(connected = True)
cf.go_offline()


# Data
df = pd.DataFrame(np.random.randn(100,4), columns = 'A B C D'.split())
df.head()


df.iplot()


df.iplot(kind = 'bar')





