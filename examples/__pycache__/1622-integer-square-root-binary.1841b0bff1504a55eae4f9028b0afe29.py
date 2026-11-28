
# apl-source:1
# مثال 1622 — الجذر التربيعي الصحيح
# apl-source:2
# Integer square root by binary search
# apl-source:3
# Demonstrates: بحث ثنائي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1622-integer-square-root-binary.apl
# apl-source:6

# apl-source:7
# نبحث بين صفر والعدد
# apl-source:8
# نحفظ آخر قيمة مربعها مناسب
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
def جذر_صحيح(ن):
  # apl-source:19
  ي = 0
  # apl-source:20
  ج = ن
  # apl-source:21
  نتيجة = 0
  # apl-source:22
  while ي <= ج:
    # apl-source:23
    م = (ي + ج) // 2
    # apl-source:24
    if م * م <= ن:
      # apl-source:25
      نتيجة = م
      # apl-source:26
      ي = م + 1
    # apl-source:27
    else:
      # apl-source:28
      ج = م - 1
  # apl-source:29
  return نتيجة
# apl-source:30

# apl-source:31
تأكد_يساوي(جذر_صحيح(0), 0, "صفر")
# apl-source:32
تأكد_يساوي(جذر_صحيح(8), 2, "ثمانية")
# apl-source:33
تأكد_يساوي(جذر_صحيح(16), 4, "مربع كامل")
# apl-source:34
تأكد_يساوي(جذر_صحيح(1000000), 1000, "مليون")
# apl-source:35
