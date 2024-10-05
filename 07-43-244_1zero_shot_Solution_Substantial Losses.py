MOD = 998244353

def compute_expected_days(W, G, L):
    delta = (W - G) % MOD
    unit_expected_days = (2 * L + 1) % MOD
    total_expected_days = (delta * unit_expected_days) % MOD
    return total_expected_days

def main():
    import sys
    import threading
    def run():
        T = int(sys.stdin.readline())
        for case_num in range(1, T + 1):
            W_str, G_str, L_str = sys.stdin.readline().split()
            W = int(W_str)
            G = int(G_str)
            L = int(L_str)
            result = compute_expected_days(W, G, L)
            print(f"Case #{case_num}: {result}")
    threading.Thread(target=run).start()

if __name__ == "__main__":
    main()