
# apl-source:1
# مثال 5308 — ضرب كل عنصر في 17
# apl-source:2
# Scale list by 17
# apl-source:3
# Demonstrates: تمارين متنوعة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/5308-scale-list-17.apl
# apl-source:6

# apl-source:7
# قائمة جديدة بالقيم المضروبة
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
def ف(ق):
  # apl-source:18
  ر = []
  # apl-source:19
  for خ in ق:
    # apl-source:20
    ر = ر + [خ * 17]
  # apl-source:21
  return ر
# apl-source:22

# apl-source:23
تأكد_يساوي(ف([1, 2, 3]), [17, 34, 51], "حالة 1")
# apl-source:24
تأكد_يساوي(ف([]), [], "حالة 2")
# apl-source:25
تأكد_يساوي(ف([0, -4, 10]), [0, -68, 170], "حالة 3")
# apl-source:26
