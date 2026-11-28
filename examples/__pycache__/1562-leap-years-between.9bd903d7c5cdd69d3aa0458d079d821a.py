
# apl-source:1
# مثال 1562 — عدد السنوات الكبيسة بين سنتين
# apl-source:2
# Count leap years in a range
# apl-source:3
# Demonstrates: وقت
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1562-leap-years-between.apl
# apl-source:6

# apl-source:7
# عدد الكبائس حتى س = س÷4 ناقص س÷100 زائد س÷400
# apl-source:8
# نطرح العد قبل البداية
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
def كبائس_حتى(س):
  # apl-source:19
  return س // 4 - س // 100 + س // 400
# apl-source:20

# apl-source:21
def كبائس_بين(من_سنة, إلى_سنة):
  # apl-source:22
  return كبائس_حتى(إلى_سنة) - كبائس_حتى(من_سنة - 1)
# apl-source:23

# apl-source:24
تأكد_يساوي(كبائس_بين(2000, 2000), 1, "سنة كبيسة")
# apl-source:25
تأكد_يساوي(كبائس_بين(1900, 1900), 0, "مئوية غير كبيسة")
# apl-source:26
تأكد_يساوي(كبائس_بين(2001, 2024), 6, "ربع قرن")
# apl-source:27
تأكد_يساوي(كبائس_بين(1996, 2004), 3, "عقد")
# apl-source:28
