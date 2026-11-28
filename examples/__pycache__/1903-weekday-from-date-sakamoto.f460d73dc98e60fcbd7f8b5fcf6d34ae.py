
# apl-source:1
# مثال 1903 — يوم الأسبوع من التاريخ
# apl-source:2
# Weekday from a date
# apl-source:3
# Demonstrates: تاريخ
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1903-weekday-from-date-sakamoto.apl
# apl-source:6

# apl-source:7
# جدول ثابت لكل شهر
# apl-source:8
# الناتج صفر للأحد وواحد للاثنين
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
def يوم_الاسبوع(س, ش, ي):
  # apl-source:19
  ج = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
  # apl-source:20
  if ش < 3:
    # apl-source:21
    س = س - 1
  # apl-source:22
  return (س + س // 4 - س // 100 + س // 400 + ج[ش - 1] + ي) % 7
# apl-source:23

# apl-source:24
تأكد_يساوي(يوم_الاسبوع(2024, 1, 1), 1, "الاثنين")
# apl-source:25
تأكد_يساوي(يوم_الاسبوع(2000, 1, 1), 6, "السبت")
# apl-source:26
تأكد_يساوي(يوم_الاسبوع(2023, 12, 31), 0, "الأحد")
# apl-source:27
