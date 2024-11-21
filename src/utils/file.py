import numpy as np

def load_mat(filepath):
    print('loading file on ', filepath)
    with open(filepath, 'r') as f:
        filtered = filter(lambda x: len(x.strip()), f.readlines())
        splitted = [list(map(float, row[:-2].split(','))) for row in filtered]
        result = np.array(splitted)

        print('successfully loaded mat with shape ', result.shape)
        return result
