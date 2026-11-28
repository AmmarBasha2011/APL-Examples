
# apl-source:1
# مثال 2098 — عدد الاضطرابات
# apl-source:2
# Derangements count
# apl-source:3
# Demonstrates: توافيق
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2098-derangement-count-recurrence.apl
# apl-source:6

# apl-source:7
# # D(n) = (n-1)(D(n-1)+D(n-2))
# apl-source:8
# # نحسب بالتتابع
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
def اضطراب(ن):
  # apl-source:19
  if ن == 0:
    # apl-source:20
    return 1
  # apl-source:21
  ا = 1
  # apl-source:22
  ب = 0
  # apl-source:23
  for ك in range(2, ن + 1):
    # apl-source:24
    ج = (ك - 1) * (ا + ب)
    # apl-source:25
    ا = ب
    # apl-source:26
    ب = ج
  # apl-source:27
  return ب
# apl-source:28

# apl-source:29
تأكد_يساوي(اضطراب(0), 1, "٠")
# apl-source:30
تأكد_يساوي(اضطراب(1), 0, "١")
# apl-source:31
تأكد_يساوي(اضطراب(4), 9, "٤")
# apl-source:32
تأكد_يساوي(اضطراب(6), 265, "٦")
# apl-source:33
