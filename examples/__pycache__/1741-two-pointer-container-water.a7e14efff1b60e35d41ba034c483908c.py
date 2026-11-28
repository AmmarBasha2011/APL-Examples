
# apl-source:1
# مثال 1741 — أكبر حاوية ماء
# apl-source:2
# Container with most water
# apl-source:3
# Demonstrates: مؤشران
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1741-two-pointer-container-water.apl
# apl-source:6

# apl-source:7
# مؤشر من كل طرف
# apl-source:8
# المساحة بالأقصر في العرض
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
def أكبر_حاوية(ارتفاعات):
  # apl-source:19
  ي = 0
  # apl-source:20
  ك = len(ارتفاعات) - 1
  # apl-source:21
  أفضل = 0
  # apl-source:22
  while ي < ك:
    # apl-source:23
    مساحة = min(ارتفاعات[ي], ارتفاعات[ك]) * (ك - ي)
    # apl-source:24
    أفضل = max(أفضل, مساحة)
    # apl-source:25
    if ارتفاعات[ي] < ارتفاعات[ك]:
      # apl-source:26
      ي = ي + 1
    # apl-source:27
    else:
      # apl-source:28
      ك = ك - 1
  # apl-source:29
  return أفضل
# apl-source:30

# apl-source:31
تأكد_يساوي(أكبر_حاوية([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49, "كلاسيكي")
# apl-source:32
تأكد_يساوي(أكبر_حاوية([1, 1]), 1, "اثنان")
# apl-source:33
