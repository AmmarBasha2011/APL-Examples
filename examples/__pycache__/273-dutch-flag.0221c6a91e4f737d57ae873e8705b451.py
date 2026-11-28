
# apl-source:1
# مثال 273 — مسألة العلم الهولندي
# apl-source:2
# Dutch national flag
# apl-source:3
# Demonstrates: فرز ثلاث فئات في مرور واحد
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/273-dutch-flag.apl
# apl-source:6

# apl-source:7
def علم(قائمة):
    # apl-source:8
    منخفض = 0
    # apl-source:9
    منتصف = 0
    # apl-source:10
    مرتفع = len(قائمة) - 1
    # apl-source:11
    while منتصف <= مرتفع:
        # apl-source:12
        if قائمة[منتصف] == 0:
            # apl-source:13
            مؤقت = قائمة[منخفض]
            # apl-source:14
            قائمة[منخفض] = قائمة[منتصف]
            # apl-source:15
            قائمة[منتصف] = مؤقت
            # apl-source:16
            منخفض = منخفض + 1
            # apl-source:17
            منتصف = منتصف + 1
        # apl-source:18
        elif قائمة[منتصف] == 1:
            # apl-source:19
            منتصف = منتصف + 1
        # apl-source:20
        else:
            # apl-source:21
            مؤقت = قائمة[منتصف]
            # apl-source:22
            قائمة[منتصف] = قائمة[مرتفع]
            # apl-source:23
            قائمة[مرتفع] = مؤقت
            # apl-source:24
            مرتفع = مرتفع - 1
    # apl-source:25
    return قائمة
# apl-source:26

# apl-source:27
print(علم([2, 0, 2, 1, 1, 0]))
# apl-source:28
print(علم([2, 0, 1]))
# apl-source:29
