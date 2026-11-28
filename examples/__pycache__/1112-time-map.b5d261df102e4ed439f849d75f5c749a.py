
# apl-source:1
# مثال 1112 — خريطة زمنية
# apl-source:2
# Time based key-value store
# apl-source:3
# Demonstrates: نسخ بالطوابع الزمنية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1112-time-map.apl
# apl-source:6

# apl-source:7
# كل مفتاح يحتفظ بقيمه مع أوقاتها
# apl-source:8
# والقراءة ترجع آخر قيمة وقتها لا يتجاوز الوقت المطلوب
# apl-source:9

# apl-source:10
def تأكد_يساوي(فعلي, متوقع, اسم):
  # apl-source:11
  if فعلي != متوقع:
    # apl-source:12
    print("فشل:", اسم)
    # apl-source:13
    print("  متوقع:", متوقع)
    # apl-source:14
    print("  فعلي:", فعلي)
    # apl-source:15
    قياسي_نظام_اخرج(1)
  # apl-source:16
  print("ناجح:", اسم)
# apl-source:17

# apl-source:18
class خريطة_زمنية:
    # apl-source:19
    def __init__(ذات):
        # apl-source:20
        ذات.مفاتيح = []
        # apl-source:21
        ذات.سجلات = []
# apl-source:22

    # apl-source:23
    def ضع(ذات, مفتاح, قيمة, وقت):
        # apl-source:24
        if مفتاح not in ذات.مفاتيح:
            # apl-source:25
            ذات.مفاتيح = ذات.مفاتيح + [مفتاح]
            # apl-source:26
            ذات.سجلات = ذات.سجلات + [[]]
        # apl-source:27
        ف = 0
        # apl-source:28
        while ذات.مفاتيح[ف] != مفتاح:
            # apl-source:29
            ف = ف + 1
        # apl-source:30
        ذات.سجلات[ف] = ذات.سجلات[ف] + [[وقت, قيمة]]
# apl-source:31

    # apl-source:32
    def هات(ذات, مفتاح, وقت):
        # apl-source:33
        if مفتاح not in ذات.مفاتيح:
            # apl-source:34
            return ""
        # apl-source:35
        ف = 0
        # apl-source:36
        while ذات.مفاتيح[ف] != مفتاح:
            # apl-source:37
            ف = ف + 1
        # apl-source:38
        نتيجة = ""
        # apl-source:39
        for زوج in ذات.سجلات[ف]:
            # apl-source:40
            if زوج[0] <= وقت:
                # apl-source:41
                نتيجة = زوج[1]
        # apl-source:42
        return نتيجة
# apl-source:43

# apl-source:44
خ = خريطة_زمنية()
# apl-source:45
خ.ضع("foo", "bar", 1)
# apl-source:46
تأكد_يساوي(خ.هات("foo", 1), "bar", "الوقت نفسه")
# apl-source:47
تأكد_يساوي(خ.هات("foo", 3), "bar", "وقت لاحق")
# apl-source:48
خ.ضع("foo", "bar2", 4)
# apl-source:49
تأكد_يساوي(خ.هات("foo", 4), "bar2", "القيمة الجديدة")
# apl-source:50
تأكد_يساوي(خ.هات("foo", 5), "bar2", "بعد القيمة الجديدة")
# apl-source:51
تأكد_يساوي(خ.هات("foo", 0), "", "قبل أي قيمة")
# apl-source:52
تأكد_يساوي(خ.هات("baz", 9), "", "مفتاح غائب")
# apl-source:53
