
# apl-source:1
# مثال 4733 — قراءة عدد مكتوب بالأساس 2
# apl-source:2
# Read a number written in base 2
# apl-source:3
# Demonstrates: أرقام وخوارزميات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/4733-from-base-2.apl
# apl-source:6

# apl-source:7
# نمر على الأرقام من اليسار
# apl-source:8
# ونضرب الناتج في الأساس ونضيف الرقم
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
def ف(س):
  # apl-source:19
  ن = 0
  # apl-source:20
  for خ in س:
    # apl-source:21
    ن = ن * 2 + int(خ)
  # apl-source:22
  return ن
# apl-source:23

# apl-source:24
تأكد_يساوي(ف("0"), 0, "حالة 1")
# apl-source:25
تأكد_يساوي(ف("1"), 1, "حالة 2")
# apl-source:26
تأكد_يساوي(ف("1001"), 9, "حالة 3")
# apl-source:27
تأكد_يساوي(ف("11110"), 30, "حالة 4")
# apl-source:28
تأكد_يساوي(ف("1001101"), 77, "حالة 5")
# apl-source:29
