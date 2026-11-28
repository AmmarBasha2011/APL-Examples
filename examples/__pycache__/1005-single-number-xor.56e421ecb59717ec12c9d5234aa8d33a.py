
# apl-source:1
# مثال 1005 — العدد الوحيد
# apl-source:2
# Single number via XOR
# apl-source:3
# Demonstrates: خاصية XOR
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1005-single-number-xor.apl
# apl-source:6

# apl-source:7
# XOR لعدد مع نفسه صفر ومع الصفر العدد نفسه
# apl-source:8
# فتتلاشى الأزواج ويبقى الفرد
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
def وحيد(ق):
  # apl-source:19
  ن = 0
  # apl-source:20
  for ع in ق:
    # apl-source:21
    ن = ن ^ ع
  # apl-source:22
  return ن
# apl-source:23

# apl-source:24
تأكد_يساوي(وحيد([2, 2, 1]), 1, "ثلاثة عناصر")
# apl-source:25
تأكد_يساوي(وحيد([4, 1, 2, 1, 2]), 4, "خمسة عناصر")
# apl-source:26
تأكد_يساوي(وحيد([7]), 7, "عنصر واحد")
# apl-source:27
