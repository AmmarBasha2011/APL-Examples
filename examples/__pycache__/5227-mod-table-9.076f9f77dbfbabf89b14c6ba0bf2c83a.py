
# apl-source:1
# مثال 5227 — باقي القسمة على 9 لكل عنصر
# apl-source:2
# Remainders mod 9
# apl-source:3
# Demonstrates: تمارين متنوعة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/5227-mod-table-9.apl
# apl-source:6

# apl-source:7
# نطبق % على كل عنصر
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
    ر = ر + [خ % 9]
  # apl-source:21
  return ر
# apl-source:22

# apl-source:23
تأكد_يساوي(ف([0, 3, 6, 9, 12, 15, 18, 21, 24, 27]), [0, 3, 6, 0, 3, 6, 0, 3, 6, 0], "حالة 1")
# apl-source:24
تأكد_يساوي(ف([-1, -5, 7]), [8, 4, 7], "حالة 2")
# apl-source:25
تأكد_يساوي(ف([]), [], "حالة 3")
# apl-source:26
