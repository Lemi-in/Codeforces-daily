import sys

def query(i):
    print(f"? {i}", flush=True)
    try:
        s = input()
    except EOFError:
        sys.exit("❌ Interactor did not return any input (likely due to wrong query or idleness).")
    if s == "-1":
        sys.exit("❌ Interactor rejected due to too many or invalid queries.")
    if not s:
        sys.exit("❌ Received empty string — likely a flush/input mismatch or interactor error.")
    return s


def main():
    try:
        n, h = input().split()
        n = int(n)
    except:
        sys.exit("❌ Failed to read initial input (n and h).")

    s1 = query(1)
    sn = query(n)

    # Safely check casing
    if len(s1) == 0 or len(sn) == 0:
        sys.exit("❌ Empty string received for s1 or sn. Something's wrong.")

    if s1[0].isupper() and sn[0].islower():
        is_upper_first = True
    elif s1[0].islower() and sn[0].isupper():
        is_upper_first = False
    else:
        # fallback: compare h to s1
        is_upper_first = h < s1

    # Binary search
    l, r = 1, n
    while l <= r:
        mid = (l + r) // 2
        smid = query(mid)
        if smid == h:
            print(f"! {mid}", flush=True)
            return
        if is_upper_first:
            if h < smid:
                r = mid - 1
            else:
                l = mid + 1
        else:
            if h < smid:
                r = mid - 1
            else:
                l = mid + 1

main()
