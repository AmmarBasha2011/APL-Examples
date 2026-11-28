
# apl-source:1
# مثال 487 — محلل استبيان
# apl-source:2
# Survey analyzer
# apl-source:3
# Demonstrates: نسب إجابات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/487-survey-analyzer.apl
# apl-source:6

# apl-source:7
إجابات = ["ممتاز", "جيد", "ممتاز", "مقبول", "جيد", "ممتاز", "جيد"]
# apl-source:8
خيارات = ["ممتاز", "جيد", "مقبول"]
# apl-source:9

# apl-source:10
print("نتائج الاستبيان:")
# apl-source:11
for خيار in خيارات:
    # apl-source:12
    عد = إجابات.count(خيار)
    # apl-source:13
    نسبة = int(عد / len(إجابات) * 100)
    # apl-source:14
    print(خيار, ":", عد, "(" + str(نسبة) + "%)")
# apl-source:15
