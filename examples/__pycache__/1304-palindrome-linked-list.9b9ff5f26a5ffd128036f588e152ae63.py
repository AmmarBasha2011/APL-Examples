
# apl-source:1
# مثال 1304 — قائمة متناظرة
# apl-source:2
# Palindrome list check
# apl-source:3
# Demonstrates: مؤشران
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1304-palindrome-linked-list.apl
# apl-source:6

# apl-source:7
# ننسخ النصف الثاني معكوساً
# apl-source:8
# ونقارنه بالنصف الأول
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
def متناظرة(قيم):
  # apl-source:19
  ن = len(قيم)
  # apl-source:20
  نصف = ن // 2
  # apl-source:21
  اول = قيم[:نصف]
  # apl-source:22
  ثان = قيم[ن - نصف:]
  # apl-source:23
  ثان.reverse()
  # apl-source:24
  return اول == ثان
# apl-source:25

# apl-source:26
تأكد_يساوي(متناظرة([1,2,2,1]), True, "زوجي")
# apl-source:27
تأكد_يساوي(متناظرة([1,2,3,2,1]), True, "فردي")
# apl-source:28
تأكد_يساوي(متناظرة([1,2]), False, "غير متناظرة")
# apl-source:29
تأكد_يساوي(متناظرة([]), True, "فارغة")
# apl-source:30
