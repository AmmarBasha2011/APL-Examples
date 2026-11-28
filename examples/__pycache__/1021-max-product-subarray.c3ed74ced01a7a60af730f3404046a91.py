
# apl-source:1
# مثال 1021 — أكبر حاصل ضرب لمصفوفة جزئية
# apl-source:2
# Maximum product subarray
# apl-source:3
# Demonstrates: حفظ الأكبر والأصغر
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1021-max-product-subarray.apl
# apl-source:6

# apl-source:7
# السالب قد يقلب أصغر ناتج إلى أكبر
# apl-source:8
# فنحفظ عند كل خطوة أكبر وأصغر ضرب ينتهي هنا
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
def اكبر_ضرب(ق):
  # apl-source:19
  اكبر = ق[0]
  # apl-source:20
  اصغر = ق[0]
  # apl-source:21
  افضل = ق[0]
  # apl-source:22
  for ع in range(1, len(ق)):
    # apl-source:23
    س = ق[ع]
    # apl-source:24
    أ = اكبر * س
    # apl-source:25
    ب = اصغر * س
    # apl-source:26
    اكبر = س
    # apl-source:27
    if أ > اكبر:
      # apl-source:28
      اكبر = أ
    # apl-source:29
    if ب > اكبر:
      # apl-source:30
      اكبر = ب
    # apl-source:31
    اصغر = س
    # apl-source:32
    if أ < اصغر:
      # apl-source:33
      اصغر = أ
    # apl-source:34
    if ب < اصغر:
      # apl-source:35
      اصغر = ب
    # apl-source:36
    if اكبر > افضل:
      # apl-source:37
      افضل = اكبر
  # apl-source:38
  return افضل
# apl-source:39

# apl-source:40
تأكد_يساوي(اكبر_ضرب([2, 3, -2, 4]), 6, "سالب في الوسط")
# apl-source:41
تأكد_يساوي(اكبر_ضرب([-2, 0, -1]), 0, "صفر يفصل")
# apl-source:42
تأكد_يساوي(اكبر_ضرب([-2, 3, -4]), 24, "سالبان")
# apl-source:43
تأكد_يساوي(اكبر_ضرب([-3]), -3, "عنصر سالب")
# apl-source:44
