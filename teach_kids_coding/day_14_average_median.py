# import pdb; pdb.set_trace() # [s]tep into function; [l]ist 11 lines; [w]here in stack; # [p]rint (exp/var);
                            # [b]reak at line no; [c]ontinue to break; [q]uit; [h]elp
from functools import lru_cache # cache since Python 3.9
from typing import List, Optional

class Problem:
    def __init__(self):
        pass

    # @lru_cache
    # def methodAverage(self, nums:List[int]) -> Optional[int]:
    def methodAverage(self, nums) :
        # print(nums)
        s = 0
        for n in nums:
            s += n
        return s / len(nums)

    # @lru_cache
    def methodMedian(self, nums):
        sz = len(nums)
        if sz % 2 == 1:
            return nums[sz // 2]
        return (nums[sz // 2] + nums[sz // 2 - 1]) / 2




    

def main():
    sol = Problem()
    data = [1, 2, 3, 4, 5]
    ans_average = sol.methodAverage(data)
    ans_median = sol.methodMedian(data)

    # assert ans == -1
    print(ans_average)
    print(ans_median)

if __name__ == "__main__":
    print('Template')
    main()