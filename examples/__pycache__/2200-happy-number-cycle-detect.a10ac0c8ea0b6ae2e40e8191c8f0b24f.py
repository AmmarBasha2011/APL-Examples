
# apl-source:1
# مثال 2200 — العدد السعيد
# apl-source:2
# Happy number
# apl-source:3
# Demonstrates: أرقام
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2200-happy-number-cycle-detect.apl
# apl-source:6

# apl-source:7
# # ندخل القيم
# apl-source:8
# # ونقارن النتيجة
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
def ف(ن):
  # apl-source:19
  شوهد = []
  # apl-source:20
  while ن != 1 and شوهد.count(ن) == 0:
    # apl-source:21
    شوهد = شوهد + [ن]
    # apl-source:22
    م = 0
    # apl-source:23
    for ر in str(ن):
      # apl-source:24
      م = م + int(ر) ** 2
    # apl-source:25
    ن = م
  # apl-source:26
  return ن == 1
# apl-source:27

# apl-source:28
تأكد_يساوي(ف(1), True, "حالة 1")
# apl-source:29
تأكد_يساوي(ف(7), True, "حالة 7")
# apl-source:30
تأكد_يساوي(ف(19), True, "حالة 19")
# apl-source:31
تأكد_يساوي(ف(2), False, "حالة 2")
# apl-source:32
تأكد_يساوي(ف(4), False, "حالة 4")
# apl-source:33
تأكد_يساوي(ف(100), True, "حالة 100")
# apl-source:34
