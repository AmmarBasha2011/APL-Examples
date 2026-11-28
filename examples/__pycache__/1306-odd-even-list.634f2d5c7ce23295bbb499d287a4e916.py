
# apl-source:1
# مثال 1306 — فردي وزوجي
# apl-source:2
# Odd even linked list regroup
# apl-source:3
# Demonstrates: إعادة ترتيب
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1306-odd-even-list.apl
# apl-source:6

# apl-source:7
# نجمع عناصر المواضع الفردية أولاً
# apl-source:8
# ثم عناصر المواضع الزوجية بنفس ترتيبها
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
def اعد_جمع(قيم):
  # apl-source:19
  فردي = []
  # apl-source:20
  زوجي = []
  # apl-source:21
  for ع in range(len(قيم)):
    # apl-source:22
    if ع % 2 == 0:
      # apl-source:23
      فردي = فردي + [قيم[ع]]
    # apl-source:24
    else:
      # apl-source:25
      زوجي = زوجي + [قيم[ع]]
  # apl-source:26
  return فردي + زوجي
# apl-source:27

# apl-source:28
تأكد_يساوي(اعد_جمع([1,2,3,4,5]), [1,3,5,2,4], "خمسة")
# apl-source:29
تأكد_يساوي(اعد_جمع([2,1,3,5,6,4,7]), [2,3,6,7,1,5,4], "سبعة")
# apl-source:30
تأكد_يساوي(اعد_جمع([]), [], "فارغة")
# apl-source:31
