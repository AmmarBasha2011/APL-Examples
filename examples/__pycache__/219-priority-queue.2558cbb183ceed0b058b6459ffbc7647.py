import queue
# apl-source:1
# مثال 219 — طابور الأولوية اليدوي
# apl-source:2
# Manual priority queue
# apl-source:3
# Demonstrates: قائمة مرتبة بالأولوية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/219-priority-queue.apl
# apl-source:6

# apl-source:7
class طابور_أولوية:
    # apl-source:8
    def __init__(ذات):
        # apl-source:9
        ذات.عناصر = []
# apl-source:10

    # apl-source:11
    def أدخل(ذات, عنصر, أولوية):
        # apl-source:12
        ذات.عناصر.append({"عنصر": عنصر, "أولوية": أولوية})
# apl-source:13

    # apl-source:14
    def أخرج_أعلى(ذات):
        # apl-source:15
        if len(ذات.عناصر) == 0:
            # apl-source:16
            return "فارغ"
        # apl-source:17
        أعلى = 0
        # apl-source:18
        for ي in range(1, len(ذات.عناصر)):
            # apl-source:19
            if ذات.عناصر[ي]["أولوية"] > ذات.عناصر[أعلى]["أولوية"]:
                # apl-source:20
                أعلى = ي
        # apl-source:21
        return ذات.عناصر.pop(أعلى)["عنصر"]
# apl-source:22

# apl-source:23
ط = طابور_أولوية()
# apl-source:24
ط.أدخل("مهمة عادية", 1)
# apl-source:25
ط.أدخل("طارئة", 10)
# apl-source:26
ط.أدخل("مهمة", 5)
# apl-source:27
print(ط.أخرج_أعلى())
# apl-source:28
print(ط.أخرج_أعلى())
# apl-source:29
print(ط.أخرج_أعلى())
# apl-source:30
