
# apl-source:1
# مثال 429 — مجموعات منفصلة
# apl-source:2
# Union-Find
# apl-source:3
# Demonstrates: دمج واستعلام
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/429-union-find.apl
# apl-source:6

# apl-source:7
def جذر_مجموعة(أصل, عقدة):
    # apl-source:8
    while أصل[عقدة] != عقدة:
        # apl-source:9
        عقدة = أصل[عقدة]
    # apl-source:10
    return عقدة
# apl-source:11

# apl-source:12
def ادمج(أصل, أ, ب):
    # apl-source:13
    أصل[جذر_مجموعة(أصل, أ)] = جذر_مجموعة(أصل, ب)
# apl-source:14

# apl-source:15
أصل = {}
# apl-source:16
for ي in range(6):
    # apl-source:17
    أصل[ي] = ي
# apl-source:18

# apl-source:19
ادمج(أصل, 0, 1)
# apl-source:20
ادمج(أصل, 2, 3)
# apl-source:21
ادمج(أصل, 1, 2)
# apl-source:22

# apl-source:23
print("0 و 3 معا؟", جذر_مجموعة(أصل, 0) == جذر_مجموعة(أصل, 3))
# apl-source:24
print("0 و 4 معا؟", جذر_مجموعة(أصل, 0) == جذر_مجموعة(أصل, 4))
# apl-source:25
