
# apl-source:1
# مثال 400 — احتمالات بسيطة
# apl-source:2
# Simple probabilities
# apl-source:3
# Demonstrates: توزيع نتائج حجرتين نرد
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/400-chi-square.apl
# apl-source:6

# apl-source:7
تكرار = {}
# apl-source:8
for أ in range(1, 7):
    # apl-source:9
    for ب in range(1, 7):
        # apl-source:10
        مجموع_نرد = أ + ب
        # apl-source:11
        قديم = تكرار.get(مجموع_نرد, 0)
        # apl-source:12
        تكرار[مجموع_نرد] = قديم + 1
# apl-source:13

# apl-source:14
print("توزيع مجموع نردين:")
# apl-source:15
for مجموع_نرد in range(2, 13):
    # apl-source:16
    احتمال = تكرار[مجموع_نرد] / 36 * 100
    # apl-source:17
    print(مجموع_نرد, "->", str(احتمال) + "%")
# apl-source:18
