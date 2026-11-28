
# apl-source:1
# مثال 1968 — مجموع صف مثلث باسكال قوى الاثنين
# apl-source:2
# Pascal row sums are powers of two
# apl-source:3
# Demonstrates: توافيق
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1968-pascal-triangle-row-sum-powers.apl
# apl-source:6

# apl-source:7
# # نبني كل صف من الصف السابق
# apl-source:8
# # ونتحقق من مجموعه
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
def صف_تالي(ص):
  # apl-source:19
  خرج = [1]
  # apl-source:20
  for ك in range(len(ص) - 1):
    # apl-source:21
    خرج = خرج + [ص[ك] + ص[ك + 1]]
  # apl-source:22
  return خرج + [1]
# apl-source:23

# apl-source:24
def مجموع_صف(ن):
  # apl-source:25
  ص = [1]
  # apl-source:26
  for ك in range(ن):
    # apl-source:27
    ص = صف_تالي(ص)
  # apl-source:28
  مج = 0
  # apl-source:29
  for ع in ص:
    # apl-source:30
    مج = مج + ع
  # apl-source:31
  return مج
# apl-source:32

# apl-source:33
تأكد_يساوي(مجموع_صف(0), 1, "الصف ٠")
# apl-source:34
تأكد_يساوي(مجموع_صف(5), 32, "الصف ٥")
# apl-source:35
تأكد_يساوي(مجموع_صف(10), 1024, "الصف ١٠")
# apl-source:36
تأكد_يساوي(صف_تالي([1, 3, 3, 1]), [1, 4, 6, 4, 1], "صف خمسة")
# apl-source:37
