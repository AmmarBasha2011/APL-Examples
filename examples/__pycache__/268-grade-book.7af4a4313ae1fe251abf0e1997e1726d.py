
# apl-source:1
# مثال 268 — سجل درجات فصل
# apl-source:2
# Class grade book
# apl-source:3
# Demonstrates: متوسطات وتقديرات وترتيب
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/268-grade-book.apl
# apl-source:6

# apl-source:7
طلاب = {
    # apl-source:8
    "علي": [80, 75, 90],
    # apl-source:9
    "سارة": [95, 88, 92],
    # apl-source:10
    "خالد": [60, 70, 65]
# apl-source:11
}
# apl-source:12

# apl-source:13
def متوسط(قائمة):
    # apl-source:14
    م = 0
    # apl-source:15
    for ع in قائمة:
        # apl-source:16
        م = م + ع
    # apl-source:17
    return م / len(قائمة)
# apl-source:18

# apl-source:19
def تقدير(درجة):
    # apl-source:20
    if درجة >= 90:
        # apl-source:21
        return "ممتاز"
    # apl-source:22
    elif درجة >= 75:
        # apl-source:23
        return "جيد جدا"
    # apl-source:24
    elif درجة >= 60:
        # apl-source:25
        return "جيد"
    # apl-source:26
    else:
        # apl-source:27
        return "ضعيف"
# apl-source:28

# apl-source:29
نتائج = []
# apl-source:30
for اسم in طلاب:
    # apl-source:31
    م = متوسط(طلاب[اسم])
    # apl-source:32
    نتائج.append({"اسم": اسم, "متوسط": round(م, 1), "تقدير": تقدير(م)})
# apl-source:33

# apl-source:34
مرتبون = sorted(نتائج, key=lambda س: س["متوسط"], reverse=True)
# apl-source:35
for ي in range(len(مرتبون)):
    # apl-source:36
    print(ي + 1, "-", مرتبون[ي]["اسم"], ":", مرتبون[ي]["متوسط"], "(", مرتبون[ي]["تقدير"], ")")
# apl-source:37
