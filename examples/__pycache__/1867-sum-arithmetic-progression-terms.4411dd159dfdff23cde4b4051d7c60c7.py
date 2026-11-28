
# apl-source:1
# مثال 1867 — مجموع المتوالية الحسابية
# apl-source:2
# Arithmetic progression sum
# apl-source:3
# Demonstrates: حساب
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1867-sum-arithmetic-progression-terms.apl
# apl-source:6

# apl-source:7
# المجموع = ن × (الأول + الأخير) ÷ 2
# apl-source:8
# نتحقق بالجمع المباشر
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
def مجموع_متوالية(أول, فرق, ن):
  # apl-source:19
  أخير = أول + (ن - 1) * فرق
  # apl-source:20
  return ن * (أول + أخير) // 2
# apl-source:21

# apl-source:22
def مباشر(أول, فرق, ن):
  # apl-source:23
  مجموع = 0
  # apl-source:24
  for ك in range(ن):
    # apl-source:25
    مجموع = مجموع + أول + ك * فرق
  # apl-source:26
  return مجموع
# apl-source:27

# apl-source:28
تأكد_يساوي(مجموع_متوالية(1, 1, 100), 5050, "مئة")
# apl-source:29
تأكد_يساوي(مجموع_متوالية(2, 3, 5), 40, "خمسة")
# apl-source:30
تأكد_يساوي(مجموع_متوالية(5, 2, 7), مباشر(5, 2, 7), "تطابق")
# apl-source:31
