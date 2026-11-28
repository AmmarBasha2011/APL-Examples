
# apl-source:1
# مثال 1399 — فرق مجموع المربعات
# apl-source:2
# Sum square difference
# apl-source:3
# Demonstrates: رياضيات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1399-sum-square-difference.apl
# apl-source:6

# apl-source:7
# نحسب الاثنين بالصيغ المغلقة
# apl-source:8
# ونطرح
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
def فرق_مربعات(ن):
  # apl-source:19
  مجموع = ن * (ن + 1) // 2
  # apl-source:20
  مربعات = ن * (ن + 1) * (2 * ن + 1) // 6
  # apl-source:21
  return مجموع * مجموع - مربعات
# apl-source:22

# apl-source:23
تأكد_يساوي(فرق_مربعات(1), 0, "واحد")
# apl-source:24
تأكد_يساوي(فرق_مربعات(10), 2640, "عشرة")
# apl-source:25
تأكد_يساوي(فرق_مربعات(100), 25164150, "مئة")
# apl-source:26
