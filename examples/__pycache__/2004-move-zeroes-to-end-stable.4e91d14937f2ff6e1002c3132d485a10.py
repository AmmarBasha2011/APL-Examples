
# apl-source:1
# مثال 2004 — نقل الأصفار إلى النهاية
# apl-source:2
# Move zeroes to end
# apl-source:3
# Demonstrates: قوائم
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2004-move-zeroes-to-end-stable.apl
# apl-source:6

# apl-source:7
# # نجمع غير الأصفار أولا
# apl-source:8
# # ثم نلحق الأصفار
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
def انقل(ق):
  # apl-source:19
  غير = []
  # apl-source:20
  اصفار = 0
  # apl-source:21
  for ع in ق:
    # apl-source:22
    if ع == 0:
      # apl-source:23
      اصفار = اصفار + 1
    # apl-source:24
    else:
      # apl-source:25
      غير = غير + [ع]
  # apl-source:26
  return غير + [0] * اصفار
# apl-source:27

# apl-source:28
تأكد_يساوي(انقل([0, 1, 0, 3, 12]), [1, 3, 12, 0, 0], "كلاسيكي")
# apl-source:29
تأكد_يساوي(انقل([0, 0]), [0, 0], "أصفار")
# apl-source:30
تأكد_يساوي(انقل([1, 2]), [1, 2], "بلا أصفار")
# apl-source:31
