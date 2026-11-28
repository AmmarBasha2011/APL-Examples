
# apl-source:1
# مثال 2185 — خطوات كولاتز
# apl-source:2
# Collatz steps to one
# apl-source:3
# Demonstrates: أرقام
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2185-collatz-steps-to-one-count.apl
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
  خ = 0
  # apl-source:20
  while ن != 1:
    # apl-source:21
    if ن % 2 == 0:
      # apl-source:22
      ن = ن // 2
    # apl-source:23
    else:
      # apl-source:24
      ن = 3 * ن + 1
    # apl-source:25
    خ = خ + 1
  # apl-source:26
  return خ
# apl-source:27

# apl-source:28
تأكد_يساوي(ف(1), 0, "حالة 1")
# apl-source:29
تأكد_يساوي(ف(6), 8, "حالة 6")
# apl-source:30
تأكد_يساوي(ف(7), 16, "حالة 7")
# apl-source:31
تأكد_يساوي(ف(27), 111, "حالة 27")
# apl-source:32
