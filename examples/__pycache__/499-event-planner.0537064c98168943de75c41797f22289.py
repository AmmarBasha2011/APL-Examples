
# apl-source:1
# مثال 499 — مخطط فعاليات
# apl-source:2
# Event planner
# apl-source:3
# Demonstrates: جدول بدون تداخل
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/499-event-planner.apl
# apl-source:6

# apl-source:7
فعاليات = [
    # apl-source:8
    {"اسم": "اجتماع", "من": 9, "إلى": 10},
    # apl-source:9
    {"اسم": "ورشة", "من": 10, "إلى": 12},
    # apl-source:10
    {"اسم": "غداء", "من": 12, "إلى": 13},
    # apl-source:11
    {"اسم": "عرض", "من": 11, "إلى": 12}
# apl-source:12
]
# apl-source:13

# apl-source:14
def متداخل(أ, ب):
    # apl-source:15
    return أ["من"] < ب["إلى"] and ب["من"] < أ["إلى"]
# apl-source:16

# apl-source:17
print("فحص التداخلات:")
# apl-source:18
for ي in range(len(فعاليات)):
    # apl-source:19
    for ز in range(ي + 1, len(فعاليات)):
        # apl-source:20
        if متداخل(فعاليات[ي], فعاليات[ز]):
            # apl-source:21
            print("تداخل:", فعاليات[ي]["اسم"], "مع", فعاليات[ز]["اسم"])
# apl-source:22
