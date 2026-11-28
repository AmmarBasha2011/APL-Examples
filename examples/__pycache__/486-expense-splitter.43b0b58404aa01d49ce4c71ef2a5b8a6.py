
# apl-source:1
# مثال 486 — مقسم المصاريف
# apl-source:2
# Expense splitter
# apl-source:3
# Demonstrates: تقسيم فاتورة رحلة بالتساوي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/486-expense-splitter.apl
# apl-source:6

# apl-source:7
مصاريف = [
    # apl-source:8
    {"دافع": "عمار", "مبلغ": 300},
    # apl-source:9
    {"دافع": "سارة", "مبلغ": 150},
    # apl-source:10
    {"دافع": "خالد", "مبلغ": 60}
# apl-source:11
]
# apl-source:12

# apl-source:13
أسماء = ["عمار", "سارة", "خالد"]
# apl-source:14
إجمالي = 0
# apl-source:15
for مصروف in مصاريف:
    # apl-source:16
    إجمالي = إجمالي + مصروف["مبلغ"]
# apl-source:17
نصيب = إجمالي / len(أسماء)
# apl-source:18

# apl-source:19
print("الإجمالي:", إجمالي, "- نصيب كل واحد:", نصيب)
# apl-source:20
for مصروف in مصاريف:
    # apl-source:21
    فرق = مصروف["مبلغ"] - نصيب
    # apl-source:22
    if فرق > 0:
        # apl-source:23
        print(مصروف["دافع"], "يستحق", فرق)
    # apl-source:24
    elif فرق < 0:
        # apl-source:25
        print(مصروف["دافع"], "يدفع", abs(فرق))
    # apl-source:26
    else:
        # apl-source:27
        print(مصروف["دافع"], "متساوي")
# apl-source:28
