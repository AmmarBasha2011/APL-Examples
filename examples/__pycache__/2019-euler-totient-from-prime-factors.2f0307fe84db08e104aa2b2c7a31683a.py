
# apl-source:1
# مثال 2019 — دالة أويلر فاي
# apl-source:2
# Euler totient
# apl-source:3
# Demonstrates: نظرية الأعداد
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2019-euler-totient-from-prime-factors.apl
# apl-source:6

# apl-source:7
# # نبدأ بالعدد نفسه
# apl-source:8
# # ولكل عامل أولي ننقص النتيجة بمقدار قسمتها على العامل
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
def فاي(ن):
  # apl-source:19
  نتيجة = ن
  # apl-source:20
  د = 2
  # apl-source:21
  while د * د <= ن:
    # apl-source:22
    if ن % د == 0:
      # apl-source:23
      while ن % د == 0:
        # apl-source:24
        ن = ن // د
      # apl-source:25
      نتيجة = نتيجة - نتيجة // د
    # apl-source:26
    د = د + 1
  # apl-source:27
  if ن > 1:
    # apl-source:28
    نتيجة = نتيجة - نتيجة // ن
  # apl-source:29
  return نتيجة
# apl-source:30

# apl-source:31
تأكد_يساوي(فاي(1), 1, "١")
# apl-source:32
تأكد_يساوي(فاي(9), 6, "٩")
# apl-source:33
تأكد_يساوي(فاي(10), 4, "١٠")
# apl-source:34
تأكد_يساوي(فاي(36), 12, "٣٦")
# apl-source:35
تأكد_يساوي(فاي(97), 96, "أولي")
# apl-source:36
