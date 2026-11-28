
# apl-source:1
# مثال 3365 — أعداد لها 24 قواسم
# apl-source:2
# Numbers with exactly 24 divisors
# apl-source:3
# Demonstrates: أرقام
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/3365-count-numbers-with-exactly-24-divisors-below-limit.apl
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
  ك = 0
  # apl-source:20
  for ي in range(1, ن):
    # apl-source:21
    د = 0
    # apl-source:22
    for ج in range(1, ي + 1):
      # apl-source:23
      if ي % ج == 0:
        # apl-source:24
        د = د + 1
    # apl-source:25
    if د == 24:
      # apl-source:26
      ك = ك + 1
  # apl-source:27
  return ك
# apl-source:28

# apl-source:29
تأكد_يساوي(ف(10), 0, "حالة 1")
# apl-source:30
تأكد_يساوي(ف(30), 0, "حالة 2")
# apl-source:31
تأكد_يساوي(ف(60), 0, "حالة 3")
# apl-source:32
