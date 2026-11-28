
# apl-source:1
# مثال 858 — المتتابعة الجزئية
# apl-source:2
# Aliquot sequence
# apl-source:3
# Demonstrates: قواسم ذاتية متكررة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/858-aliquot-sequence.apl
# apl-source:6

# apl-source:7
# المتتابعة الجزئية: كل حد هو مجموع القواسم الذاتية للسابق
# apl-source:8
# من 12: 12, 16, 15, 9, 4, 3, 1 ثم تنتهي
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
def مجموع_القواسم(ن):
  # apl-source:19
  مجموع = 0
  # apl-source:20
  for ق in range(1, ن):
    # apl-source:21
    if ن % ق == 0:
      # apl-source:22
      مجموع = مجموع + ق
  # apl-source:23
  return مجموع
# apl-source:24

# apl-source:25
def متتابعة_جزئية(بداية, حد_أقصى):
  # apl-source:26
  ت = [بداية]
  # apl-source:27
  while ت[len(ت) - 1] > 1 and len(ت) < حد_أقصى:
    # apl-source:28
    ت = ت + [مجموع_القواسم(ت[len(ت) - 1])]
  # apl-source:29
  return ت
# apl-source:30

# apl-source:31
ت = متتابعة_جزئية(12, 100)
# apl-source:32
print("من 12:", ت)
# apl-source:33

# apl-source:34
تأكد_يساوي(len(ت), 7, "سبعة حدود")
# apl-source:35
تأكد_يساوي(ت[1], 16, "الثاني 16")
# apl-source:36
تأكد_يساوي(ت[2], 15, "الثالث 15")
# apl-source:37
تأكد_يساوي(ت[6], 1, "تنتهي بواحد")
# apl-source:38

# apl-source:39
# الأعداد الكاملة تستقر فوراً: 28 -> 28
# apl-source:40
تك = متتابعة_جزئية(28, 5)
# apl-source:41
تأكد_يساوي(تك[1], 28, "28 كامل: يعود لنفسه")
# apl-source:42

# apl-source:43
# الأولية تنتهي بخطوتين: 13 -> 1
# apl-source:44
تأكد_يساوي(len(متتابعة_جزئية(13, 10)), 2, "الأولي ينتهي فوراً")
# apl-source:45
