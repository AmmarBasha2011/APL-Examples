
# apl-source:1
# مثال 1073 — التبديل التالي
# apl-source:2
# Next permutation
# apl-source:3
# Demonstrates: أول هبوط من اليمين
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1073-next-permutation.apl
# apl-source:6

# apl-source:7
# نجد أول موضع من اليمين يقل عن التالي له
# apl-source:8
# نبدله بأصغر أكبر منه على يمينه ثم نعكس الذيل
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
def تالي(ق):
  # apl-source:19
  ع = len(ق) - 2
  # apl-source:20
  while (ع >= 0) and (ق[ع] >= ق[ع + 1]):
    # apl-source:21
    ع = ع - 1
  # apl-source:22
  if ع >= 0:
    # apl-source:23
    ك = len(ق) - 1
    # apl-source:24
    while ق[ك] <= ق[ع]:
      # apl-source:25
      ك = ك - 1
    # apl-source:26
    مؤقت = ق[ع]
    # apl-source:27
    ق[ع] = ق[ك]
    # apl-source:28
    ق[ك] = مؤقت
  # apl-source:29
  ي = ع + 1
  # apl-source:30
  ل = len(ق) - 1
  # apl-source:31
  while ي < ل:
    # apl-source:32
    مؤقت = ق[ي]
    # apl-source:33
    ق[ي] = ق[ل]
    # apl-source:34
    ق[ل] = مؤقت
    # apl-source:35
    ي = ي + 1
    # apl-source:36
    ل = ل - 1
  # apl-source:37
  return ق
# apl-source:38

# apl-source:39
تأكد_يساوي(تالي([1, 2, 3]), [1, 3, 2], "ثلاثة")
# apl-source:40
تأكد_يساوي(تالي([3, 2, 1]), [1, 2, 3], "الأخير يلتف")
# apl-source:41
تأكد_يساوي(تالي([1, 1, 5]), [1, 5, 1], "مكرر")
# apl-source:42
تأكد_يساوي(تالي([1, 3, 2]), [2, 1, 3], "بدل أول")
# apl-source:43
