
# apl-source:1
# مثال 1002 — أكبر حاوية ماء
# apl-source:2
# Container with most water
# apl-source:3
# Demonstrates: مؤشران من الطرفين
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1002-container-water.apl
# apl-source:6

# apl-source:7
# نبدأ بمؤشرين عند الطرفين ونحرك الأقصر منهما
# apl-source:8
# المساحة هي العرض في أقصر الارتفاعين
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
def اكبر_ماء(ارتفاعات):
  # apl-source:19
  ي = 0
  # apl-source:20
  ن = len(ارتفاعات) - 1
  # apl-source:21
  أفضل = 0
  # apl-source:22
  while ي < ن:
    # apl-source:23
    ع = ارتفاعات[ي]
    # apl-source:24
    if ارتفاعات[ن] < ع:
      # apl-source:25
      ع = ارتفاعات[ن]
    # apl-source:26
    مساحة = ع * (ن - ي)
    # apl-source:27
    if مساحة > أفضل:
      # apl-source:28
      أفضل = مساحة
    # apl-source:29
    if ارتفاعات[ي] < ارتفاعات[ن]:
      # apl-source:30
      ي = ي + 1
    # apl-source:31
    else:
      # apl-source:32
      ن = ن - 1
  # apl-source:33
  return أفضل
# apl-source:34

# apl-source:35
تأكد_يساوي(اكبر_ماء([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49, "المثال الكلاسيكي")
# apl-source:36
تأكد_يساوي(اكبر_ماء([1, 1]), 1, "عمودان")
# apl-source:37
تأكد_يساوي(اكبر_ماء([4, 3, 2, 1, 4]), 16, "الطرفان")
# apl-source:38
