
# apl-source:1
# مثال 393 — المتوسط المرجح
# apl-source:2
# Weighted average
# apl-source:3
# Demonstrates: أوزان الدرجات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/393-weighted-average.apl
# apl-source:6

# apl-source:7
مقررات = [
    # apl-source:8
    {"اسم": "رياضيات", "درجة": 85, "ساعة": 3},
    # apl-source:9
    {"اسم": "برمجة", "درجة": 95, "ساعة": 4},
    # apl-source:10
    {"اسم": "فيزياء", "درجة": 70, "ساعة": 2}
# apl-source:11
]
# apl-source:12

# apl-source:13
مرجح = 0
# apl-source:14
ساعة_كلي = 0
# apl-source:15
for مقرر in مقررات:
    # apl-source:16
    مرجح = مرجح + مقرر["درجة"] * مقرر["ساعة"]
    # apl-source:17
    ساعة_كلي = ساعة_كلي + مقرر["ساعة"]
# apl-source:18

# apl-source:19
print("المتوسط المرجح:", مرجح / ساعة_كلي)
# apl-source:20
