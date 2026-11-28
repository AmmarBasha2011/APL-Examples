
# apl-source:1
# مثال 1531 — الأصفار في نهاية الثنائي
# apl-source:2
# Trailing zero bits
# apl-source:3
# Demonstrates: بتات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1531-trailing-zero-bits.apl
# apl-source:6

# apl-source:7
# نقسم على اثنين ما دام العدد زوجياً
# apl-source:8
# الصفر حالة خاصة
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
def أصفار_النهاية(ن):
  # apl-source:19
  if ن == 0:
    # apl-source:20
    return -1
  # apl-source:21
  عد = 0
  # apl-source:22
  while ن % 2 == 0:
    # apl-source:23
    ن = ن // 2
    # apl-source:24
    عد = عد + 1
  # apl-source:25
  return عد
# apl-source:26

# apl-source:27
تأكد_يساوي(أصفار_النهاية(8), 3, "ثمانية")
# apl-source:28
تأكد_يساوي(أصفار_النهاية(12), 2, "اثنا عشر")
# apl-source:29
تأكد_يساوي(أصفار_النهاية(7), 0, "فردي")
# apl-source:30
تأكد_يساوي(أصفار_النهاية(0), -1, "صفر")
# apl-source:31
