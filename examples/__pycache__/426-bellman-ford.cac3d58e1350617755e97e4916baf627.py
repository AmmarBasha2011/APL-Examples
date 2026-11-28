
# apl-source:1
# مثال 426 — بيلمان فورد
# apl-source:2
# Bellman-Ford
# apl-source:3
# Demonstrates: مسارات بأوزان سالبة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/426-bellman-ford.apl
# apl-source:6

# apl-source:7
حواف = [[0, 1, 5], [0, 2, 4], [1, 2, -3], [2, 3, 2], [1, 3, 6]]
# apl-source:8
مسافات = {0: 0, 1: 999, 2: 999, 3: 999}
# apl-source:9

# apl-source:10
for _ in range(3):
    # apl-source:11
    for حافة in حواف:
        # apl-source:12
        if مسافات[حافة[0]] + حافة[2] < مسافات[حافة[1]]:
            # apl-source:13
            مسافات[حافة[1]] = مسافات[حافة[0]] + حافة[2]
# apl-source:14

# apl-source:15
print("المسافات من 0:", مسافات)
# apl-source:16
