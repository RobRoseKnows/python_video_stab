import unittest
import numpy as np
import vidstab.utils as utils


class UtilTests(unittest.TestCase):
    def test_bfill_rolling_mean(self):
        test_arr = np.array([[1, 2, 3], [4, 5, 6]])

        self.assertTrue(np.allclose(utils.bfill_rolling_mean(test_arr, n=1), test_arr))
        self.assertTrue(np.allclose(utils.bfill_rolling_mean(test_arr, n=2),
                                    np.array([[2.5, 3.5, 4.5],
                                              [2.5, 3.5, 4.5]])))

        with self.assertRaises(ValueError) as err:
            utils.bfill_rolling_mean(test_arr, n=3)
        self.assertTrue(isinstance(err.exception, ValueError), 'reject when n > arr.shape[0]')


if __name__ == '__main__':
    unittest.main()
