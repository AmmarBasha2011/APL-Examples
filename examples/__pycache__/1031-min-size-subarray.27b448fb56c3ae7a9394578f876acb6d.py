
# apl-source:1
# مثال 1031 — أقصر جزء بمجموع كاف
# apl-source:2
# Minimum size subarray sum
# apl-source:3
# Demonstrates: نافذة متغيرة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1031-min-size-subarray.apl
# apl-source:6

# apl-source:7
# نوسع النافذة حتى يبلغ المجموع الهدف
# apl-source:8
# ثم نضيقها من اليسار ونسجل أقصر طول
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
def اقصر_جزء(هدف, ق):
  # apl-source:19
  ي = 0
  # apl-source:20
  مجموع_ن = 0
  # apl-source:21
  افضل = 0
  # apl-source:22
  for ع in range(len(ق)):
    # apl-source:23
    مجموع_ن = مجموع_ن + ق[ع]
    # apl-source:24
    while مجموع_ن >= هدف:
      # apl-source:25
      ط = (ع - ي) + 1
      # apl-source:26
      if (افضل == 0) or (ط < افضل):
        # apl-source:27
        افضل = ط
      # apl-source:28
      مجموع_ن = مجموع_ن - ق[ي]
      # apl-source:29
      ي = ي + 1
  # apl-source:30
  return افضل
# apl-source:31

# apl-source:32
تأكد_يساوي(اقصر_جزء(7, [2, 3, 1, 2, 4, 3]), 2, "4 و3")
# apl-source:33
تأكد_يساوي(اقصر_جزء(4, [1, 4, 4]), 1, "عنصر واحد")
# apl-source:34
تأكد_يساوي(اقصر_جزء(11, [1, 1, 1, 1]), 0, "غير ممكن")
# apl-source:35
