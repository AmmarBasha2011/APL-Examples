
# apl-source:1
# مثال 1514 — نقطة التعادل بالوحدات
# apl-source:2
# Break even units
# apl-source:3
# Demonstrates: مالية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1514-break-even-units.apl
# apl-source:6

# apl-source:7
# الهامش = سعر البيع - التكلفة المتغيرة
# apl-source:8
# نقسم التكلفة الثابتة على الهامش ونقرب لأعلى
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
def وحدات_التعادل(ثابتة, سعر, متغيرة):
  # apl-source:19
  هامش = سعر - متغيرة
  # apl-source:20
  if هامش <= 0:
    # apl-source:21
    return -1
  # apl-source:22
  return (ثابتة + هامش - 1) // هامش
# apl-source:23

# apl-source:24
تأكد_يساوي(وحدات_التعادل(1000, 50, 30), 50, "تقسيم تام")
# apl-source:25
تأكد_يساوي(وحدات_التعادل(1000, 45, 30), 67, "تقريب لأعلى")
# apl-source:26
تأكد_يساوي(وحدات_التعادل(1000, 30, 30), -1, "لا تعادل")
# apl-source:27
