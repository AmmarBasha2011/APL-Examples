
# apl-source:1
# مثال 2201 — عدد سميث
# apl-source:2
# Smith number check
# apl-source:3
# Demonstrates: أرقام
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2201-smith-like-digit-sum-equals-factor-sum.apl
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
def مجد(ن):
  # apl-source:19
  م = 0
  # apl-source:20
  for ر in str(ن):
    # apl-source:21
    م = م + int(ر)
  # apl-source:22
  return م
# apl-source:23

# apl-source:24
def ف(ن):
  # apl-source:25
  ا = ن
  # apl-source:26
  د = 2
  # apl-source:27
  ع = 0
  # apl-source:28
  ف2 = 0
  # apl-source:29
  while ا > 1:
    # apl-source:30
    if ا % د == 0:
      # apl-source:31
      ف2 = ف2 + مجد(د)
      # apl-source:32
      ع = ع + 1
      # apl-source:33
      ا = ا // د
    # apl-source:34
    else:
      # apl-source:35
      د = د + 1
  # apl-source:36
  return ع > 1 and ف2 == مجد(ن)
# apl-source:37

# apl-source:38
تأكد_يساوي(ف(4), True, "حالة 4")
# apl-source:39
تأكد_يساوي(ف(22), True, "حالة 22")
# apl-source:40
تأكد_يساوي(ف(27), True, "حالة 27")
# apl-source:41
تأكد_يساوي(ف(13), False, "حالة 13")
# apl-source:42
تأكد_يساوي(ف(58), True, "حالة 58")
# apl-source:43
تأكد_يساوي(ف(85), True, "حالة 85")
# apl-source:44
