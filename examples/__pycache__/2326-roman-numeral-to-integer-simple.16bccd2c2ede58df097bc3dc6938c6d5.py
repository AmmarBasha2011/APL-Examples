
# apl-source:1
# مثال 2326 — روماني إلى عدد
# apl-source:2
# Roman numeral to integer
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2326-roman-numeral-to-integer-simple.apl
# apl-source:6

# apl-source:7
# # ندخل النص
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
  ق = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
  # apl-source:20
  م = 0
  # apl-source:21
  for ي in range(len(ن)):
    # apl-source:22
    if ي + 1 < len(ن) and ق[ن[ي]] < ق[ن[ي + 1]]:
      # apl-source:23
      م = م - ق[ن[ي]]
    # apl-source:24
    else:
      # apl-source:25
      م = م + ق[ن[ي]]
  # apl-source:26
  return م
# apl-source:27

# apl-source:28
تأكد_يساوي(ف("III"), 3, "حالة 1")
# apl-source:29
تأكد_يساوي(ف("IV"), 4, "حالة 2")
# apl-source:30
تأكد_يساوي(ف("IX"), 9, "حالة 3")
# apl-source:31
تأكد_يساوي(ف("LVIII"), 58, "حالة 4")
# apl-source:32
تأكد_يساوي(ف("MCMXCIV"), 1994, "حالة 5")
# apl-source:33
