
# apl-source:1
# مثال 319 — المعكوس الضربي التراكبي
# apl-source:2
# Modular multiplicative inverse
# apl-source:3
# Demonstrates: خوارزمية إقليدس الممتدة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/319-modular-inverse.apl
# apl-source:6

# apl-source:7
def معكوس_تراكبي(أ, م):
    # apl-source:8
    م0 = م
    # apl-source:9
    س = 1
    # apl-source:10
    ص = 0
    # apl-source:11
    while أ > 1:
        # apl-source:12
        خارج = أ // م
        # apl-source:13
        مؤقت = م
        # apl-source:14
        م = أ % م
        # apl-source:15
        أ = مؤقت
        # apl-source:16
        مؤقت = ص
        # apl-source:17
        ص = س - خارج * ص
        # apl-source:18
        س = مؤقت
    # apl-source:19
    if س < 0:
        # apl-source:20
        س = س + م0
    # apl-source:21
    return س
# apl-source:22

# apl-source:23
print("معكوس 3 mod 11 =", معكوس_تراكبي(3, 11))
# apl-source:24
print("تحقق: 3 × 4 mod 11 =", (12) % 11)
# apl-source:25
print("معكوس 10 mod 17 =", معكوس_تراكبي(10, 17))
# apl-source:26
