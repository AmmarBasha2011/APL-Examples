
# apl-source:1
# مثال 370 — عد استدعاءات فيبوناتشي
# apl-source:2
# Count fibonacci calls
# apl-source:3
# Demonstrates: تكلفة العودية الساذجة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/370-fib-tree-count.apl
# apl-source:6

# apl-source:7
عداد = {"عدد": 0}
# apl-source:8

# apl-source:9
def فيب(ن):
    # apl-source:10
    عداد["عدد"] = عداد["عدد"] + 1
    # apl-source:11
    if ن < 2:
        # apl-source:12
        return ن
    # apl-source:13
    return فيب(ن - 1) + فيب(ن - 2)
# apl-source:14

# apl-source:15
print("فيب(10) =", فيب(10))
# apl-source:16
print("عدد الاستدعاءات:", عداد["عدد"])
# apl-source:17
