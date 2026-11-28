
# apl-source:1
# مثال 1356 — برج الشمبانيا
# apl-source:2
# Champagne tower
# apl-source:3
# Demonstrates: محاكاة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1356-champagne-tower.apl
# apl-source:6

# apl-source:7
# نصب السائل في الكأس الأعلى
# apl-source:8
# الفائض يتوزع بالتساوي على الكأسين تحته
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
def كأس_الشمبانيا(سكب, صف, عمود):
  # apl-source:19
  برج = []
  # apl-source:20
  for ع in range(صف + 2):
    # apl-source:21
    برج = برج + [[0.0] * (ع + 2)]
  # apl-source:22
  برج[0][0] = سكب * 1.0
  # apl-source:23
  for ع in range(صف + 1):
    # apl-source:24
    for ج in range(ع + 1):
      # apl-source:25
      فائض = (برج[ع][ج] - 1.0) / 2.0
      # apl-source:26
      if فائض > 0:
        # apl-source:27
        برج[ع + 1][ج] = برج[ع + 1][ج] + فائض
        # apl-source:28
        برج[ع + 1][ج + 1] = برج[ع + 1][ج + 1] + فائض
  # apl-source:29
  return min(1.0, برج[صف][عمود])
# apl-source:30

# apl-source:31
تأكد_يساوي(كأس_الشمبانيا(1, 1, 1), 0.0, "لا يصل")
# apl-source:32
تأكد_يساوي(كأس_الشمبانيا(2, 1, 1), 0.5, "نصف كأس")
# apl-source:33
تأكد_يساوي(كأس_الشمبانيا(100000009, 33, 17), 1.0, "ممتلئ")
# apl-source:34
