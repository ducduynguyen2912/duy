def main():
    n = int(input())
    s = []
    for _ in range(n):
        d = input().split()
        a = d[0]
        b = int(d[1])
        c = float(d[2])
        e = float(d[3])
        f = float(d[4])
        g = round((c + e + f) / 3, 2)
        s.append({"a": a, "b": b, "c": c, "e": e, "f": f, "g": g})
    r = []
    for x in s:
        h = 0
        if x["c"] < 4.0:
            h += 1
        if x["e"] < 4.0:
            h += 1
        if x["f"] < 4.0:
            h += 1
        if h >= 2:
            r.append(x)
    print("Danh sach sinh vien hoc lai")
    for x in r:
        print(f"{x['b']} {x['a']} {x['c']:.2f} {x['e']:.2f} {x['f']:.2f} {x['g']:.2f}")
    print(f"Danh sach nay co {len(r)} sinh vien phai hoc lai")

if __name__ == "__main__":
    main()
