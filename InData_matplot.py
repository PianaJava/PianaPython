import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

df = pd.read_csv("S809_1.dat", sep="\t", names= ["Ang", "CL", "CD", "CM"])
df.to_csv("out.xls")

print(df.head(5))

fig = plt.figure(1)
plt.plot(df.Ang,df.CL,"-g", label="CL")
plt.plot(df.Ang,df.CD, "-y", label="CD")
plt.plot(df.Ang,df.CM, "-b", label="CM")
fig.suptitle("Polars", fontsize=20)
plt.xlabel("Angle", fontsize = 18)
plt.ylabel("Adimensional Value", fontsize =18)
plt.legend()
plt.show()











