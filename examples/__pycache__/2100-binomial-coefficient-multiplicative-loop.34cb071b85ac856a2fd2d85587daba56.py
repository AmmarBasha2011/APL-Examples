
# apl-source:1
# مثال 2100 — معامل ذي الحدين بالضرب المتكرر
# apl-source:2
# Binomial coefficient multiplicative
# apl-source:3
# Demonstrates: توافيق
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2100-binomial-coefficient-multiplicative-loop.apl
# apl-source:6

# apl-source:7
# # الناتج بعد كل خطوة صحيح دائما
# apl-source:8
# # C(n,k) = 0 إذا كان k أكبر من n
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
def اختر(ن, ك):
  # apl-source:19
  if ك > ن:
    # apl-source:20
    return 0
  # apl-source:21
  ك = min(ك, ن - ك)
  # apl-source:22
  ناتج = 1
  # apl-source:23
  for ي in range(1, ك + 1):
    # apl-source:24
    ناتج = ناتج * (ن - ك + ي) // ي
  # apl-source:25
  return ناتج
# apl-source:26

# apl-source:27
تأكد_يساوي(اختر(10, 3), 120, "١٠،٣")
# apl-source:28
تأكد_يساوي(اختر(52, 5), 2598960, "ورق")
# apl-source:29
تأكد_يساوي(اختر(5, 0), 1, "صفر")
# apl-source:30
تأكد_يساوي(اختر(5, 6), 0, "أكبر")
# apl-source:31
