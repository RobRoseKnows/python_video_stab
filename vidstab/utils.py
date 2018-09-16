import numpy as np

def bfill_rolling_mean(arr, n=30):
    """Helper to perform trajectory smoothing

    :param arr: Numpy array of frame trajectory to be smoothed
    :param n: window size for rolling mean
    :return: smoothed input arr

    >>> arr = np.array([[1, 2, 3], [4, 5, 6]])
    >>> bfill_rolling_mean(arr, n=2)
    array([[ 2.5,  3.5,  4.5],
           [ 2.5,  3.5,  4.5]])
    """
    if arr.shape[0] < n:
        raise ValueError('arr.shape[0] cannot be less than n')
    if n == 1:
        return arr

    pre_buffer = np.zeros(3).reshape(1, 3)
    post_buffer = np.zeros(3 * n).reshape(n, 3)
    arr_cumsum = np.cumsum(np.vstack((pre_buffer, arr, post_buffer)), axis=0)
    buffer_roll_mean = (arr_cumsum[n:, :] - arr_cumsum[:-n, :]) / float(n)
    trunc_roll_mean = buffer_roll_mean[:-n, ]

    bfill_size = arr.shape[0] - trunc_roll_mean.shape[0]
    bfill = np.tile(trunc_roll_mean[0, :], (bfill_size, 1))

    return np.vstack((bfill, trunc_roll_mean))
