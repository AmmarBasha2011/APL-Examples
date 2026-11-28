
# apl-source:1
# مثال 5080 — حذف الحرف l من النص
# apl-source:2
# Remove letter l
# apl-source:3
# Demonstrates: منطق وتمارين
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/5080-remove-char-l.apl
# apl-source:6

# apl-source:7
# نبني نصاً جديداً بدون الحرف
# apl-source:8

# apl-source:9
def تأكد_يساوي(فعلي, متوقع, اسم):
  # apl-source:10
  if فعلي != متوقع:
    # apl-source:11
    print("فشل:", اسم)
    # apl-source:12
    print("  متوقع:", متوقع)
    # apl-source:13
    print("  فعلي:", فعلي)
    # apl-source:14
    قياسي_نظام_اخرج(1)
  # apl-source:15
  print("ناجح:", اسم)
# apl-source:16

# apl-source:17
def ف(ن):
  # apl-source:18
  ر = ""
  # apl-source:19
  for ح in ن:
    # apl-source:20
    if ح != "l":
      # apl-source:21
      ر = ر + ح
  # apl-source:22
  return ر
# apl-source:23

# apl-source:24
تأكد_يساوي(ف("banana"), "banana", "حالة 1")
# apl-source:25
تأكد_يساوي(ف("education"), "education", "حالة 2")
# apl-source:26
تأكد_يساوي(ف(""), "", "حالة 3")
# apl-source:27
تأكد_يساوي(ف("mississippi"), "mississippi", "حالة 4")
# apl-source:28
