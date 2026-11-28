
# apl-source:1
# مثال 365 — مجموع الأرقام بالعودية
# apl-source:2
# Recursive digit sum
# apl-source:3
# Demonstrates: قسمة وباقي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/365-sum-digits-rec.apl
# apl-source:6

# apl-source:7
def مجموع_أرقام(عدد):
    # apl-source:8
    if عدد == 0:
        # apl-source:9
        return 0
    # apl-source:10
    return عدد % 10 + مجموع_أرقام(عدد // 10)
# apl-source:11

# apl-source:12
print("12345 ->", مجموع_أرقام(12345))
# apl-source:13
print("999 ->", مجموع_أرقام(999))
# apl-source:14
