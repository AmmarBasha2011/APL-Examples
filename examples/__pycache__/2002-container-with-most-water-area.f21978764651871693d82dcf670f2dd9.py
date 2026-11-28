
# apl-source:1
# مثال 2002 — أكبر حاوية ماء
# apl-source:2
# Container with most water
# apl-source:3
# Demonstrates: مؤشران
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2002-container-with-most-water-area.apl
# apl-source:6

# apl-source:7
# # نحرك مؤشر الجدار الأقصر دائما
# apl-source:8
# # لأن تحريك الأطول لا يزيد المساحة
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
def اكبر_مساحة(ارتفاع):
  # apl-source:19
  ي = 0
  # apl-source:20
  ل = len(ارتفاع) - 1
  # apl-source:21
  افضل = 0
  # apl-source:22
  while ي < ل:
    # apl-source:23
    افضل = max(افضل, min(ارتفاع[ي], ارتفاع[ل]) * (ل - ي))
    # apl-source:24
    if ارتفاع[ي] < ارتفاع[ل]:
      # apl-source:25
      ي = ي + 1
    # apl-source:26
    else:
      # apl-source:27
      ل = ل - 1
  # apl-source:28
  return افضل
# apl-source:29

# apl-source:30
تأكد_يساوي(اكبر_مساحة([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49, "كلاسيكي")
# apl-source:31
تأكد_يساوي(اكبر_مساحة([1, 1]), 1, "جداران")
# apl-source:32
تأكد_يساوي(اكبر_مساحة([4, 3, 2, 1, 4]), 16, "الطرفان")
# apl-source:33
