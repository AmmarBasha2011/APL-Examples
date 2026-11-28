
# apl-source:1
# مثال 1939 — إجمالي الانتظار عند صراف واحد
# apl-source:2
# Single teller total wait time
# apl-source:3
# Demonstrates: محاكاة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1939-bank-single-teller-total-wait.apl
# apl-source:6

# apl-source:7
# الخدمة تبدأ عند الأكبر من الوصول وفراغ الصراف
# apl-source:8
# الانتظار = بداية الخدمة - الوصول
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
def انتظار(وصول, خدمة):
  # apl-source:19
  حر = 0
  # apl-source:20
  كلي = 0
  # apl-source:21
  for ك in range(len(وصول)):
    # apl-source:22
    بداية = max(وصول[ك], حر)
    # apl-source:23
    كلي = كلي + بداية - وصول[ك]
    # apl-source:24
    حر = بداية + خدمة[ك]
  # apl-source:25
  return كلي
# apl-source:26

# apl-source:27
تأكد_يساوي(انتظار([0, 1, 2], [3, 3, 3]), 6, "ازدحام")
# apl-source:28
تأكد_يساوي(انتظار([0, 10], [3, 3]), 0, "بلا انتظار")
# apl-source:29
تأكد_يساوي(انتظار([0], [5]), 0, "عميل واحد")
# apl-source:30
