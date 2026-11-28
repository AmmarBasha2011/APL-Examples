
# apl-source:1
# مثال 309 — العوامل الأولية
# apl-source:2
# Prime factorization
# apl-source:3
# Demonstrates: القسمة المتكررة على العوامل
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/309-prime-factors.apl
# apl-source:6

# apl-source:7
def عوامل_أولية(عدد):
    # apl-source:8
    عوامل = []
    # apl-source:9
    قاسم = 2
    # apl-source:10
    while قاسم * قاسم <= عدد:
        # apl-source:11
        while عدد % قاسم == 0:
            # apl-source:12
            عوامل.append(قاسم)
            # apl-source:13
            عدد = عدد // قاسم
        # apl-source:14
        قاسم = قاسم + 1
    # apl-source:15
    if عدد > 1:
        # apl-source:16
        عوامل.append(عدد)
    # apl-source:17
    return عوامل
# apl-source:18

# apl-source:19
print("12 =", عوامل_أولية(12))
# apl-source:20
print("315 =", عوامل_أولية(315))
# apl-source:21
print("97 =", عوامل_أولية(97))
# apl-source:22
