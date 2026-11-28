
# apl-source:1
# مثال 1417 — مطابقة نص الزيادة والنقصان
# apl-source:2
# DI string match permutation
# apl-source:3
# Demonstrates: جشع
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1417-di-string-match.apl
# apl-source:6

# apl-source:7
# I تعني الأصغر التالي D تعني الأكبر التالي
# apl-source:8
# نأخذ من أصغر أو أكبر قيمة متبقية
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
def تبديل_نمط(نمط):
  # apl-source:19
  ادنى = 0
  # apl-source:20
  اعلى = len(نمط)
  # apl-source:21
  ناتج = []
  # apl-source:22
  for ح in نمط:
    # apl-source:23
    if ح == "I":
      # apl-source:24
      ناتج = ناتج + [ادنى]
      # apl-source:25
      ادنى = ادنى + 1
    # apl-source:26
    else:
      # apl-source:27
      ناتج = ناتج + [اعلى]
      # apl-source:28
      اعلى = اعلى - 1
  # apl-source:29
  ناتج = ناتج + [ادنى]
  # apl-source:30
  return ناتج
# apl-source:31

# apl-source:32
تأكد_يساوي(تبديل_نمط("IDID"), [0,4,1,3,2], "أربعة")
# apl-source:33
تأكد_يساوي(تبديل_نمط("III"), [0,1,2,3], "صاعد")
# apl-source:34
تأكد_يساوي(تبديل_نمط("DDI"), [3,2,0,1], "هابط ثم صاعد")
# apl-source:35
