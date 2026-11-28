
# apl-source:1
# مثال 1513 — الإهلاك بالقسط الثابت
# apl-source:2
# Straight line depreciation
# apl-source:3
# Demonstrates: مالية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1513-straight-line-depreciation.apl
# apl-source:6

# apl-source:7
# الإهلاك السنوي = (التكلفة - الخردة) ÷ العمر
# apl-source:8
# القيمة لا تنزل تحت الخردة
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
def قيمة_الأصل(تكلفة, خردة, عمر, سنوات):
  # apl-source:19
  if سنوات >= عمر:
    # apl-source:20
    return خردة
  # apl-source:21
  سنوي = (تكلفة - خردة) / عمر
  # apl-source:22
  return تكلفة - سنوي * سنوات
# apl-source:23

# apl-source:24
تأكد_يساوي(قيمة_الأصل(10000, 2000, 4, 1), 8000.0, "سنة")
# apl-source:25
تأكد_يساوي(قيمة_الأصل(10000, 2000, 4, 4), 2000, "نهاية العمر")
# apl-source:26
تأكد_يساوي(قيمة_الأصل(10000, 2000, 4, 9), 2000, "بعد العمر")
# apl-source:27
