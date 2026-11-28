
# apl-source:1
# مثال 1405 — أصغر عدد وحدات يقبل القسمة
# apl-source:2
# Smallest repunit divisible by k
# apl-source:3
# Demonstrates: رياضيات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1405-smallest-repunit-divisor.apl
# apl-source:6

# apl-source:7
# الأعداد التي كل أرقامها واحد
# apl-source:8
# نحدث الباقي فقط دون بناء العدد
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
def طول_الوحدات(ك):
  # apl-source:19
  if (ك % 2 == 0) or (ك % 5 == 0):
    # apl-source:20
    return -1
  # apl-source:21
  باقي = 1 % ك
  # apl-source:22
  ن = 1
  # apl-source:23
  while باقي != 0:
    # apl-source:24
    باقي = (باقي * 10 + 1) % ك
    # apl-source:25
    ن = ن + 1
  # apl-source:26
  return ن
# apl-source:27

# apl-source:28
تأكد_يساوي(طول_الوحدات(7), 6, "سبعة")
# apl-source:29
تأكد_يساوي(طول_الوحدات(3), 3, "ثلاثة")
# apl-source:30
تأكد_يساوي(طول_الوحدات(41), 5, "واحد وأربعون")
# apl-source:31
تأكد_يساوي(طول_الوحدات(10), -1, "عشرة")
# apl-source:32
