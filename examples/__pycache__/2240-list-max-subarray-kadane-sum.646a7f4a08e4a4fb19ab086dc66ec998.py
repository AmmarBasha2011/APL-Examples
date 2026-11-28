
# apl-source:1
# مثال 2240 — أكبر مجموع جزئي
# apl-source:2
# Kadane max subarray
# apl-source:3
# Demonstrates: قوائم
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2240-list-max-subarray-kadane-sum.apl
# apl-source:6

# apl-source:7
# # نمرر القائمة
# apl-source:8
# # ونتحقق من الناتج
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
def ف(ق):
  # apl-source:19
  ح = ق[0]
  # apl-source:20
  ك = ق[0]
  # apl-source:21
  for ع in ق[1:]:
    # apl-source:22
    ح = max(ع, ح + ع)
    # apl-source:23
    if ح > ك:
      # apl-source:24
      ك = ح
  # apl-source:25
  return ك
# apl-source:26

# apl-source:27
تأكد_يساوي(ف([3, 1, 2]), 6, "حالة 1")
# apl-source:28
تأكد_يساوي(ف([5]), 5, "حالة 2")
# apl-source:29
تأكد_يساوي(ف([1, 2, 3, 4, 5, 6]), 21, "حالة 3")
# apl-source:30
تأكد_يساوي(ف([-2, 0, 7, 7, 4]), 18, "حالة 4")
# apl-source:31
تأكد_يساوي(ف([10, 20, 10, 30, 20, 10]), 100, "حالة 5")
# apl-source:32
تأكد_يساوي(ف([-3, -1, -2]), -1, "حالة 6")
# apl-source:33
تأكد_يساوي(ف([2, -1, 2, 3, -9, 4]), 6, "حالة 7")
# apl-source:34
