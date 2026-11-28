
# apl-source:1
# مثال 1114 — أول عدد فريد في تدفق
# apl-source:2
# First unique number in a stream
# apl-source:3
# Demonstrates: عد الظهور
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1114-first-unique-stream.apl
# apl-source:6

# apl-source:7
# نحتفظ بالعناصر بترتيب وصولها
# apl-source:8
# ونفحص أول عنصر يظهر مرة واحدة فقط
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
class اول_فريد:
    # apl-source:19
    def __init__(ذات, بداية):
        # apl-source:20
        ذات.عناصر = list(بداية)
# apl-source:21

    # apl-source:22
    def ظهور(ذات, س):
        # apl-source:23
        ن = 0
        # apl-source:24
        for ع in ذات.عناصر:
            # apl-source:25
            if ع == س:
                # apl-source:26
                ن = ن + 1
        # apl-source:27
        return ن
# apl-source:28

    # apl-source:29
    def اظهر_الاول(ذات):
        # apl-source:30
        for ع in ذات.عناصر:
            # apl-source:31
            if ذات.ظهور(ع) == 1:
                # apl-source:32
                return ع
        # apl-source:33
        return -1
# apl-source:34

    # apl-source:35
    def اضف_قيمة(ذات, س):
        # apl-source:36
        ذات.عناصر = ذات.عناصر + [س]
# apl-source:37

# apl-source:38
ف = اول_فريد([2, 3, 5])
# apl-source:39
تأكد_يساوي(ف.اظهر_الاول(), 2, "البداية")
# apl-source:40
ف.اضف_قيمة(5)
# apl-source:41
تأكد_يساوي(ف.اظهر_الاول(), 2, "بعد 5")
# apl-source:42
ف.اضف_قيمة(2)
# apl-source:43
تأكد_يساوي(ف.اظهر_الاول(), 3, "بعد 2")
# apl-source:44
ف.اضف_قيمة(3)
# apl-source:45
تأكد_يساوي(ف.اظهر_الاول(), -1, "لا فريد")
# apl-source:46
