# import pdb; pdb.set_trace() # [s]tep into function; [l]ist 11 lines; [w]here in stack; # [p]rint (exp/var);
                            # [b]reak at line no; [c]ontinue to break; [q]uit; [h]elp
from functools import lru_cache # cache since Python 3.9
from typing import List, Optional

class Problem:
    def __init__(self):
        pass

    # @lru_cache
    def methodOne(self, n, s, nb=set()):
        
        if n[s] == 0:
            return True
        
        for i in [-1, 1]:
            next = s + i*n[s]
            if next >= 0 and next < len(n) and next not in nb:
                nb.add(next)
                if self.methodOne(n, next, nb):
                    return True
        return False

    

def main():
    sol = Problem()
    data = [2, 0, 3, 1, 3, 4]
    ans_1 = sol.methodOne(data, 3)

    # assert ans == -1
    print(ans_1)

if __name__ == "__main__":
    print('Template')
    main()