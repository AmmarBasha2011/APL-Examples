
# apl-source:1
# مثال 1042 — الجذر الصحيح
# apl-source:2
# Integer square root by binary search
# apl-source:3
# Demonstrates: بحث ثنائي على الجواب
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1042-integer-sqrt.apl
# apl-source:6

# apl-source:7
# الجواب بين صفر والعدد نفسه
# apl-source:8
# نبحث عن أكبر ج يحقق ج×ج ≤ ن
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
def جذر_ص(ن):
  # apl-source:19
  ي = 0
  # apl-source:20
  ل = ن
  # apl-source:21
  افضل = 0
  # apl-source:22
  while ي <= ل:
    # apl-source:23
    وسط = (ي + ل) // 2
    # apl-source:24
    if (وسط * وسط) <= ن:
      # apl-source:25
      افضل = وسط
      # apl-source:26
      ي = وسط + 1
    # apl-source:27
    else:
      # apl-source:28
      ل = وسط - 1
  # apl-source:29
  return افضل
# apl-source:30

# apl-source:31
تأكد_يساوي(جذر_ص(0), 0, "صفر")
# apl-source:32
تأكد_يساوي(جذر_ص(8), 2, "ثمانية")
# apl-source:33
تأكد_يساوي(جذر_ص(16), 4, "مربع كامل")
# apl-source:34
تأكد_يساوي(جذر_ص(1000000), 1000, "مليون")
# apl-source:35
تأكد_يساوي(جذر_ص(99), 9, "تسعة وتسعون")
# apl-source:36
