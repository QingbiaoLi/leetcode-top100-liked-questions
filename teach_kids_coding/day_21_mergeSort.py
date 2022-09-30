# import pdb; pdb.set_trace() # [s]tep into function; [l]ist 11 lines; [w]here in stack; # [p]rint (exp/var);
                            # [b]reak at line no; [c]ontinue to break; [q]uit; [h]elp
from functools import lru_cache # cache since Python 3.9
from typing import List, Optional
import random

class Problem:
    def __init__(self):
        pass

    # @lru_cache
    def methodOne(self, n):
        # quickSort
        if len(n) <= 1:
            return n
        
        pivot = random.choice(n)
        eq = [x for x in n if x == pivot]
        smaller = [x for x in n if x < pivot]
        larger = [x for x in n if x > pivot]
        return self.methodOne(smaller) + eq + self.methodOne(larger)
        
    def methodTwo(self, n):
        # quickSort
        if len(n) <= 1:
            return n
        
        pivot = random.choice(n)
        eq = []
        smaller = []
        larger = []
        for i in n:
            if i == pivot:
                eq.append(i)
            elif i < pivot:
                smaller.append(i)
            else:
                larger.append(i)
        return self.methodOne(smaller) + eq + self.methodOne(larger)
        
    

def main():
    sol = Problem()
    data = [3,3,2,1,6, 5]
    ans_1 = sol.methodTwo(data)

    # assert ans == -1
    print(ans_1)

if __name__ == "__main__":
    print('Template')
    main()