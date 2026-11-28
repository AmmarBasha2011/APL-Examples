
# apl-source:1
# مثال 208 — فيبوناتشي بالتخزين
# apl-source:2
# Fibonacci with memoization
# apl-source:3
# Demonstrates: عودية + قاموس حفظ
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/208-fibonacci-memo.apl
# apl-source:6

# apl-source:7
محفوظ = {}
# apl-source:8

# apl-source:9
def فيب(ن):
    # apl-source:10
    if ن < 2:
        # apl-source:11
        return ن
    # apl-source:12
    if ن in محفوظ:
        # apl-source:13
        return محفوظ[ن]
    # apl-source:14
    قيمة = فيب(ن - 1) + فيب(ن - 2)
    # apl-source:15
    محفوظ[ن] = قيمة
    # apl-source:16
    return قيمة
# apl-source:17

# apl-source:18
for ن in [10, 30, 50, 100]:
    # apl-source:19
    print("فيب(", ن, ") =", فيب(ن))
# apl-source:20

# apl-source:21
print("عناصر محفوظة:", len(محفوظ))
# apl-source:22
