
# apl-source:1
# مثال 1341 — عد حروف العلة المرتبة
# apl-source:2
# Count sorted vowel strings
# apl-source:3
# Demonstrates: برمجة ديناميكية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1341-count-sorted-vowels.apl
# apl-source:6

# apl-source:7
# نبدأ بواحد لكل حرف علة
# apl-source:8
# كل خطوة تجمع تراكمياً
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
def عد_مرتبة(ن):
  # apl-source:19
  ع = [1, 1, 1, 1, 1]
  # apl-source:20
  for خطوة in range(ن - 1):
    # apl-source:21
    for ج in range(1, 5):
      # apl-source:22
      ع[ج] = ع[ج] + ع[ج - 1]
  # apl-source:23
  مجموع = 0
  # apl-source:24
  for ق in ع:
    # apl-source:25
    مجموع = مجموع + ق
  # apl-source:26
  return مجموع
# apl-source:27

# apl-source:28
تأكد_يساوي(عد_مرتبة(1), 5, "طول واحد")
# apl-source:29
تأكد_يساوي(عد_مرتبة(2), 15, "طول اثنين")
# apl-source:30
تأكد_يساوي(عد_مرتبة(33), 66045, "طول كبير")
# apl-source:31
