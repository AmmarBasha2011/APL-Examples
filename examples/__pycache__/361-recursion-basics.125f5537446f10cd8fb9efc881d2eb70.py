
# apl-source:1
# مثال 361 — أساسيات العودية
# apl-source:2
# Recursion basics
# apl-source:3
# Demonstrates: عد تنازلي ومجموع وطباعة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/361-recursion-basics.apl
# apl-source:6

# apl-source:7
def عد_تنازلي(ن):
    # apl-source:8
    if ن == 0:
        # apl-source:9
        print("انتهى")
        # apl-source:10
        return
    # apl-source:11
    print(ن)
    # apl-source:12
    عد_تنازلي(ن - 1)
# apl-source:13

# apl-source:14
عد_تنازلي(3)
# apl-source:15

# apl-source:16
def مجموع_حتى(ن):
    # apl-source:17
    if ن == 0:
        # apl-source:18
        return 0
    # apl-source:19
    return ن + مجموع_حتى(ن - 1)
# apl-source:20

# apl-source:21
print("المجموع حتى 10:", مجموع_حتى(10))
# apl-source:22
