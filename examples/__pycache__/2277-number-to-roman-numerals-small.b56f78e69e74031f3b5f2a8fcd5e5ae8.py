
# apl-source:1
# مثال 2277 — تحويل لأرقام رومانية
# apl-source:2
# Number to Roman numerals
# apl-source:3
# Demonstrates: أرقام
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2277-number-to-roman-numerals-small.apl
# apl-source:6

# apl-source:7
# # ندخل القيم
# apl-source:8
# # ونقارن النتيجة
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
def ف(ن):
  # apl-source:19
  ق = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
  # apl-source:20
  ر = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
  # apl-source:21
  خ = ""
  # apl-source:22
  for ي in range(13):
    # apl-source:23
    while ن >= ق[ي]:
      # apl-source:24
      خ = خ + ر[ي]
      # apl-source:25
      ن = ن - ق[ي]
  # apl-source:26
  return خ
# apl-source:27

# apl-source:28
تأكد_يساوي(ف(4), "IV", "حالة 1")
# apl-source:29
تأكد_يساوي(ف(9), "IX", "حالة 2")
# apl-source:30
تأكد_يساوي(ف(14), "XIV", "حالة 3")
# apl-source:31
تأكد_يساوي(ف(58), "LVIII", "حالة 4")
# apl-source:32
تأكد_يساوي(ف(1994), "MCMXCIV", "حالة 5")
# apl-source:33
تأكد_يساوي(ف(3999), "MMMCMXCIX", "حالة 6")
# apl-source:34
