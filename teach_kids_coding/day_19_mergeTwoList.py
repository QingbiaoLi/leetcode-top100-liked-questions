# import pdb; pdb.set_trace() # [s]tep into function; [l]ist 11 lines; [w]here in stack; # [p]rint (exp/var);
                            # [b]reak at line no; [c]ontinue to break; [q]uit; [h]elp
from functools import lru_cache # cache since Python 3.9
from typing import List, Optional

class Problem:
    def __init__(self):
        pass

    # @lru_cache
    def methodOne(self, a, b):
        
        c = []
        i, j, la, lb = 0, 0, len(a), len(b)

        while i < la and j < lb:
            if a[i] < b[j]:
                # c.append(a[i])
                c += [a[i]]
                i += 1
            else:
                c += [b[j]]
                # c.append(b[j])
                j += 1

            # while i <la:
            #     # c.append(a[i])
            #     c += [a[i]]
            #     i += 1
            # while i < lb:
            #     # c.append(b[j])
            #     c += [b[j]]
            #     j += 1
        return c + a[i:] + b[j:]

    def methodTwo(self, a, b):
        c = []
        i, j, la, lb = 0, 0, len(a), len(b)

        while i < la and j < lb:
            while i <la:
                # c.append(a[i])
                c += [a[i]]
                i += 1
            while j < lb:
                # c.append(b[j])
                c += [b[j]]
                j += 1
        return c 

    

def main():
    sol = Problem()
    a = [1,3, 4, 5, 7, 9]
    b = [2, 4, 6, 8]
    ans_1 = sol.methodOne(a, b)

    # ans_1 = sol.methodTwo(a, b)

    # assert ans == -1
    print(ans_1)

if __name__ == "__main__":
    print('Template')
    main()