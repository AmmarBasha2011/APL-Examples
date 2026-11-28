
# apl-source:1
# مثال 552 — لغز إسقاط البيض
# apl-source:2
# Egg drop DP
# apl-source:3
# Demonstrates: برمجة ديناميكية، لغز البيض، أسوأ حالة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/552-egg-drop-dp.apl
# apl-source:6

# apl-source:7
def تأكد_يساوي(فعلي, متوقع, اسم):
    # apl-source:8
    if فعلي != متوقع:
        # apl-source:9
        print("فشل:", اسم, "| متوقع:", متوقع, "| فعلي:", فعلي)
        # apl-source:10
        قياسي_نظام_اخرج(1)
    # apl-source:11
    print("ناجح:", اسم)
# apl-source:12

# apl-source:13

# apl-source:14
# لغز البيض: أقل محاولات مضمونة (برمجة ديناميكية)
# apl-source:15
def أقل_محاولات(بيض, طوابق):
    # apl-source:16
    جدول = list()
    # apl-source:17
    for i in range(بيض + 1):
        # apl-source:18
        جدول.append([0] * (طوابق + 1))
    # apl-source:19
    for طابق in range(1, طوابق + 1):
        # apl-source:20
        جدول[1][طابق] = طابق
    # apl-source:21
    for ب in range(2, بيض + 1):
        # apl-source:22
        for طابق in range(1, طوابق + 1):
            # apl-source:23
            أدنى = 999999
            # apl-source:24
            for محاولة in range(1, طابق + 1):
                # apl-source:25
                أسوأ = 1 + max(جدول[ب - 1][محاولة - 1], جدول[ب][طابق - محاولة])
                # apl-source:26
                if أسوأ < أدنى:
                    # apl-source:27
                    أدنى = أسوأ
            # apl-source:28
            جدول[ب][طابق] = أدنى
    # apl-source:29
    return جدول[بيض][طوابق]
# apl-source:30

# apl-source:31
تأكد_يساوي(أقل_محاولات(2, 10), 4, "بيضتان و10 طوابق")
# apl-source:32
تأكد_يساوي(أقل_محاولات(1, 5), 5, "بيضة واحدة")
# apl-source:33
تأكد_يساوي(أقل_محاولات(2, 100), 14, "بيضتان و100 طابق")
# apl-source:34
