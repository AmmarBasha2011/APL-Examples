
# apl-source:1
# مثال 1698 — من عدد إلى أرقام رومانية
# apl-source:2
# Integer to Roman numeral
# apl-source:3
# Demonstrates: ترميز
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1698-integer-to-roman-numeral.apl
# apl-source:6

# apl-source:7
# جدول القيم والرموز
# apl-source:8
# نكرر الأكبر المناسب
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
def لعدد_روماني(ن):
  # apl-source:19
  قيم = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
  # apl-source:20
  رموز = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
  # apl-source:21
  ناتج = ""
  # apl-source:22
  for ك in range(len(قيم)):
    # apl-source:23
    while ن >= قيم[ك]:
      # apl-source:24
      ناتج = ناتج + رموز[ك]
      # apl-source:25
      ن = ن - قيم[ك]
  # apl-source:26
  return ناتج
# apl-source:27

# apl-source:28
تأكد_يساوي(لعدد_روماني(9), "IX", "تسعة")
# apl-source:29
تأكد_يساوي(لعدد_روماني(58), "LVIII", "ثمانية وخمسون")
# apl-source:30
تأكد_يساوي(لعدد_روماني(1994), "MCMXCIV", "1994")
# apl-source:31
