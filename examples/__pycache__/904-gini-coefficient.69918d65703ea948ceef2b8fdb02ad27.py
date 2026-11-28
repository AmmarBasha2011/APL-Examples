
# apl-source:1
# مثال 904 — معامل جيني
# apl-source:2
# Gini coefficient
# apl-source:3
# Demonstrates: مجاميع الفروق المطلقة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/904-gini-coefficient.apl
# apl-source:6

# apl-source:7
# معامل جيني: قياس عدم المساواة في التوزيع
# apl-source:8
# G = مجموع |سi - سj| / (2 * ن * مجموع س)
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
def جيني(قيم):
  # apl-source:19
  ن = len(قيم)
  # apl-source:20
  مجموع_فروق = 0
  # apl-source:21
  for i in range(ن):
    # apl-source:22
    for ج in range(ن):
      # apl-source:23
      فرق = قيم[i] - قيم[ج]
      # apl-source:24
      if فرق < 0:
        # apl-source:25
        فرق = -فرق
      # apl-source:26
      مجموع_فروق = مجموع_فروق + فرق
  # apl-source:27
  مجموع = 0
  # apl-source:28
  for x in قيم:
    # apl-source:29
    مجموع = مجموع + x
  # apl-source:30
  return مجموع_فروق / (2 * ن * مجموع)
# apl-source:31

# apl-source:32
ز1 = جيني([1, 2, 3, 4, 5])
# apl-source:33
print("جيني(1..5) =", ز1)
# apl-source:34

# apl-source:35
تأكد_يساوي(round(ز1, 4), 0.2667, "جيني 1..5")
# apl-source:36

# apl-source:37
# المساواة التامة تعطي صفراً
# apl-source:38
تأكد_يساوي(جيني([7, 7, 7, 7]), 0, "مساواة تامة")
# apl-source:39

# apl-source:40
# اللامساواة القصوى تقارب 1 - 1/ن
# apl-source:41
ز3 = جيني([0, 0, 0, 0, 100])
# apl-source:42
print("جيني(شبه قصوى) =", ز3)
# apl-source:43
تأكد_يساوي(round(ز3, 4), 0.8, "1 - 1/5")
# apl-source:44
