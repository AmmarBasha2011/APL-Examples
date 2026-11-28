
# apl-source:1
# مثال 4838 — فائدة بسيطة بنسبة 10%
# apl-source:2
# Simple interest at 10 percent
# apl-source:3
# Demonstrates: مالية وهندسة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/4838-simple-interest-10.apl
# apl-source:6

# apl-source:7
# الفائدة = المبلغ × النسبة × السنوات ÷ 100
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
def ف(م, س):
  # apl-source:18
  return م * 10 * س // 100
# apl-source:19

# apl-source:20
تأكد_يساوي(ف(1000, 1), 100, "حالة 1")
# apl-source:21
تأكد_يساوي(ف(2500, 3), 750, "حالة 2")
# apl-source:22
تأكد_يساوي(ف(100, 10), 100, "حالة 3")
# apl-source:23
تأكد_يساوي(ف(8000, 2), 1600, "حالة 4")
# apl-source:24
