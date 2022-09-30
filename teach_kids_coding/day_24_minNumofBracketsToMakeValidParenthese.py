# import pdb; pdb.set_trace() # [s]tep into function; [l]ist 11 lines; [w]here in stack; # [p]rint (exp/var);
                            # [b]reak at line no; [c]ontinue to break; [q]uit; [h]elp
from functools import lru_cache # cache since Python 3.9
from typing import List, Optional

class Problem:
    def __init__(self):
        pass

    # @lru_cache
    def methodOne(self, s):
        
        ans = 0
        bal = 0

        for i in s:
            if i == '(':
                bal += 1
            elif i == ')':
                bal -= 1
                if bal < 0:
                    bal = 0
                    ans += 1
        return ans + bal

    

def main():
    sol = Problem()
    data = '((())))'
    ans_1 = sol.methodOne(data)

    # assert ans == -1
    print(ans_1)

if __name__ == "__main__":
    print('Template')
    main()