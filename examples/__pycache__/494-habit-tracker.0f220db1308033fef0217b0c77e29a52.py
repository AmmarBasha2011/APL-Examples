
# apl-source:1
# مثال 494 — متتبع العادات
# apl-source:2
# Habit tracker
# apl-source:3
# Demonstrates: أسبوع عادات ونسبة إنجاز
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/494-habit-tracker.apl
# apl-source:6

# apl-source:7
أيام_أسبوع = ["السبت", "الأحد", "الاثنين", "الثلاثاء", "الأربعاء", "الخميس", "الجمعة"]
# apl-source:8
عادات = {
    # apl-source:9
    "قراءة": [True, True, False, True, True, False, True],
    # apl-source:10
    "رياضة": [False, True, True, False, True, True, False]
# apl-source:11
}
# apl-source:12

# apl-source:13
for عادة in عادات.keys():
    # apl-source:14
    إنجاز = 0
    # apl-source:15
    for تمت in عادات[عادة]:
        # apl-source:16
        if تمت:
            # apl-source:17
            إنجاز = إنجاز + 1
    # apl-source:18
    print(عادة, ":", إنجاز, "/ 7 أيام")
# apl-source:19

# apl-source:20
print("أفضل يوم للقراءة: السبت")
# apl-source:21
