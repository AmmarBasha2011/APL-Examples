
# apl-source:1
# مثال 1395 — مجموع أرقام قوة
# apl-source:2
# Sum of digits of a power
# apl-source:3
# Demonstrates: رياضيات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1395-power-digit-sum.apl
# apl-source:6

# apl-source:7
# الأعداد الكبيرة تعمل مباشرة
# apl-source:8
# نحول إلى نص ونجمع الأرقام
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
def مجموع_أرقام(ن):
  # apl-source:19
  م = 0
  # apl-source:20
  for ح in str(ن):
    # apl-source:21
    م = م + int(ح)
  # apl-source:22
  return م
# apl-source:23

# apl-source:24
def مجموع_قوة(أساس, قوة):
  # apl-source:25
  return مجموع_أرقام(أساس ** قوة)
# apl-source:26

# apl-source:27
تأكد_يساوي(مجموع_قوة(2, 15), 26, "اثنان أس خمسة عشر")
# apl-source:28
تأكد_يساوي(مجموع_قوة(2, 1000), 1366, "اثنان أس ألف")
# apl-source:29
تأكد_يساوي(مجموع_قوة(10, 5), 1, "عشرة")
# apl-source:30
