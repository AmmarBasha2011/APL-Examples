
# apl-source:1
# مثال 837 — تحليل LU
# apl-source:2
# LU decomposition
# apl-source:3
# Demonstrates: مثلثتان سفلية وعلوية، دوليتل
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/837-lu-decomposition.apl
# apl-source:6

# apl-source:7
# تحليل LU: تحليل المصفوفة إلى مثلثة سفلية وعلوية
# apl-source:8
# A = L @ U بدون تبديل صفوف (طريقة دوليتل)
# apl-source:9
# تستخدم في حل أنظمة المعادلات وحساب المحدد
# apl-source:10

# apl-source:11
def تأكد_يساوي(فعلي, متوقع, اسم):
  # apl-source:12
  if فعلي != متوقع:
    # apl-source:13
    print("فشل:", اسم)
    # apl-source:14
    print("  متوقع:", متوقع)
    # apl-source:15
    print("  فعلي:", فعلي)
    # apl-source:16
    قياسي_نظام_اخرج(1)
  # apl-source:17
  print("ناجح:", اسم)
# apl-source:18

# apl-source:19
def تحليل_LU(مصفوفة):
  # apl-source:20
  ن = len(مصفوفة)
  # apl-source:21
  ل = []
  # apl-source:22
  ع = []
  # apl-source:23
  for _ in range(ن):
    # apl-source:24
    صف_ل = []
    # apl-source:25
    صف_ع = []
    # apl-source:26
    for __ in range(ن):
      # apl-source:27
      صف_ل = صف_ل + [0.0]
      # apl-source:28
      صف_ع = صف_ع + [0.0]
    # apl-source:29
    ل = ل + [صف_ل]
    # apl-source:30
    ع = ع + [صف_ع]
  # apl-source:31
  for ك in range(ن):
    # apl-source:32
    ل[ك][ك] = 1.0
    # apl-source:33
    for ج in range(ن):
      # apl-source:34
      if ج >= ك:
        # apl-source:35
        مجموع = 0.0
        # apl-source:36
        for م in range(ك):
          # apl-source:37
          مجموع = مجموع + ل[ك][م] * ع[م][ج]
        # apl-source:38
        ع[ك][ج] = مصفوفة[ك][ج] - مجموع
    # apl-source:39
    for i in range(ن):
      # apl-source:40
      if i > ك:
        # apl-source:41
        مجموع2 = 0.0
        # apl-source:42
        for م in range(ك):
          # apl-source:43
          مجموع2 = مجموع2 + ل[i][م] * ع[م][ك]
        # apl-source:44
        ل[i][ك] = (مصفوفة[i][ك] - مجموع2) / ع[ك][ك]
  # apl-source:45
  return ل, ع
# apl-source:46

# apl-source:47
أ = [
  # apl-source:48
  [4.0, 3.0],
  # apl-source:49
  [6.0, 3.0]
# apl-source:50
]
# apl-source:51
ل, ع = تحليل_LU(أ)
# apl-source:52

# apl-source:53
print("L =", ل)
# apl-source:54
print("U =", ع)
# apl-source:55

# apl-source:56
تأكد_يساوي(ل[0][0], 1.0, "ل[0][0] قطرية")
# apl-source:57
تأكد_يساوي(ل[1][0], 1.5, "ل[1][0] معامل")
# apl-source:58
تأكد_يساوي(ع[0][0], 4.0, "ع[0][0]")
# apl-source:59
تأكد_يساوي(ع[0][1], 3.0, "ع[0][1]")
# apl-source:60
تأكد_يساوي(ع[1][1], -1.5, "ع[1][1]")
# apl-source:61

# apl-source:62
# تحقق: L @ U = A
# apl-source:63
جداء00 = ل[0][0]*ع[0][0] + ل[0][1]*ع[1][0]
# apl-source:64
جداء11 = ل[1][0]*ع[0][1] + ل[1][1]*ع[1][1]
# apl-source:65
تأكد_يساوي(جداء00, 4.0, "الجداء يعيد أ[0][0]")
# apl-source:66
تأكد_يساوي(جداء11, 3.0, "الجداء يعيد أ[1][1]")
# apl-source:67
