
# apl-source:1
# مثال 2087 — الأيام بين تاريخين برقم اليوم اليولياني
# apl-source:2
# Days between dates JDN
# apl-source:3
# Demonstrates: تواريخ
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2087-days-between-dates-julian-day-number.apl
# apl-source:6

# apl-source:7
# # الصيغة تعالج السنوات الكبيسة
# apl-source:8
# # الفرق يعطي عدد الأيام
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
def رقم_يوم(س, ش, ي):
  # apl-source:19
  ا = (14 - ش) // 12
  # apl-source:20
  س2 = س + 4800 - ا
  # apl-source:21
  ش2 = ش + 12 * ا - 3
  # apl-source:22
  return ي + (153 * ش2 + 2) // 5 + 365 * س2 + س2 // 4 - س2 // 100 + س2 // 400 - 32045
# apl-source:23

# apl-source:24
def فرق(ت1, ت2):
  # apl-source:25
  return رقم_يوم(ت2[0], ت2[1], ت2[2]) - رقم_يوم(ت1[0], ت1[1], ت1[2])
# apl-source:26

# apl-source:27
تأكد_يساوي(فرق([2000, 1, 1], [2000, 12, 31]), 365, "سنة كبيسة")
# apl-source:28
تأكد_يساوي(فرق([2024, 2, 28], [2024, 3, 1]), 2, "فبراير كبيس")
# apl-source:29
تأكد_يساوي(فرق([2023, 1, 1], [2024, 1, 1]), 365, "سنة عادية")
# apl-source:30
تأكد_يساوي(فرق([2024, 1, 1], [2024, 1, 1]), 0, "نفس اليوم")
# apl-source:31
