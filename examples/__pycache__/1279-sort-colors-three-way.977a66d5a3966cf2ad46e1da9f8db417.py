
# apl-source:1
# مثال 1279 — فرز ألوان
# apl-source:2
# Sort colors three way partition
# apl-source:3
# Demonstrates: تقسيم ثلاثي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1279-sort-colors-three-way.apl
# apl-source:6

# apl-source:7
# ثلاثة مؤشرات للأصفار والأحادات والاثنينات
# apl-source:8
# نبدل العنصر الحالي إلى مكانه
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
def افرز_الوان(أ):
  # apl-source:19
  ق = list(أ)
  # apl-source:20
  ي = 0
  # apl-source:21
  م = 0
  # apl-source:22
  ن = len(ق) - 1
  # apl-source:23
  while م <= ن:
    # apl-source:24
    if ق[م] == 0:
      # apl-source:25
      ت = ق[ي]
      # apl-source:26
      ق[ي] = ق[م]
      # apl-source:27
      ق[م] = ت
      # apl-source:28
      ي = ي + 1
      # apl-source:29
      م = م + 1
    # apl-source:30
    elif ق[م] == 2:
      # apl-source:31
      ت = ق[ن]
      # apl-source:32
      ق[ن] = ق[م]
      # apl-source:33
      ق[م] = ت
      # apl-source:34
      ن = ن - 1
    # apl-source:35
    else:
      # apl-source:36
      م = م + 1
  # apl-source:37
  return ق
# apl-source:38

# apl-source:39
تأكد_يساوي(افرز_الوان([2,0,2,1,1,0]), [0,0,1,1,2,2], "مثال أول")
# apl-source:40
تأكد_يساوي(افرز_الوان([2,0,1]), [0,1,2], "ثلاثة")
# apl-source:41
تأكد_يساوي(افرز_الوان([1,1,1]), [1,1,1], "متشابهة")
# apl-source:42
