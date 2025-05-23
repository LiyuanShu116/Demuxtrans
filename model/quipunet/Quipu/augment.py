# Project Quipu - quipunet augmentation methods

import scipy.signal as signal
import numpy as np
import Quipu.tools


# def addNoise(xs, std = 0.05):
#     "Add gaussian noise"
#     return xs + np.random.normal(0, std, xs.shape)
def addNoise(xs, std=0.02):
    """Add Gaussian noise with reduced noise standard deviation."""
    return xs + np.random.normal(0, std, xs.shape)

# def stretchDuration(xs, std = 0.1, probability = 0.quipunet):
#     """
#     Augment the length by re-sampling. probability gives ratio of mutations
#     Slow method since it uses scipy
#
#     :param xs: input numpy quipunet structure
#     :param std: amound to mutate (drawn from normal distribution)
#     :param probability: probabi
#     """
#     x_new = np.copy(xs)
#     for i in range(len(xs)):
#         if np.random.rand() > probability:
#             x_new[i] = _mutateDurationTrace(x_new[i], std)
#     return x_new

def stretchDuration(xs, std=0.05, probability=0.5):
    """
    Augment the length by re-sampling, with a reduced standard deviation for stretching.
    The probability parameter gives the ratio of mutations.
    """
    x_new = np.copy(xs)
    for i in range(len(xs)):
        if np.random.rand() < probability:  # Adjusted to use < instead of >
            x_new[i] = _mutateDurationTrace(x_new[i], std)
    return x_new


def _mutateDurationTrace(x, std = 0.05):
    "adjust the sampling rate"
    length = len(x)
    return Quipu.tools.normaliseLength( signal.resample(x, int(length*np.random.normal(1, std))) , length = length)

def magnitude(xs, std = 0.1):
    "Baseline mutation"
    return xs * np.abs(np.random.normal(1, std, len(xs)).reshape((-1,1)) )
