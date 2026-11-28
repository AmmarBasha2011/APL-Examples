
# apl-source:1
# مثال 1561 — ربع السنة
# apl-source:2
# Quarter of the year
# apl-source:3
# Demonstrates: وقت
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1561-quarter-of-year.apl
# apl-source:6

# apl-source:7
# كل ثلاثة أشهر ربع
# apl-source:8
# نستخدم القسمة الصحيحة
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
def الربع(شهر):
  # apl-source:19
  return (شهر - 1) // 3 + 1
# apl-source:20

# apl-source:21
تأكد_يساوي(الربع(1), 1, "يناير")
# apl-source:22
تأكد_يساوي(الربع(3), 1, "مارس")
# apl-source:23
تأكد_يساوي(الربع(4), 2, "أبريل")
# apl-source:24
تأكد_يساوي(الربع(12), 4, "ديسمبر")
# apl-source:25
