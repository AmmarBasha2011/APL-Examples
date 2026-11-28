
# apl-source:1
# مثال 286 — فأر في متاهة
# apl-source:2
# Rat in a maze
# apl-source:3
# Demonstrates: تراجع على شبكة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/286-rat-maze.apl
# apl-source:6

# apl-source:7
def جد_طريق(متاهة, س, ص, مسار, ن):
    # apl-source:8
    if س == ن - 1 and ص == ن - 1 and متاهة[س][ص] == 1:
        # apl-source:9
        مسار[س][ص] = 1
        # apl-source:10
        return True
    # apl-source:11
    if س < 0 or ص < 0 or س >= ن or ص >= ن:
        # apl-source:12
        return False
    # apl-source:13
    if متاهة[س][ص] == 0 or مسار[س][ص] == 1:
        # apl-source:14
        return False
    # apl-source:15
    مسار[س][ص] = 1
    # apl-source:16
    if جد_طريق(متاهة, س + 1, ص, مسار, ن):
        # apl-source:17
        return True
    # apl-source:18
    if جد_طريق(متاهة, س, ص + 1, مسار, ن):
        # apl-source:19
        return True
    # apl-source:20
    مسار[س][ص] = 0
    # apl-source:21
    return False
# apl-source:22

# apl-source:23
متاهة = [
    # apl-source:24
    [1, 0, 0, 0],
    # apl-source:25
    [1, 1, 0, 1],
    # apl-source:26
    [0, 1, 0, 0],
    # apl-source:27
    [1, 1, 1, 1]
# apl-source:28
]
# apl-source:29
ن = 4
# apl-source:30
مسار = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
# apl-source:31
if جد_طريق(متاهة, 0, 0, مسار, ن):
    # apl-source:32
    for صف in مسار:
        # apl-source:33
        print(صف)
# apl-source:34
else:
    # apl-source:35
    print("لا طريق")
# apl-source:36
