
# apl-source:1
# مثال 1923 — كتابة عدد بالكلمات الإنجليزية
# apl-source:2
# Number to English words
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1923-spell-number-english-under-thousand.apl
# apl-source:6

# apl-source:7
# جدول للأعداد حتى ١٩
# apl-source:8
# جدول للعشرات
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
def كلمات(ن):
  # apl-source:19
  صغير = ["zero","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
  # apl-source:20
  عشرات = ["","","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
  # apl-source:21
  if ن < 20:
    # apl-source:22
    return صغير[ن]
  # apl-source:23
  if ن < 100:
    # apl-source:24
    if ن % 10 == 0:
      # apl-source:25
      return عشرات[ن // 10]
    # apl-source:26
    return عشرات[ن // 10] + "-" + صغير[ن % 10]
  # apl-source:27
  if ن % 100 == 0:
    # apl-source:28
    return صغير[ن // 100] + " hundred"
  # apl-source:29
  return صغير[ن // 100] + " hundred " + كلمات(ن % 100)
# apl-source:30

# apl-source:31
تأكد_يساوي(كلمات(7), "seven", "آحاد")
# apl-source:32
تأكد_يساوي(كلمات(42), "forty-two", "عشرات")
# apl-source:33
تأكد_يساوي(كلمات(300), "three hundred", "مئات")
# apl-source:34
تأكد_يساوي(كلمات(115), "one hundred fifteen", "مختلط")
# apl-source:35
