
# apl-source:1
# مثال 265 — مكتبة كتب بسيطة
# apl-source:2
# Mini library system
# apl-source:3
# Demonstrates: إعارة واسترجاع
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/265-library-books.apl
# apl-source:6

# apl-source:7
class مكتبة:
    # apl-source:8
    def __init__(ذات):
        # apl-source:9
        ذات.كتب = {}
# apl-source:10

    # apl-source:11
    def أضف_كتابا(ذات, عنوان, نسخ):
        # apl-source:12
        ذات.كتب[عنوان] = نسخ
# apl-source:13

    # apl-source:14
    def أعِر(ذات, عنوان):
        # apl-source:15
        if عنوان not in ذات.كتب:
            # apl-source:16
            return "غير موجود"
        # apl-source:17
        if ذات.كتب[عنوان] == 0:
            # apl-source:18
            return "لا نسخ متاحة"
        # apl-source:19
        ذات.كتب[عنوان] = ذات.كتب[عنوان] - 1
        # apl-source:20
        return "تمت الإعارة"
# apl-source:21

    # apl-source:22
    def استرجع(ذات, عنوان):
        # apl-source:23
        if عنوان in ذات.كتب:
            # apl-source:24
            ذات.كتب[عنوان] = ذات.كتب[عنوان] + 1
# apl-source:25

# apl-source:26
م = مكتبة()
# apl-source:27
م.أضف_كتابا("البداية والنهاية", 2)
# apl-source:28
م.أضف_كتابا("مقدمة ابن خلدون", 1)
# apl-source:29
print(م.أعِر("البداية والنهاية"))
# apl-source:30
print(م.أعِر("مقدمة ابن خلدون"))
# apl-source:31
print(م.أعِر("مقدمة ابن خلدون"))
# apl-source:32
م.استرجع("مقدمة ابن خلدون")
# apl-source:33
print(م.أعِر("مقدمة ابن خلدون"))
# apl-source:34
