
# apl-source:1
# مثال 4893 — اليوم بعد 2 أيام
# apl-source:2
# Weekday 2 days later
# apl-source:3
# Demonstrates: مالية وهندسة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/4893-week-day-shift-2.apl
# apl-source:6

# apl-source:7
# أيام الأسبوع مرقمة من 0 إلى 6
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
def ف(ي):
  # apl-source:18
  return (ي + 2) % 7
# apl-source:19

# apl-source:20
تأكد_يساوي(ف(0), 2, "حالة 1")
# apl-source:21
تأكد_يساوي(ف(3), 5, "حالة 2")
# apl-source:22
تأكد_يساوي(ف(6), 1, "حالة 3")
# apl-source:23
تأكد_يساوي(ف(4), 6, "حالة 4")
# apl-source:24
