
# apl-source:1
# مثال 187 — الترتيب السريع
# apl-source:2
# Quick sort
# apl-source:3
# Demonstrates: العودية، المحور، توليدات القوائم
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/187-quick-sort.apl
# apl-source:6

# apl-source:7
def سريع(قائمة):
    # apl-source:8
    if len(قائمة) <= 1:
        # apl-source:9
        return قائمة
    # apl-source:10
    محور = قائمة[0]
    # apl-source:11
    أصغر_من = [ع for ع in قائمة[1:] if ع <= محور]
    # apl-source:12
    أكبر_من = [ع for ع in قائمة[1:] if ع > محور]
    # apl-source:13
    return سريع(أصغر_من) + [محور] + سريع(أكبر_من)
# apl-source:14

# apl-source:15
أرقام = [10, 7, 8, 9, 1, 5]
# apl-source:16
print("قبل:", أرقام)
# apl-source:17
print("بعد:", سريع(أرقام))
# apl-source:18
