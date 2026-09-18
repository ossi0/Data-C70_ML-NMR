import numpy as np

sig_list = np.loadtxt('./0/sig.txt', usecols=0)
print(f'Sigma average: {np.mean(sig_list):.3f} pm {(np.std(sig_list)/len(sig_list)**(1/2)):.3f}')
