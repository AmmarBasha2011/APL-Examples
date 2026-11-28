
# apl-source:1
# مثال 2025 — عدد حدود متتالية فاري
# apl-source:2
# Farey sequence length
# apl-source:3
# Demonstrates: نظرية الأعداد
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2025-farey-sequence-term-count.apl
# apl-source:6

# apl-source:7
# # نبدأ بالكسر 0/1 ثم 1/n
# apl-source:8
# # ونولد الحدود حتى 1/1
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
def طول_فاري(ن):
  # apl-source:19
  ا = 0
  # apl-source:20
  ب = 1
  # apl-source:21
  ج = 1
  # apl-source:22
  د = ن
  # apl-source:23
  عدد = 1
  # apl-source:24
  while ج <= ن:
    # apl-source:25
    ك = (ن + ب) // د
    # apl-source:26
    ت1 = ج
    # apl-source:27
    ت2 = د
    # apl-source:28
    ج = ك * ج - ا
    # apl-source:29
    د = ك * د - ب
    # apl-source:30
    ا = ت1
    # apl-source:31
    ب = ت2
    # apl-source:32
    عدد = عدد + 1
  # apl-source:33
  return عدد
# apl-source:34

# apl-source:35
تأكد_يساوي(طول_فاري(1), 2, "ف١")
# apl-source:36
تأكد_يساوي(طول_فاري(5), 11, "ف٥")
# apl-source:37
تأكد_يساوي(طول_فاري(6), 13, "ف٦")
# apl-source:38
تأكد_يساوي(طول_فاري(10), 33, "ف١٠")
# apl-source:39
