
# apl-source:1
# مثال 1011 — أفضل وقت للبيع
# apl-source:2
# Best time to buy and sell stock
# apl-source:3
# Demonstrates: أدنى سعر حتى الآن
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1011-best-time-stock.apl
# apl-source:6

# apl-source:7
# نمر على الأسعار ونحفظ أدنى سعر رأيناه
# apl-source:8
# الربح المحتمل كل يوم هو السعر ناقص ذلك الأدنى
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
def اقصى_ربح(أسعار):
  # apl-source:19
  أدنى = أسعار[0]
  # apl-source:20
  ربح = 0
  # apl-source:21
  for س in أسعار:
    # apl-source:22
    if س < أدنى:
      # apl-source:23
      أدنى = س
    # apl-source:24
    if (س - أدنى) > ربح:
      # apl-source:25
      ربح = س - أدنى
  # apl-source:26
  return ربح
# apl-source:27

# apl-source:28
تأكد_يساوي(اقصى_ربح([7, 1, 5, 3, 6, 4]), 5, "ربح خمسة")
# apl-source:29
تأكد_يساوي(اقصى_ربح([7, 6, 4, 3, 1]), 0, "هبوط دائم")
# apl-source:30
تأكد_يساوي(اقصى_ربح([2, 4, 1]), 2, "قمة مبكرة")
# apl-source:31
