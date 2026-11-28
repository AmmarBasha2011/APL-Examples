
# apl-source:1
# مثال 483 — نظام درجات مدرسي
# apl-source:2
# School grades system
# apl-source:3
# Demonstrates: طلاب ومواد ومعدلات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/483-grades-system.apl
# apl-source:6

# apl-source:7
طلاب = {
    # apl-source:8
    "عمار": [90, 85, 95],
    # apl-source:9
    "سارة": [88, 92, 79],
    # apl-source:10
    "خالد": [70, 65, 80]
# apl-source:11
}
# apl-source:12

# apl-source:13
for اسم in طلاب.keys():
    # apl-source:14
    درجات = طلاب[اسم]
    # apl-source:15
    مجموع = 0
    # apl-source:16
    for د in درجات:
        # apl-source:17
        مجموع = مجموع + د
    # apl-source:18
    معدل = مجموع / len(درجات)
    # apl-source:19
    تقدير = "ضعيف"
    # apl-source:20
    if معدل >= 90:
        # apl-source:21
        تقدير = "ممتاز"
    # apl-source:22
    elif معدل >= 75:
        # apl-source:23
        تقدير = "جيد جدا"
    # apl-source:24
    elif معدل >= 60:
        # apl-source:25
        تقدير = "جيد"
    # apl-source:26
    print(اسم, ":", معدل, "-", تقدير)
# apl-source:27
