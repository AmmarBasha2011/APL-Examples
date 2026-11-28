
# apl-source:1
# مثال 497 — محرك بحث جهات اتصال
# apl-source:2
# Contact search engine
# apl-source:3
# Demonstrates: بحث جزئي غير حساس للحالة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/497-contact-search.apl
# apl-source:6

# apl-source:7
جهات = [
    # apl-source:8
    {"اسم": "Ahmed Ali", "هاتف": "01011112222"},
    # apl-source:9
    {"اسم": "Sara Ahmed", "هاتف": "01033334444"},
    # apl-source:10
    {"اسم": "Ali Hassan", "هاتف": "01055556666"}
# apl-source:11
]
# apl-source:12

# apl-source:13
def ابحث(جزء):
    # apl-source:14
    نتائج = []
    # apl-source:15
    for جهة in جهات:
        # apl-source:16
        if جهة["اسم"].lower().find(جزء.lower()) >= 0:
            # apl-source:17
            نتائج.append(جهة)
    # apl-source:18
    return نتائج
# apl-source:19

# apl-source:20
نتائج = ابحث("ali")
# apl-source:21
print("نتائج البحث عن ali:", len(نتائج))
# apl-source:22
for ن in نتائج:
    # apl-source:23
    print("  ", ن["اسم"], "-", ن["هاتف"])
# apl-source:24
