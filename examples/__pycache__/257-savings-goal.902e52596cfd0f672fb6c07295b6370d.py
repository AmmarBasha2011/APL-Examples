
# apl-source:1
# مثال 257 — هدف الادخار
# apl-source:2
# Savings goal planner
# apl-source:3
# Demonstrates: أشهر الوصول للهدف
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/257-savings-goal.apl
# apl-source:6

# apl-source:7
def أشهر_الوصول(هدف, شهري, نسبة_سنوية):
    # apl-source:8
    رصيد = 0
    # apl-source:9
    أشهر = 0
    # apl-source:10
    ر = نسبة_سنوية / 100 / 12
    # apl-source:11
    while رصيد < هدف and أشهر < 1200:
        # apl-source:12
        رصيد = رصيد * (1 + ر) + شهري
        # apl-source:13
        أشهر = أشهر + 1
    # apl-source:14
    return [أشهر, round(رصيد, 2)]
# apl-source:15

# apl-source:16
ن = أشهر_الوصول(50000, 1000, 4)
# apl-source:17
print("للوصول إلى 50000 ادخارا:", ن[0], "شهرا")
# apl-source:18
print("الرصيد حينها:", ن[1])
# apl-source:19
print("أي حوالي", round(ن[0] / 12, 1), "سنة")
# apl-source:20
