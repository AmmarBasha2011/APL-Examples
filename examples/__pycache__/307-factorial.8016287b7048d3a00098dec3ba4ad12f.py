
# apl-source:1
# مثال 307 — العاملي (مضروب العدد)
# apl-source:2
# Factorial
# apl-source:3
# Demonstrates: تكراري وعودي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/307-factorial.apl
# apl-source:6

# apl-source:7
def عاملي_تكراري(ن):
    # apl-source:8
    نتيجة = 1
    # apl-source:9
    for ي in range(2, ن + 1):
        # apl-source:10
        نتيجة = نتيجة * ي
    # apl-source:11
    return نتيجة
# apl-source:12

# apl-source:13
def عاملي_عودي(ن):
    # apl-source:14
    if ن <= 1:
        # apl-source:15
        return 1
    # apl-source:16
    return ن * عاملي_عودي(ن - 1)
# apl-source:17

# apl-source:18
print("5! =", عاملي_تكراري(5))
# apl-source:19
print("10! =", عاملي_عودي(10))
# apl-source:20
print("20! =", عاملي_تكراري(20))
# apl-source:21
