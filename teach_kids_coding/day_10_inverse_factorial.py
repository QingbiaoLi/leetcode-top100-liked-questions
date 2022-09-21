# import pdb; pdb.set_trace() # [s]tep into function; [l]ist 11 lines; [w]here in stack; # [p]rint (exp/var);
                            # [b]reak at line no; [c]ontinue to break; [q]uit; [h]elp
from functools import lru_cache # cache since Python 3.9
from typing import List, Optional

class Problem:
    def __init__(self):
        pass

    @lru_cache
    def methodOne(self, n: int=0) -> int:
        if n == 1:
            return 1
        if n < 1:
            return -1
        i = 2
        s = 1
        while s < n:
            s = s * i
            i += 1
        return i - 1 if s == n else -1

    @lru_cache
    def methodTwo(self, n: int=0) -> int:
        if n == 1:
            return 1
        if n < 1:
            return -1
        i = 2
        s = 1
        while n > 1:
            if n % i != 0:
                return -1
            n = n // i
            i += 1
        return i - 1


    

def main():
    sol = Problem()
    # ans = sol.methodOne(24)
    ans = sol.methodTwo(15)

    # assert ans == -1
    print(ans)

if __name__ == "__main__":
    print('Template')
    main()