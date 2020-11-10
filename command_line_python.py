import sys
import numpy as np

action = sys.argv[1]
filenames = sys.argv[2:]

for filename in filenames:
	data = np.loadtxt(filename, delimiter=',')
	if action == '--mean':
		print(np.mean(data))
	elif action == '--min':
		print(np.min(data))
	elif action == '--printname':
		print(filename)
	else:
		print('Action not recognised')
