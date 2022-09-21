# import pdb; pdb.set_trace() # [s]tep into function; [l]ist 11 lines; [w]here in stack; # [p]rint (exp/var);
                            # [b]reak at line no; [c]ontinue to break; [q]uit; [h]elp
from functools import lru_cache # cache since Python 3.9
from typing import List, Optional

class Problem:
    def __init__(self):
        pass

    # @lru_cache
    def gcd(self, a, b):
        while b > 0:
            a, b = b, a % b
        return a
    
    def lcm(self, a, b):
        return a * b // self.gcd(a, b)



    

def main():
    sol = Problem()
    # ans = sol.methodOne(24)
    ans_gcd = sol.gcd(25, 35)
    ans_lcm = sol.lcm(25, 35)

    # assert ans == -1
    print(ans_gcd)
    print(ans_lcm)

if __name__ == "__main__":
    print('Template')
    main()