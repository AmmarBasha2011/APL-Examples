
# apl-source:1
# مثال 409 — منطق أربعة تربح
# apl-source:2
# Connect four logic
# apl-source:3
# Demonstrates: فحص أربعة في صف
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/409-connect-four.apl
# apl-source:6

# apl-source:7
def فائز_أفقي(شبكة):
    # apl-source:8
    for سطر in شبكة:
        # apl-source:9
        for ي in range(len(سطر) - 3):
            # apl-source:10
            if سطر[ي] != "-" and سطر[ي] == سطر[ي + 1] and سطر[ي + 1] == سطر[ي + 2] and سطر[ي + 2] == سطر[ي + 3]:
                # apl-source:11
                return سطر[ي]
    # apl-source:12
    return "-"
# apl-source:13

# apl-source:14
شبكة = [
    # apl-source:15
    ["-", "-", "-", "-", "-", "-"],
    # apl-source:16
    ["-", "-", "-", "-", "-", "-"],
    # apl-source:17
    ["أ", "أ", "أ", "أ", "-", "-"]
# apl-source:18
]
# apl-source:19
print("الفائز:", فائز_أفقي(شبكة))
# apl-source:20
