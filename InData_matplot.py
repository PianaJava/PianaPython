#import libraries
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

#DataFrame
df = pd.read_csv("S809_1.dat", sep="\t", names= ["Ang", "CL", "CD", "CM"])
#export data
df.to_csv("out.xls")

#print on screen the first 5 lines
print(df.head(5))

#define the output graph
fig = plt.figure(1)
plt.plot(df.Ang,df.CL,"-g", label="CL")
plt.plot(df.Ang,df.CD, "-y", label="CD")
plt.plot(df.Ang,df.CM, "-b", label="CM")
fig.suptitle("Polars", fontsize=20)
plt.xlabel("Angle", fontsize = 18)
plt.ylabel("Adimensional Value", fontsize =18)
plt.legend()
#show the graph
plt.show()











