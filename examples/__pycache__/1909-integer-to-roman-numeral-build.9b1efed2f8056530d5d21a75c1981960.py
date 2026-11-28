
# apl-source:1
# مثال 1909 — تحويل عدد لأرقام رومانية
# apl-source:2
# Convert integer to Roman numeral
# apl-source:3
# Demonstrates: تحويل
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1909-integer-to-roman-numeral-build.apl
# apl-source:6

# apl-source:7
# جدول قيم من الأكبر للأصغر
# apl-source:8
# نكرر الرمز طالما القيمة تتسع
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
def الى_روماني(ن):
  # apl-source:19
  قيم = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
  # apl-source:20
  رموز = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
  # apl-source:21
  خرج = ""
  # apl-source:22
  for ك in range(len(قيم)):
    # apl-source:23
    while ن >= قيم[ك]:
      # apl-source:24
      خرج = خرج + رموز[ك]
      # apl-source:25
      ن = ن - قيم[ك]
  # apl-source:26
  return خرج
# apl-source:27

# apl-source:28
تأكد_يساوي(الى_روماني(4), "IV", "أربعة")
# apl-source:29
تأكد_يساوي(الى_روماني(58), "LVIII", "٥٨")
# apl-source:30
تأكد_يساوي(الى_روماني(1994), "MCMXCIV", "١٩٩٤")
# apl-source:31
