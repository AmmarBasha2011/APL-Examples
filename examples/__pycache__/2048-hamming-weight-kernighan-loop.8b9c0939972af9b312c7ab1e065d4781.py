
# apl-source:1
# مثال 2048 — عدد البتات الواحدة بطريقة كيرنيغان
# apl-source:2
# Kernighan bit count
# apl-source:3
# Demonstrates: بتات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2048-hamming-weight-kernighan-loop.apl
# apl-source:6

# apl-source:7
# # العملية n & (n - 1) تزيل أقل بت واحد
# apl-source:8
# # فنعد الخطوات
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
  عدد = 0
  # apl-source:20
  while ن != 0:
    # apl-source:21
    ن = ن & (ن - 1)
    # apl-source:22
    عدد = عدد + 1
  # apl-source:23
  return عدد
# apl-source:24

# apl-source:25
تأكد_يساوي(وزن(11), 3, "١١")
# apl-source:26
تأكد_يساوي(وزن(128), 1, "١٢٨")
# apl-source:27
تأكد_يساوي(وزن(255), 8, "٢٥٥")
# apl-source:28
تأكد_يساوي(وزن(0), 0, "صفر")
# apl-source:29
