
# apl-source:1
# مثال 2356 — القاسم المشترك الأكبر للقائمة
# apl-source:2
# GCD of list
# apl-source:3
# Demonstrates: قوائم
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2356-list-gcd-of-all-items.apl
# apl-source:6

# apl-source:7
# # نمرر القائمة
# apl-source:8
# # ونتحقق من الناتج
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
def ق2(أ, ب):
  # apl-source:19
  while ب != 0:
    # apl-source:20
    أ, ب = ب, أ % ب
  # apl-source:21
  return أ
# apl-source:22

# apl-source:23
def ف(ق):
  # apl-source:24
  غ = ق[0]
  # apl-source:25
  for ع in ق:
    # apl-source:26
    غ = ق2(غ, ع)
  # apl-source:27
  return غ
# apl-source:28

# apl-source:29
تأكد_يساوي(ف([12, 18]), 6, "حالة 1")
# apl-source:30
تأكد_يساوي(ف([7]), 7, "حالة 2")
# apl-source:31
تأكد_يساوي(ف([8, 12, 20]), 4, "حالة 3")
# apl-source:32
تأكد_يساوي(ف([9, 10]), 1, "حالة 4")
# apl-source:33
