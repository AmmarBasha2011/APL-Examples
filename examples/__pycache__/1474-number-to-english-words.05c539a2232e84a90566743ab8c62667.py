
# apl-source:1
# مثال 1474 — رقم إلى كلمات إنجليزية
# apl-source:2
# Number to English words
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1474-number-to-english-words.apl
# apl-source:6

# apl-source:7
# نتعامل مع المئات ثم العشرات
# apl-source:8
# الآلاف تتكرر نفس القاعدة
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
def أقل_من_ألف(ن):
  # apl-source:19
  آحاد = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
  # apl-source:20
  عشرات = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
  # apl-source:21
  أجزاء = []
  # apl-source:22
  if ن >= 100:
    # apl-source:23
    أجزاء.append(آحاد[ن // 100])
    # apl-source:24
    أجزاء.append("hundred")
    # apl-source:25
    ن = ن % 100
  # apl-source:26
  if ن >= 20:
    # apl-source:27
    أجزاء.append(عشرات[ن // 10])
    # apl-source:28
    ن = ن % 10
  # apl-source:29
  if ن > 0:
    # apl-source:30
    أجزاء.append(آحاد[ن])
  # apl-source:31
  return " ".join(أجزاء)
# apl-source:32

# apl-source:33
def بالكلمات(ن):
  # apl-source:34
  if ن == 0:
    # apl-source:35
    return "zero"
  # apl-source:36
  if ن < 1000:
    # apl-source:37
    return أقل_من_ألف(ن)
  # apl-source:38
  باقي = ن % 1000
  # apl-source:39
  بداية = أقل_من_ألف(ن // 1000) + " thousand"
  # apl-source:40
  if باقي == 0:
    # apl-source:41
    return بداية
  # apl-source:42
  return بداية + " " + أقل_من_ألف(باقي)
# apl-source:43

# apl-source:44
تأكد_يساوي(بالكلمات(0), "zero", "صفر")
# apl-source:45
تأكد_يساوي(بالكلمات(42), "forty two", "اثنان وأربعون")
# apl-source:46
تأكد_يساوي(بالكلمات(315), "three hundred fifteen", "ثلاثمئة")
# apl-source:47
تأكد_يساوي(بالكلمات(2005), "two thousand five", "ألفان")
# apl-source:48
