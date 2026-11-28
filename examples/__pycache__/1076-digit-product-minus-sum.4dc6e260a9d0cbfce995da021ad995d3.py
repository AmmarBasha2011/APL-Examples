
# apl-source:1
# مثال 1076 — الفرق بين ضرب وجمع الخانات
# apl-source:2
# Subtract product and sum of digits
# apl-source:3
# Demonstrates: استخراج الخانات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1076-digit-product-minus-sum.apl
# apl-source:6

# apl-source:7
# نستخرج الخانات بالباقي والقسمة على عشرة
# apl-source:8
# ونطرح مجموعها من حاصل ضربها
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
def فرق_خانات(ن):
  # apl-source:19
  ضرب = 1
  # apl-source:20
  جمع = 0
  # apl-source:21
  while ن > 0:
    # apl-source:22
    خ = ن % 10
    # apl-source:23
    ضرب = ضرب * خ
    # apl-source:24
    جمع = جمع + خ
    # apl-source:25
    ن = ن // 10
  # apl-source:26
  return ضرب - جمع
# apl-source:27

# apl-source:28
تأكد_يساوي(فرق_خانات(234), 15, "234")
# apl-source:29
تأكد_يساوي(فرق_خانات(4421), 21, "4421")
# apl-source:30
تأكد_يساوي(فرق_خانات(5), 0, "خانة واحدة")
# apl-source:31
