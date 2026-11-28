
# apl-source:1
# مثال 877 — جامع الكوبونات
# apl-source:2
# Coupon collector
# apl-source:3
# Demonstrates: n ضرب العدد التوافقي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/877-coupon-collector.apl
# apl-source:6

# apl-source:7
# جامع الكوبونات: متوسط التجارب لجمع n نوعاً هو n * H(n)
# apl-source:8
# H(n) هو العدد التوافقي؛ لستة أنواع: 14.7 تجربة
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
def توافقي(ن):
  # apl-source:19
  مجموع = 0.0
  # apl-source:20
  for ك in range(1, ن + 1):
    # apl-source:21
    مجموع = مجموع + 1.0 / ك
  # apl-source:22
  return مجموع
# apl-source:23

# apl-source:24
def متوسط_جمع(أنواع):
  # apl-source:25
  return أنواع * توافقي(أنواع)
# apl-source:26

# apl-source:27
print("متوسط جمع 6 أنواع:", متوسط_جمع(6))
# apl-source:28
print("متوسط جمع 10 أنواع:", متوسط_جمع(10))
# apl-source:29

# apl-source:30
تأكد_يساوي(round(متوسط_جمع(1), 6), 1.0, "نوع واحد = تجربة واحدة")
# apl-source:31
تأكد_يساوي(round(متوسط_جمع(6), 1), 14.7, "6 أنواع = 14.7")
# apl-source:32
تأكد_يساوي(round(متوسط_جمع(10), 2), 29.29, "10 أنواع = 29.29")
# apl-source:33

# apl-source:34
# التوافقي ينمو لوغاريتمياً: H(100) ≈ 5.19
# apl-source:35
تأكد_يساوي(round(توافقي(100), 2), 5.19, "H(100) ≈ 5.19")
# apl-source:36
