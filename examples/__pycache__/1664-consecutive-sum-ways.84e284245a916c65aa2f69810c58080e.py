
# apl-source:1
# مثال 1664 — كتابة العدد كمجموع متتاليات
# apl-source:2
# Ways as sum of consecutive integers
# apl-source:3
# Demonstrates: نظرية الأعداد
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1664-consecutive-sum-ways.apl
# apl-source:6

# apl-source:7
# مجموع ك عدداً يبدأ بـ أ يساوي ك×أ + ك(ك-1)/2
# apl-source:8
# نجرب أطوال المتتالية
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
def طرق_المتتالية(ن):
  # apl-source:19
  عد = 0
  # apl-source:20
  ك = 1
  # apl-source:21
  while ك * (ك + 1) // 2 <= ن:
    # apl-source:22
    باقي = ن - ك * (ك - 1) // 2
    # apl-source:23
    if باقي % ك == 0:
      # apl-source:24
      عد = عد + 1
    # apl-source:25
    ك = ك + 1
  # apl-source:26
  return عد
# apl-source:27

# apl-source:28
تأكد_يساوي(طرق_المتتالية(5), 2, "خمسة")
# apl-source:29
تأكد_يساوي(طرق_المتتالية(9), 3, "تسعة")
# apl-source:30
تأكد_يساوي(طرق_المتتالية(15), 4, "خمسة عشر")
# apl-source:31
تأكد_يساوي(طرق_المتتالية(8), 1, "قوة اثنين")
# apl-source:32
