
# apl-source:1
# مثال 1834 — الجذر التربيعي الصحيح
# apl-source:2
# Integer square root by binary search
# apl-source:3
# Demonstrates: بحث
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1834-integer-sqrt-binary-search.apl
# apl-source:6

# apl-source:7
# نبحث بين 0 و ن
# apl-source:8
# نوسع حتى يتجاوز المربع
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
  يسار = 0
  # apl-source:20
  يمين = ن
  # apl-source:21
  نتيجة = 0
  # apl-source:22
  while يسار <= يمين:
    # apl-source:23
    وسط = (يسار + يمين) // 2
    # apl-source:24
    if وسط * وسط <= ن:
      # apl-source:25
      نتيجة = وسط
      # apl-source:26
      يسار = وسط + 1
    # apl-source:27
    else:
      # apl-source:28
      يمين = وسط - 1
  # apl-source:29
  return نتيجة
# apl-source:30

# apl-source:31
تأكد_يساوي(جذر_صحيح(16), 4, "مربع كامل")
# apl-source:32
تأكد_يساوي(جذر_صحيح(15), 3, "غير كامل")
# apl-source:33
تأكد_يساوي(جذر_صحيح(0), 0, "صفر")
# apl-source:34
تأكد_يساوي(جذر_صحيح(1000000), 1000, "مليون")
# apl-source:35
