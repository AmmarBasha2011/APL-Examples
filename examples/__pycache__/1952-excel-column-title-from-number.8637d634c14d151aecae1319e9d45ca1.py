
# apl-source:1
# مثال 1952 — اسم عمود إكسل من رقمه
# apl-source:2
# Excel column title from number
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1952-excel-column-title-from-number.apl
# apl-source:6

# apl-source:7
# # نطرح 1 قبل كل قسمة لأن الترقيم يبدأ من 1
# apl-source:8
# # ونبني الحروف من اليمين
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
def عنوان(ن):
  # apl-source:19
  خرج = ""
  # apl-source:20
  while ن > 0:
    # apl-source:21
    ن = ن - 1
    # apl-source:22
    خرج = chr(65 + ن % 26) + خرج
    # apl-source:23
    ن = ن // 26
  # apl-source:24
  return خرج
# apl-source:25

# apl-source:26
تأكد_يساوي(عنوان(1), "A", "أول")
# apl-source:27
تأكد_يساوي(عنوان(26), "Z", "آخر حرف")
# apl-source:28
تأكد_يساوي(عنوان(27), "AA", "بعد Z")
# apl-source:29
تأكد_يساوي(عنوان(701), "ZY", "٧٠١")
# apl-source:30
تأكد_يساوي(عنوان(703), "AAA", "ثلاثة")
# apl-source:31
