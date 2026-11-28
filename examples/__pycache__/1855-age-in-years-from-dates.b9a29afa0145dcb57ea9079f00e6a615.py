
# apl-source:1
# مثال 1855 — العمر بالسنوات من التاريخ
# apl-source:2
# Age in years from birth date
# apl-source:3
# Demonstrates: وقت
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1855-age-in-years-from-dates.apl
# apl-source:6

# apl-source:7
# الفرق بين السنتين
# apl-source:8
# ننقص واحداً إن لم يأتِ عيد الميلاد
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
def العمر(مولد, اليوم):
  # apl-source:19
  عمر = اليوم[0] - مولد[0]
  # apl-source:20
  if اليوم[1] < مولد[1]:
    # apl-source:21
    عمر = عمر - 1
  # apl-source:22
  elif اليوم[1] == مولد[1] and اليوم[2] < مولد[2]:
    # apl-source:23
    عمر = عمر - 1
  # apl-source:24
  return عمر
# apl-source:25

# apl-source:26
تأكد_يساوي(العمر([2000, 9, 9], [2026, 11, 26]), 26, "بعد العيد")
# apl-source:27
تأكد_يساوي(العمر([2000, 12, 31], [2026, 11, 26]), 25, "قبل العيد")
# apl-source:28
تأكد_يساوي(العمر([2000, 11, 26], [2026, 11, 26]), 26, "يوم العيد")
# apl-source:29
