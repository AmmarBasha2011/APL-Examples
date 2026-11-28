
# apl-source:1
# مثال 5070 — موضع أول ظهور للحرف r
# apl-source:2
# Index of first r
# apl-source:3
# Demonstrates: منطق وتمارين
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/5070-first-index-r.apl
# apl-source:6

# apl-source:7
# نرجع -1 إن لم يوجد
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
  for ي in range(len(ن)):
    # apl-source:19
    if ن[ي] == "r":
      # apl-source:20
      return ي
  # apl-source:21
  return -1
# apl-source:22

# apl-source:23
تأكد_يساوي(ف("banana"), -1, "حالة 1")
# apl-source:24
تأكد_يساوي(ف("education"), -1, "حالة 2")
# apl-source:25
تأكد_يساوي(ف(""), -1, "حالة 3")
# apl-source:26
تأكد_يساوي(ف("sky"), -1, "حالة 4")
# apl-source:27
