# import pdb; pdb.set_trace() # [s]tep into function; [l]ist 11 lines; [w]here in stack; # [p]rint (exp/var);
                            # [b]reak at line no; [c]ontinue to break; [q]uit; [h]elp
from functools import lru_cache # cache since Python 3.9
from typing import List, Optional

class Problem:
    def __init__(self):
        pass

    @lru_cache
    def methodOne(self, n: int=0) -> int:
        ans = 0
        while n > 0:
            ans += n % 10
            n = n // 10
        return ans

    @lru_cache
    def methodTwo(self, n: int=0) -> int:
        if n == 0:
            return 0
        return n % 10 + self.methodTwo(n // 10)


    

def main():
    sol = Problem()
    data = 123
    ans_1 = sol.methodOne(data)
    ans_2 = sol.methodTwo(data)

    # assert ans == -1
    print(ans_1)
    print(ans_2)

if __name__ == "__main__":
    print('Template')
    main()