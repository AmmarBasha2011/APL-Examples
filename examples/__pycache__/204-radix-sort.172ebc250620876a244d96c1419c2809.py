
# apl-source:1
# مثال 204 — الترتيب الجذري
# apl-source:2
# Radix sort (LSD)
# apl-source:3
# Demonstrates: الترتيب بالخانات، سلال
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/204-radix-sort.apl
# apl-source:6

# apl-source:7
def جذري(قائمة):
    # apl-source:8
    خانة = 1
    # apl-source:9
    أكبر = sorted(قائمة)[-1]
    # apl-source:10
    while أكبر // خانة > 0:
        # apl-source:11
        سلال = []
        # apl-source:12
        for _ in range(10):
            # apl-source:13
            سلال.append([])
        # apl-source:14
        for ع in قائمة:
            # apl-source:15
            سلال[(ع // خانة) % 10].append(ع)
        # apl-source:16
        جديدة = []
        # apl-source:17
        for سلة in سلال:
            # apl-source:18
            for ع in سلة:
                # apl-source:19
                جديدة.append(ع)
        # apl-source:20
        قائمة = جديدة
        # apl-source:21
        خانة = خانة * 10
    # apl-source:22
    return قائمة
# apl-source:23

# apl-source:24
أرقام = [170, 45, 75, 90, 2, 802, 24, 66]
# apl-source:25
print("قبل:", أرقام)
# apl-source:26
print("بعد:", جذري(أرقام))
# apl-source:27
