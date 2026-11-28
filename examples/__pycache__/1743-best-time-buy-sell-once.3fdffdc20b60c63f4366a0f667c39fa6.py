
# apl-source:1
# مثال 1743 — أفضل ربح بصفقة واحدة
# apl-source:2
# Best time to buy and sell stock once
# apl-source:3
# Demonstrates: جشع
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1743-best-time-buy-sell-once.apl
# apl-source:6

# apl-source:7
# أقل سعر حتى الآن
# apl-source:8
# الربح الأعلى عند كل يوم
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
def أفضل_ربح(أسعار):
  # apl-source:19
  أدنى = أسعار[0]
  # apl-source:20
  ربح = 0
  # apl-source:21
  for س in أسعار:
    # apl-source:22
    أدنى = min(أدنى, س)
    # apl-source:23
    ربح = max(ربح, س - أدنى)
  # apl-source:24
  return ربح
# apl-source:25

# apl-source:26
تأكد_يساوي(أفضل_ربح([7, 1, 5, 3, 6, 4]), 5, "كلاسيكي")
# apl-source:27
تأكد_يساوي(أفضل_ربح([7, 6, 4, 3, 1]), 0, "هابطة")
# apl-source:28
تأكد_يساوي(أفضل_ربح([2]), 0, "يوم")
# apl-source:29
