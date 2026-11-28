
# apl-source:1
# مثال 867 — الصورة التكاملية
# apl-source:2
# Integral image
# apl-source:3
# Demonstrates: مجموع مقدم ثنائي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/867-integral-image.apl
# apl-source:6

# apl-source:7
# الصورة التكاملية: مجموع مقدم ثنائي الأبعاد لمجاميع المستطيلات في O(1)
# apl-source:8
# أساس مرشحات الرؤية الحاسوبية السريعة (طريقة فيولا-جونز)
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
def صورة_تكاملية(مصفوفة):
  # apl-source:19
  ن = len(مصفوفة)
  # apl-source:20
  م = len(مصفوفة[0])
  # apl-source:21
  ت = []
  # apl-source:22
  for _ in range(ن):
    # apl-source:23
    صف = []
    # apl-source:24
    for __ in range(م):
      # apl-source:25
      صف = صف + [0]
    # apl-source:26
    ت = ت + [صف]
  # apl-source:27
  for i in range(ن):
    # apl-source:28
    for ج in range(م):
      # apl-source:29
      قيمة = مصفوفة[i][ج]
      # apl-source:30
      if i > 0:
        # apl-source:31
        قيمة = قيمة + ت[i - 1][ج]
      # apl-source:32
      if ج > 0:
        # apl-source:33
        قيمة = قيمة + ت[i][ج - 1]
      # apl-source:34
      if i > 0 and ج > 0:
        # apl-source:35
        قيمة = قيمة - ت[i - 1][ج - 1]
      # apl-source:36
      ت[i][ج] = قيمة
  # apl-source:37
  return ت
# apl-source:38

# apl-source:39
# مجموع المستطيل من (ص1,ع1) إلى (ص2,ع2) شاملاً
# apl-source:40
def مجموع_مستطيل(ت, ص1, ع1, ص2, ع2):
  # apl-source:41
  ناتج = ت[ص2][ع2]
  # apl-source:42
  if ص1 > 0:
    # apl-source:43
    ناتج = ناتج - ت[ص1 - 1][ع2]
  # apl-source:44
  if ع1 > 0:
    # apl-source:45
    ناتج = ناتج - ت[ص2][ع1 - 1]
  # apl-source:46
  if ص1 > 0 and ع1 > 0:
    # apl-source:47
    ناتج = ناتج + ت[ص1 - 1][ع1 - 1]
  # apl-source:48
  return ناتج
# apl-source:49

# apl-source:50
مصفوفة = [
  # apl-source:51
  [1, 2, 3],
  # apl-source:52
  [4, 5, 6],
  # apl-source:53
  [7, 8, 9]
# apl-source:54
]
# apl-source:55
ت = صورة_تكاملية(مصفوفة)
# apl-source:56
print("الصورة التكاملية:", ت)
# apl-source:57

# apl-source:58
تأكد_يساوي(ت[0][2], 6, "صف أول تراكمي")
# apl-source:59
تأكد_يساوي(ت[1][1], 12, "ت[1][1] = 1+2+4+5")
# apl-source:60
تأكد_يساوي(ت[2][2], 45, "المجموع الكلي 45")
# apl-source:61

# apl-source:62
# مستطيل 2x2 من المركز: 5+6+8+9 = 28
# apl-source:63
تأكد_يساوي(مجموع_مستطيل(ت, 1, 1, 2, 2), 28, "مستطيل المركز")
# apl-source:64
تأكد_يساوي(مجموع_مستطيل(ت, 0, 0, 2, 2), 45, "المصفوفة كاملة")
# apl-source:65
تأكد_يساوي(مجموع_مستطيل(ت, 0, 1, 1, 2), 16, "مستطيل علوي أيمن: 2+3+5+6")
# apl-source:66
