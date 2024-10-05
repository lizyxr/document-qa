import sys
import threading

def main():
    import math
    T = int(sys.stdin.readline())
    INF = float('inf')
    for case_num in range(1, T + 1):
        N = int(sys.stdin.readline())
        V_min = 0.0
        V_max = INF
        impossible = False
        for i in range(1, N + 1):
            A_i_str, B_i_str = sys.stdin.readline().split()
            A_i = int(A_i_str)
            B_i = int(B_i_str)
            if B_i == 0 and i != 0:
                print(f"Case #{case_num}: -1")
                impossible = True
                # Read remaining input for this test case
                for _ in range(i + 1, N + 1):
                    sys.stdin.readline()
                break
            if B_i > 0:
                v_min_i = i / B_i
            else:
                v_min_i = 0.0  # B_i == 0 and i == 0
            if A_i > 0:
                v_max_i = i / A_i
            else:
                v_max_i = INF
            V_min = max(V_min, v_min_i)
            V_max = min(V_max, v_max_i)
        if not impossible:
            if V_min <= V_max:
                print(f"Case #{case_num}: {V_min:.10f}")
            else:
                print(f"Case #{case_num}: -1")

threading.Thread(target=main).start()