
# apl-source:1
# مثال 1221 — وزن هامينغ
# apl-source:2
# Hamming weight of integers
# apl-source:3
# Demonstrates: عمليات بتات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1221-hamming-weight-table.apl
# apl-source:6

# apl-source:7
# نزيل أدنى بت مضبوط في كل خطوة بعملية n و n-1
# apl-source:8
# ونعد الخطوات
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
def وزن(ن):
  # apl-source:19
  ع = 0
  # apl-source:20
  while ن > 0:
    # apl-source:21
    ن = ن & (ن - 1)
    # apl-source:22
    ع = ع + 1
  # apl-source:23
  return ع
# apl-source:24

# apl-source:25
تأكد_يساوي(وزن(0), 0, "صفر")
# apl-source:26
تأكد_يساوي(وزن(11), 3, "أحد عشر")
# apl-source:27
تأكد_يساوي(وزن(128), 1, "قوة اثنين")
# apl-source:28
تأكد_يساوي(وزن(2147483647), 31, "أقصى")
# apl-source:29
تأكد_يساوي(وزن(255), 8, "بايت")
# apl-source:30
