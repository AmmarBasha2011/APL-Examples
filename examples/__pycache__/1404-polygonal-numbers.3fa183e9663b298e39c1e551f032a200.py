
# apl-source:1
# مثال 1404 — الأعداد المضلعة
# apl-source:2
# Polygonal numbers formula
# apl-source:3
# Demonstrates: رياضيات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1404-polygonal-numbers.apl
# apl-source:6

# apl-source:7
# الصيغة العامة ((ك-2)ن² - (ك-4)ن) / 2
# apl-source:8
# تغطي المثلثي والمربع والخماسي والسداسي
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
def مضلع(ك, ن):
  # apl-source:19
  return ((ك - 2) * ن * ن - (ك - 4) * ن) // 2
# apl-source:20

# apl-source:21
تأكد_يساوي(مضلع(3, 7), 28, "مثلثي")
# apl-source:22
تأكد_يساوي(مضلع(4, 5), 25, "مربع")
# apl-source:23
تأكد_يساوي(مضلع(5, 4), 22, "خماسي")
# apl-source:24
تأكد_يساوي(مضلع(6, 3), 15, "سداسي")
# apl-source:25
