# import pdb; pdb.set_trace() # [s]tep into function; [l]ist 11 lines; [w]here in stack; # [p]rint (exp/var);
                            # [b]reak at line no; [c]ontinue to break; [q]uit; [h]elp
from collections import defaultdict
from functools import lru_cache
from hashlib import shake_128 # cache since Python 3.9
from typing import Counter, List, Optional

class Problem:
    def __init__(self):
        pass

    @lru_cache
    def methodOne(self, s1, s2) -> int:
        d1 = defaultdict(int)
        d2 = defaultdict(int)
        for i in s1:
            d1[i] += 1
        for i in s2:
            d2[i] += 1
        return d1 == d2

    @lru_cache
    def methodTwo(self, s1, s2) -> int:
        d1 = Counter(s1)
        d2 = Counter(s2)
        return d1 == d2

        


    

def main():
    sol = Problem()
    s1 = 'listen'
    s2 = 'silen'

    ans_1 = sol.methodOne(s1, s2)
    ans_2 = sol.methodTwo(s1, s2)

    # assert ans == -1
    print(ans_1)
    print(ans_2)

if __name__ == "__main__":
    print('Template')
    main()