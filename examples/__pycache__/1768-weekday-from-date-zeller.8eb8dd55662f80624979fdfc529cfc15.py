
# apl-source:1
# مثال 1768 — يوم الأسبوع بمعادلة زيلر
# apl-source:2
# Weekday from date by Zeller
# apl-source:3
# Demonstrates: وقت
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1768-weekday-from-date-zeller.apl
# apl-source:6

# apl-source:7
# الشهران يناير وفبراير يحسبان من السنة السابقة
# apl-source:8
# النتيجة صفر للسبت
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
def يوم_الأسبوع(س, ش, ي):
  # apl-source:19
  if ش < 3:
    # apl-source:20
    ش = ش + 12
    # apl-source:21
    س = س - 1
  # apl-source:22
  ك = س % 100
  # apl-source:23
  ج = س // 100
  # apl-source:24
  ه = (ي + (13 * (ش + 1)) // 5 + ك + ك // 4 + ج // 4 + 5 * ج) % 7
  # apl-source:25
  return ه
# apl-source:26

# apl-source:27
تأكد_يساوي(يوم_الأسبوع(2000, 1, 1), 0, "سبت")
# apl-source:28
تأكد_يساوي(يوم_الأسبوع(2024, 1, 1), 2, "اثنين")
# apl-source:29
تأكد_يساوي(يوم_الأسبوع(2023, 12, 25), 2, "ميلاد")
# apl-source:30
