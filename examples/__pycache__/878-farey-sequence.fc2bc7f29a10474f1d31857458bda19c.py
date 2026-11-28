
# apl-source:1
# مثال 878 — متتابعة فاري
# apl-source:2
# Farey sequence
# apl-source:3
# Demonstrates: كسور مختزلة مرتبة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/878-farey-sequence.apl
# apl-source:6

# apl-source:7
# متتابعة فاري: كل الكسور المختزلة بين 0 و1 بمقامات لا تتجاوز n
# apl-source:8
# خاصية الجارين: ب*ج - أ*د = 1 دائماً
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
def قاسم_مشترك(أ, ب):
  # apl-source:19
  while ب != 0:
    # apl-source:20
    مؤقت = أ % ب
    # apl-source:21
    أ = ب
    # apl-source:22
    ب = مؤقت
  # apl-source:23
  return أ
# apl-source:24

# apl-source:25
def فاري(رتبة):
  # apl-source:26
  كسور = []
  # apl-source:27
  for مقام in range(1, رتبة + 1):
    # apl-source:28
    for بسط in range(0, مقام + 1):
      # apl-source:29
      if قاسم_مشترك(بسط, مقام) == 1:
        # apl-source:30
        كسور = كسور + [[بسط, مقام]]
  # apl-source:31
  # فرز بالقيمة: ب1*م2 مقابل ب2*م1
  # apl-source:32
  ن = len(كسور)
  # apl-source:33
  for i in range(ن):
    # apl-source:34
    for ج in range(ن - 1):
      # apl-source:35
      if كسور[ج][0] * كسور[ج + 1][1] > كسور[ج + 1][0] * كسور[ج][1]:
        # apl-source:36
        مؤقت = كسور[ج]
        # apl-source:37
        كسور[ج] = كسور[ج + 1]
        # apl-source:38
        كسور[ج + 1] = مؤقت
  # apl-source:39
  return كسور
# apl-source:40

# apl-source:41
ف5 = فاري(5)
# apl-source:42
print("فاري(5):", ف5)
# apl-source:43

# apl-source:44
تأكد_يساوي(len(ف5), 11, "أحد عشر كسراً")
# apl-source:45
تأكد_يساوي(ف5[0][1], 1, "تبدأ 0/1")
# apl-source:46
تأكد_يساوي(ف5[10][0], 1, "تنتهي 1/1")
# apl-source:47
تأكد_يساوي(ف5[5][0], 1, "الوسط 1/2 بسطاً")
# apl-source:48
تأكد_يساوي(ف5[5][1], 2, "الوسط 1/2 مقاماً")
# apl-source:49

# apl-source:50
# خاصية الجارين لكل زوج متتال
# apl-source:51
for i in range(len(ف5) - 1):
  # apl-source:52
  ب1 = ف5[i][0]
  # apl-source:53
  م1 = ف5[i][1]
  # apl-source:54
  ب2 = ف5[i + 1][0]
  # apl-source:55
  م2 = ف5[i + 1][1]
  # apl-source:56
  تأكد_يساوي(ب2 * م1 - ب1 * م2, 1, "خاصية الجارين عند " + str(i))
# apl-source:57
