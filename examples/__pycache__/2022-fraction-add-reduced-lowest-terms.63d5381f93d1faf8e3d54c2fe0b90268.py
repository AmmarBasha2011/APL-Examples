
# apl-source:1
# مثال 2022 — جمع كسرين واختصار الناتج
# apl-source:2
# Add fractions reduced
# apl-source:3
# Demonstrates: رياضيات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2022-fraction-add-reduced-lowest-terms.apl
# apl-source:6

# apl-source:7
# # البسط الجديد a*d+b*c والمقام b*d
# apl-source:8
# # ثم نقسم على القاسم المشترك
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
def قاسم(ا, ب):
  # apl-source:19
  while ب != 0:
    # apl-source:20
    ت = ب
    # apl-source:21
    ب = ا % ب
    # apl-source:22
    ا = ت
  # apl-source:23
  return ا
# apl-source:24

# apl-source:25
def اجمع(ن1, د1, ن2, د2):
  # apl-source:26
  ن = ن1 * د2 + ن2 * د1
  # apl-source:27
  د = د1 * د2
  # apl-source:28
  ق = قاسم(ن, د)
  # apl-source:29
  return [ن // ق, د // ق]
# apl-source:30

# apl-source:31
تأكد_يساوي(اجمع(1, 2, 1, 3), [5, 6], "نصف وثلث")
# apl-source:32
تأكد_يساوي(اجمع(1, 4, 1, 4), [1, 2], "ربعان")
# apl-source:33
تأكد_يساوي(اجمع(3, 4, 1, 4), [1, 1], "واحد")
# apl-source:34
