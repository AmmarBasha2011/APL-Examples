
# apl-source:1
# مثال 2183 — عدد العوامل الأولية المختلفة
# apl-source:2
# Distinct prime factors count
# apl-source:3
# Demonstrates: أرقام
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2183-count-distinct-prime-factors.apl
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
  د = 2
  # apl-source:20
  ع = 0
  # apl-source:21
  while ن > 1:
    # apl-source:22
    if ن % د == 0:
      # apl-source:23
      ع = ع + 1
      # apl-source:24
      while ن % د == 0:
        # apl-source:25
        ن = ن // د
    # apl-source:26
    د = د + 1
  # apl-source:27
  return ع
# apl-source:28

# apl-source:29
تأكد_يساوي(ف(2), 1, "حالة 2")
# apl-source:30
تأكد_يساوي(ف(12), 2, "حالة 12")
# apl-source:31
تأكد_يساوي(ف(30), 3, "حالة 30")
# apl-source:32
تأكد_يساوي(ف(210), 4, "حالة 210")
# apl-source:33
تأكد_يساوي(ف(64), 1, "حالة 64")
# apl-source:34
