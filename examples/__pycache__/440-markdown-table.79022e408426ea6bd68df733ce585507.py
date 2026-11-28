
# apl-source:1
# مثال 440 — مولد جداول ماركداون
# apl-source:2
# Markdown table generator
# apl-source:3
# Demonstrates: بناء جدول من قواميس
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/440-markdown-table.apl
# apl-source:6

# apl-source:7
def جدول_ماركداون(عناوين, صفوف):
    # apl-source:8
    print("| " + " | ".join(عناوين) + " |")
    # apl-source:9
    فاصل = []
    # apl-source:10
    for _ in range(len(عناوين)):
        # apl-source:11
        فاصل.append("---")
    # apl-source:12
    print("| " + " | ".join(فاصل) + " |")
    # apl-source:13
    for صف_جدول in صفوف:
        # apl-source:14
        print("| " + " | ".join(صف_جدول) + " |")
# apl-source:15

# apl-source:16
جدول_ماركداون(["اللغة", "السنة", "المجال"], [
    # apl-source:17
    ["APL", "2026", "برمجة"],
    # apl-source:18
    ["بايثون", "1991", "عام"],
    # apl-source:19
    ["جافاسكربت", "1995", "ويب"]
# apl-source:20
])
# apl-source:21
