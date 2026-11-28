
# apl-source:1
# مثال 1515 — الإضافة على التكلفة والهامش
# apl-source:2
# Markup versus margin
# apl-source:3
# Demonstrates: مالية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1515-markup-vs-margin.apl
# apl-source:6

# apl-source:7
# الزيادة تُحسب من التكلفة
# apl-source:8
# الهامش يُحسب من سعر البيع
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
def الزيادة(تكلفة, سعر):
  # apl-source:19
  return (سعر - تكلفة) * 100 / تكلفة
# apl-source:20

# apl-source:21
def الهامش(تكلفة, سعر):
  # apl-source:22
  return (سعر - تكلفة) * 100 / سعر
# apl-source:23

# apl-source:24
تأكد_يساوي(الزيادة(80, 100), 25.0, "زيادة")
# apl-source:25
تأكد_يساوي(الهامش(80, 100), 20.0, "هامش")
# apl-source:26
تأكد_يساوي(الزيادة(50, 50), 0.0, "بلا ربح")
# apl-source:27
