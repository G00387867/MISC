# IPython log file

get_ipython().run_line_magic('logstart', '')
import pandas as pd
df = pd.read_csv("http://www.biostat.jhsph.edu/~rpeng/useRbook/faithful.csv")
df
df.describe()
exit()
