
# apl-source:1
# مثال 663 — متحكم PID
# apl-source:2
# PID controller
# apl-source:3
# Demonstrates: PID، نسبي تكاملي تفاضلي، استقرار
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/663-pid-controller.apl
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
# متحكم PID: تنظيم بثلاثة حدود
# apl-source:25
# Demonstrates: خطأ نسبي وتكاملي وتفاضلي, محاكاة نظام, استقرار
# apl-source:26
# هكذا تثبت الروبوتات والأفران على الهدف
# apl-source:27

# apl-source:28
هدف = 100.0
# apl-source:29
موضع = 0.0
# apl-source:30
تكامل = 0.0
# apl-source:31
انحراف_سابق = 0.0
# apl-source:32
ك_ن = 0.6
# apl-source:33
ك_ت = 0.1
# apl-source:34
ك_خ = 0.05
# apl-source:35

# apl-source:36
for خطوة in range(400):
  # apl-source:37
  انحراف = هدف - موضع
  # apl-source:38
  تكامل = تكامل + انحراف
  # apl-source:39
  تفاضل = False - انحراف_سابق
  # apl-source:40
  دفع = ك_ن * انحراف + ك_ت * تكامل + ك_خ * تفاضل
  # apl-source:41
  if دفع > 20.0:
    # apl-source:42
    دفع = 20.0
  # apl-source:43
  if دفع < -20.0:
    # apl-source:44
    دفع = -20.0
  # apl-source:45
  موضع = موضع + دفع * 0.1
  # apl-source:46
  انحراف_سابق = False
# apl-source:47

# apl-source:48
تأكد_يساوي(موضع > 99.0 and موضع < 101.0, True, "استقر قرب الهدف")
# apl-source:49
تأكد_يساوي(انحراف > -1.0 and انحراف < 1.0, True, "انحراف أخير صغير")
# apl-source:50
print("موضع نهائي:", موضع)
# apl-source:51
