
# apl-source:1
# مثال 435 — تنسيق المدد الزمنية
# apl-source:2
# Duration formatting
# apl-source:3
# Demonstrates: ثواني إلى نص مقروء
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/435-duration-format.apl
# apl-source:6

# apl-source:7
def نص_مدة(ثواني):
    # apl-source:8
    ساعة_ق = ثواني // 3600
    # apl-source:9
    دقيقة = (ثواني % 3600) // 60
    # apl-source:10
    ثانية = ثواني % 60
    # apl-source:11
    أجزاء = []
    # apl-source:12
    if ساعة_ق > 0:
        # apl-source:13
        أجزاء.append(str(ساعة_ق) + " ساعة")
    # apl-source:14
    if دقيقة > 0:
        # apl-source:15
        أجزاء.append(str(دقيقة) + " دقيقة")
    # apl-source:16
    if ثانية > 0:
        # apl-source:17
        أجزاء.append(str(ثانية) + " ثانية")
    # apl-source:18
    if len(أجزاء) == 0:
        # apl-source:19
        return "صفر"
    # apl-source:20
    return " و ".join(أجزاء)
# apl-source:21

# apl-source:22
print(نص_مدة(3661))
# apl-source:23
print(نص_مدة(125))
# apl-source:24
print(نص_مدة(59))
# apl-source:25
