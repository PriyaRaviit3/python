import numpy as np
import matplotlib.pyplot as plt
plt.figure()

y=np.genfromtxt("E:\green java\diabetes.csv",delimiter=',',skip_header=1)
preg=y[:,0]
glu=y[:,1]

plt.plot(preg,glu)


output:

