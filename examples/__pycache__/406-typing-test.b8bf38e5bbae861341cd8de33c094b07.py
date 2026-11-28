
# apl-source:1
# مثال 406 — اختبار سرعة الكتابة
# apl-source:2
# Typing speed test
# apl-source:3
# Demonstrates: حساب الكلمات في الدقيقة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/406-typing-test.apl
# apl-source:6

# apl-source:7
def سرعة_كتابة(نص_الأصل, نص_المكتوب, ثواني):
    # apl-source:8
    كلمات_صحيحة = 0
    # apl-source:9
    أصل = نص_الأصل.split(" ")
    # apl-source:10
    مكتوب = نص_المكتوب.split(" ")
    # apl-source:11
    أقصر = len(أصل)
    # apl-source:12
    if len(مكتوب) < أقصر:
        # apl-source:13
        أقصر = len(مكتوب)
    # apl-source:14
    for ي in range(أقصر):
        # apl-source:15
        if أصل[ي] == مكتوب[ي]:
            # apl-source:16
            كلمات_صحيحة = كلمات_صحيحة + 1
    # apl-source:17
    return [كلمات_صحيحة * 60 / ثواني, كلمات_صحيحة * 100 / len(أصل)]
# apl-source:18

# apl-source:19
نتيجة = سرعة_كتابة("البرمجة مهارة جميلة ومفيدة جدا", "البرمجة مهارة جميلة ومفيدة جدا", 20)
# apl-source:20
print("كلمة في الدقيقة:", نتيجة[0])
# apl-source:21
print("الدقة:", str(نتيجة[1]) + "%")
# apl-source:22
