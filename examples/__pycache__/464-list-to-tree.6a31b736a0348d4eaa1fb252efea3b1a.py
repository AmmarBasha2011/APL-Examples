
# apl-source:1
# مثال 464 — بناء شجرة من قائمة مسطحة
# apl-source:2
# Flat list to tree
# apl-source:3
# Demonstrates: عناصر بآباء
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/464-list-to-tree.apl
# apl-source:6

# apl-source:7
عناصر = [
    # apl-source:8
    {"م": 1, "أب": 0, "اسم": "جذر"},
    # apl-source:9
    {"م": 2, "أب": 1, "اسم": "فرع أ"},
    # apl-source:10
    {"م": 3, "أب": 1, "اسم": "فرع ب"},
    # apl-source:11
    {"م": 4, "أب": 2, "اسم": "ورقة"}
# apl-source:12
]
# apl-source:13

# apl-source:14
def اطبع_شجرة(عناصر, أب, مسافة):
    # apl-source:15
    for عنصر in عناصر:
        # apl-source:16
        if عنصر["أب"] == أب:
            # apl-source:17
            print(مسافة + عنصر["اسم"])
            # apl-source:18
            اطبع_شجرة(عناصر, عنصر["م"], مسافة + "  ")
# apl-source:19

# apl-source:20
اطبع_شجرة(عناصر, 0, "")
# apl-source:21
