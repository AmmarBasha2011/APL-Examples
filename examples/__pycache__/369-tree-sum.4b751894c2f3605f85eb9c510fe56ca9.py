
# apl-source:1
# مثال 369 — مجموع شجرة بالعودية
# apl-source:2
# Recursive tree sum
# apl-source:3
# Demonstrates: جمع على بنية متداخلة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/369-tree-sum.apl
# apl-source:6

# apl-source:7
def مجموع_شجرة(عقدة):
    # apl-source:8
    if عقدة == None:
        # apl-source:9
        return 0
    # apl-source:10
    return عقدة["قيمة"] + مجموع_شجرة(عقدة["أيسر"]) + مجموع_شجرة(عقدة["أيمن"])
# apl-source:11

# apl-source:12
شجرة = {
    # apl-source:13
    "قيمة": 10,
    # apl-source:14
    "أيسر": {"قيمة": 5, "أيسر": None, "أيمن": None},
    # apl-source:15
    "أيمن": {"قيمة": 20, "أيسر": None, "أيمن": None}
# apl-source:16
}
# apl-source:17
print("مجموع الشجرة:", مجموع_شجرة(شجرة))
# apl-source:18
