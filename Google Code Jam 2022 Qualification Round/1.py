def solution():
    def solve():
        R, C = input().split()
        R, C = int(R), int(C)
        print(".." + "+-"*(C-1) + "+")
        print("." + ".|"*C)
        for _ in range(R-1):
            print("+-"*C + "+")
            print("|."*C + "|")
        print("+-"*C + "+")
        return

    for T in range(1,1+int(input())):
        solve()
        print("Case #%d:" % T)

solution()
