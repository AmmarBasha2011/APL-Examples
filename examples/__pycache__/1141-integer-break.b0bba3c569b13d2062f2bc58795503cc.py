
# apl-source:1
# مثال 1141 — تجزئة عدد
# apl-source:2
# Integer break maximum product
# apl-source:3
# Demonstrates: برمجة ديناميكية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1141-integer-break.apl
# apl-source:6

# apl-source:7
# أفضل الأجزاء هي أثلاث
# apl-source:8
# لكن نجرب كل تجزئة بالبرمجة الديناميكية
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
def اكبر_ضرب(ن):
  # apl-source:19
  د = [0] * (ن + 1)
  # apl-source:20
  د[1] = 1
  # apl-source:21
  for ع in range(2, ن + 1):
    # apl-source:22
    اق = 0
    # apl-source:23
    for ج in range(1, ع):
      # apl-source:24
      ا = ج * (ع - ج)
      # apl-source:25
      ب = ج * د[ع - ج]
      # apl-source:26
      if ا > اق:
        # apl-source:27
        اق = ا
      # apl-source:28
      if ب > اق:
        # apl-source:29
        اق = ب
    # apl-source:30
    د[ع] = اق
  # apl-source:31
  return د[ن]
# apl-source:32

# apl-source:33
تأكد_يساوي(اكبر_ضرب(2), 1, "اثنان")
# apl-source:34
تأكد_يساوي(اكبر_ضرب(10), 36, "عشرة")
# apl-source:35
تأكد_يساوي(اكبر_ضرب(6), 9, "ستة")
# apl-source:36
تأكد_يساوي(اكبر_ضرب(8), 18, "ثمانية")
# apl-source:37
