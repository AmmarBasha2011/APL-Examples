
# apl-source:1
# مثال 1870 — سعر بشرائح الخصم
# apl-source:2
# Tiered discount price
# apl-source:3
# Demonstrates: مالية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1870-discount-tier-price-calc.apl
# apl-source:6

# apl-source:7
# نختار الشريحة بالكمية
# apl-source:8
# نطبق نسبة الخصم صحيحة
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
def السعر(كمية, سعر_الوحدة):
  # apl-source:19
  خصم = 0
  # apl-source:20
  if كمية >= 100:
    # apl-source:21
    خصم = 20
  # apl-source:22
  elif كمية >= 50:
    # apl-source:23
    خصم = 10
  # apl-source:24
  elif كمية >= 10:
    # apl-source:25
    خصم = 5
  # apl-source:26
  إجمالي = كمية * سعر_الوحدة
  # apl-source:27
  return إجمالي - إجمالي * خصم // 100
# apl-source:28

# apl-source:29
تأكد_يساوي(السعر(5, 10), 50, "بلا خصم")
# apl-source:30
تأكد_يساوي(السعر(10, 10), 95, "خمسة بالمئة")
# apl-source:31
تأكد_يساوي(السعر(50, 10), 450, "عشرة بالمئة")
# apl-source:32
تأكد_يساوي(السعر(100, 10), 800, "عشرون بالمئة")
# apl-source:33
