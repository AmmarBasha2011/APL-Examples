
# apl-source:1
# مثال 1535 — ضبط ومسح وقلب بت
# apl-source:2
# Set clear toggle a bit
# apl-source:3
# Demonstrates: بتات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1535-set-clear-toggle-bit.apl
# apl-source:6

# apl-source:7
# القناع هو واحد مزاح
# apl-source:8
# OR يضبط وAND مع المعكوس يمسح وXOR يقلب
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
def اضبط(ن, ب):
  # apl-source:19
  return ن | (1 << ب)
# apl-source:20

# apl-source:21
def امسح(ن, ب):
  # apl-source:22
  return ن & ((1 << ب) ^ 255)
# apl-source:23

# apl-source:24
def اقلب(ن, ب):
  # apl-source:25
  return ن ^ (1 << ب)
# apl-source:26

# apl-source:27
تأكد_يساوي(اضبط(0, 3), 8, "ضبط")
# apl-source:28
تأكد_يساوي(امسح(15, 1), 13, "مسح")
# apl-source:29
تأكد_يساوي(اقلب(5, 0), 4, "قلب أول")
# apl-source:30
تأكد_يساوي(اقلب(5, 1), 7, "قلب ثان")
# apl-source:31
