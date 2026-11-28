
# apl-source:1
# مثال 1744 — الربح بصفقات متعددة
# apl-source:2
# Stock profit with unlimited trades
# apl-source:3
# Demonstrates: جشع
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1744-stock-profit-many-trades.apl
# apl-source:6

# apl-source:7
# كل ارتفاع بين يومين ربح
# apl-source:8
# نتجاهل الانخفاض
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
def ربح_متعدد(أسعار):
  # apl-source:19
  ربح = 0
  # apl-source:20
  for ك in range(1, len(أسعار)):
    # apl-source:21
    if أسعار[ك] > أسعار[ك - 1]:
      # apl-source:22
      ربح = ربح + أسعار[ك] - أسعار[ك - 1]
  # apl-source:23
  return ربح
# apl-source:24

# apl-source:25
تأكد_يساوي(ربح_متعدد([7, 1, 5, 3, 6, 4]), 7, "كلاسيكي")
# apl-source:26
تأكد_يساوي(ربح_متعدد([1, 2, 3, 4, 5]), 4, "صاعدة")
# apl-source:27
تأكد_يساوي(ربح_متعدد([5, 4, 3]), 0, "هابطة")
# apl-source:28
