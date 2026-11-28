
# apl-source:1
# مثال 267 — مصروفات بالفئات
# apl-source:2
# Expenses by category
# apl-source:3
# Demonstrates: تجميع ونِسَب
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/267-expense-categories.apl
# apl-source:6

# apl-source:7
مصروفات = [
    # apl-source:8
    {"وصف": "سوبر ماركت", "فئة": "طعام", "مبلغ": 300},
    # apl-source:9
    {"وصف": "مطعم", "فئة": "طعام", "مبلغ": 150},
    # apl-source:10
    {"وصف": "بنزين", "فئة": "مواصلات", "مبلغ": 200},
    # apl-source:11
    {"وصف": "فاتورة نت", "فئة": "فواتير", "مبلغ": 250}
# apl-source:12
]
# apl-source:13

# apl-source:14
بالفئة = {}
# apl-source:15
for م in مصروفات:
    # apl-source:16
    فئة = م["فئة"]
    # apl-source:17
    if فئة in بالفئة:
        # apl-source:18
        بالفئة[فئة] = بالفئة[فئة] + م["مبلغ"]
    # apl-source:19
    else:
        # apl-source:20
        بالفئة[فئة] = م["مبلغ"]
# apl-source:21

# apl-source:22
إجمالي = 0
# apl-source:23
for فئة in بالفئة:
    # apl-source:24
    إجمالي = إجمالي + بالفئة[فئة]
# apl-source:25

# apl-source:26
for فئة in بالفئة:
    # apl-source:27
    print(فئة, ":", بالفئة[فئة], "(", round(بالفئة[فئة] * 100 / إجمالي, 1), "%)")
# apl-source:28
print("الإجمالي:", إجمالي)
# apl-source:29
