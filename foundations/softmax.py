import numpy as np
from numpy.typing import NDArray


class Solution:

    def softmax(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        maximum=max(z)
        new=np.subtract(z,maximum)
        new_exp=np.exp(new)
        sum=0
        for i in new_exp:
            sum+=i
        new_arr=np.divide(new_exp,sum)
        return np.round(new_arr,4)
