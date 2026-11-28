
# apl-source:1
# مثال 833 — رونغه-كوتا
# apl-source:2
# Runge-Kutta RK4
# apl-source:3
# Demonstrates: أربعة ميول مرجحة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/833-runge-kutta.apl
# apl-source:6

# apl-source:7
# Assertion style:
# apl-source:8
#   دالة تأكد_يساوي(فعلي, متوقع, اسم):
# apl-source:9
#     لو فعلي != متوقع:
# apl-source:10
#       اطبع "فشل:", اسم
# apl-source:11
#       اطبع "  متوقع:", متوقع
# apl-source:12
#       اطبع "  فعلي:", فعلي
# apl-source:13
#       قياسي_نظام_اخرج(1)
# apl-source:14
#     اطبع "ناجح:", اسم
# apl-source:15

# apl-source:16
def تأكد_يساوي(فعلي, متوقع, اسم):
  # apl-source:17
  if فعلي != متوقع:
    # apl-source:18
    print("فشل:", اسم)
    # apl-source:19
    print("  متوقع:", متوقع)
    # apl-source:20
    print("  فعلي:", فعلي)
    # apl-source:21
    قياسي_نظام_اخرج(1)
  # apl-source:22
  print("ناجح:", اسم)
# apl-source:23

# apl-source:24
# تكامل رونغه-كوتا الرابع: أربعة ميول مرجحة لكل خطوة
# apl-source:25
# Demonstrates: ميول k1..k4, وزن 1/6, دقة من الدرجة الرابعة
# apl-source:26

# apl-source:27
def ميل(ز, قيمة):
  # apl-source:28
  return قيمة
# apl-source:29

# apl-source:30
def ار_كي_فور(خطوة, عدد):
  # apl-source:31
  قيمة = 1.0
  # apl-source:32
  ز = 0.0
  # apl-source:33
  for ي in range(عدد):
    # apl-source:34
    ك1 = ميل(ز, قيمة)
    # apl-source:35
    ك2 = ميل(ز + خطوة / 2, قيمة + خطوة * ك1 / 2)
    # apl-source:36
    ك3 = ميل(ز + خطوة / 2, قيمة + خطوة * ك2 / 2)
    # apl-source:37
    ك4 = ميل(ز + خطوة, قيمة + خطوة * ك3)
    # apl-source:38
    قيمة = قيمة + خطوة * (ك1 + 2 * ك2 + 2 * ك3 + ك4) / 6
    # apl-source:39
    ز = ز + خطوة
  # apl-source:40
  return قيمة
# apl-source:41

# apl-source:42
تأكد_يساوي(round(ار_كي_فور(0.1, 10), 6), 2.71828, "تقدير هـ بعد عشر خطوات")
# apl-source:43
تأكد_يساوي(round(ار_كي_فور(0.05, 20), 6), 2.718282, "خطوة أدق")
# apl-source:44
تأكد_يساوي(round(ار_كي_فور(0.1, 5), 4), 1.6487, "منتصف الطريق")
# apl-source:45
تأكد_يساوي(round(ار_كي_فور(0.2, 10), 5), 7.38889, "حتى ز=2")
# apl-source:46
