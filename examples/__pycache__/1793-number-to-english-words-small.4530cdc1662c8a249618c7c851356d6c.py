
# apl-source:1
# مثال 1793 — العدد بالكلمات الإنجليزية
# apl-source:2
# Number to English words under 100
# apl-source:3
# Demonstrates: ترميز
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1793-number-to-english-words-small.apl
# apl-source:6

# apl-source:7
# جداول للآحاد والعشرات
# apl-source:8
# نربط العشرة بالوحدة
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
def بالكلمات(ن):
  # apl-source:19
  آحاد = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
  # apl-source:20
  عشرات = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
  # apl-source:21
  if ن < 20:
    # apl-source:22
    return آحاد[ن]
  # apl-source:23
  if ن % 10 == 0:
    # apl-source:24
    return عشرات[ن // 10]
  # apl-source:25
  return عشرات[ن // 10] + "-" + آحاد[ن % 10]
# apl-source:26

# apl-source:27
تأكد_يساوي(بالكلمات(7), "seven", "سبعة")
# apl-source:28
تأكد_يساوي(بالكلمات(40), "forty", "أربعون")
# apl-source:29
تأكد_يساوي(بالكلمات(99), "ninety-nine", "تسعة وتسعون")
# apl-source:30
تأكد_يساوي(بالكلمات(15), "fifteen", "خمسة عشر")
# apl-source:31
