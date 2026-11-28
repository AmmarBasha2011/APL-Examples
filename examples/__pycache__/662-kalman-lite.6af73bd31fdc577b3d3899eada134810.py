
# apl-source:1
# مثال 662 — مرشح كالمان الأحادي
# apl-source:2
# 1D Kalman filter
# apl-source:3
# Demonstrates: كالمان، ربح، عدم يقين
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/662-kalman-lite.apl
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
# مرشح كالمان الأحادي
# apl-source:25
# Demonstrates: تنبؤ وتحديث, ربح كالمان, تناقص عدم اليقين
# apl-source:26
# يدمج قياسات مزعجة في تقدير أهدأ
# apl-source:27

# apl-source:28
تقدير = 0.0
# apl-source:29
يقين = 1.0
# apl-source:30
ضجيج_عملية = 0.01
# apl-source:31
ضجيج_قياس = 0.5
# apl-source:32

# apl-source:33
def خطوة(تقدير, يقين, قياس):
  # apl-source:34
  يقين_متنبأ = يقين + ضجيج_عملية
  # apl-source:35
  ربح = يقين_متنبأ / (يقين_متنبأ + ضجيج_قياس)
  # apl-source:36
  تقدير_جديد = تقدير + ربح * (قياس - تقدير)
  # apl-source:37
  يقين_جديد = (1.0 - ربح) * يقين_متنبأ
  # apl-source:38
  return [تقدير_جديد, يقين_جديد]
# apl-source:39

# apl-source:40
قياسات = [19.5, 20.4, 19.8, 20.2, 19.9, 20.1, 20.3, 19.7, 20.0, 20.2]
# apl-source:41
حالة = [تقدير, يقين]
# apl-source:42
for ق in قياسات:
  # apl-source:43
  حالة = خطوة(حالة[0], حالة[1], ق)
# apl-source:44

# apl-source:45
تأكد_يساوي(حالة[0] > 19.0 and حالة[0] < 20.5, True, "التقدير قرب الحقيقة")
# apl-source:46
تأكد_يساوي(حالة[1] < يقين, True, "عدم اليقين تناقص")
# apl-source:47
تأكد_يساوي(حالة[1] > 0.0, True, "عدم اليقين موجب")
# apl-source:48
حالة2 = [حالة[0], حالة[1]]
# apl-source:49
for ي in range(5):
  # apl-source:50
  حالة2 = خطوة(حالة2[0], حالة2[1], 20.0)
# apl-source:51
تأكد_يساوي(حالة2[0] > حالة[0] or حالة[0] > 20.0, True, "يتجه نحو 20")
# apl-source:52
print("تقدير نهائي:", حالة[0])
# apl-source:53
print("يقين نهائي:", حالة[1])
# apl-source:54
