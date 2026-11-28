
# apl-source:1
# مثال 1407 — مجموع القواسم
# apl-source:2
# Sum of divisors sigma function
# apl-source:3
# Demonstrates: رياضيات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1407-sum-of-divisors-sigma.apl
# apl-source:6

# apl-source:7
# نمر حتى الجذر التربيعي
# apl-source:8
# كل قاسم يعطي قاسماً مقابلاً
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
def سيغما(ن):
  # apl-source:19
  مجموع = 0
  # apl-source:20
  ع = 1
  # apl-source:21
  while ع * ع <= ن:
    # apl-source:22
    if ن % ع == 0:
      # apl-source:23
      مجموع = مجموع + ع
      # apl-source:24
      if ع * ع != ن:
        # apl-source:25
        مجموع = مجموع + ن // ع
    # apl-source:26
    ع = ع + 1
  # apl-source:27
  return مجموع
# apl-source:28

# apl-source:29
تأكد_يساوي(سيغما(1), 1, "واحد")
# apl-source:30
تأكد_يساوي(سيغما(12), 28, "اثنا عشر")
# apl-source:31
تأكد_يساوي(سيغما(28), 56, "عدد كامل")
# apl-source:32
تأكد_يساوي(سيغما(36), 91, "مربع كامل")
# apl-source:33
