
# apl-source:1
# مثال 2249 — فهرسا مجموع تسعة
# apl-source:2
# Two sum target nine
# apl-source:3
# Demonstrates: قوائم
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2249-list-two-sum-indices-target-nine.apl
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
  for ي in range(len(ق)):
    # apl-source:20
    for ك in range(ي + 1, len(ق)):
      # apl-source:21
      if ق[ي] + ق[ك] == 9:
        # apl-source:22
        return [ي, ك]
  # apl-source:23
  return []
# apl-source:24

# apl-source:25
تأكد_يساوي(ف([2, 7, 11, 15]), [0, 1], "حالة 1")
# apl-source:26
تأكد_يساوي(ف([1, 2, 3]), [], "حالة 2")
# apl-source:27
تأكد_يساوي(ف([4, 5]), [0, 1], "حالة 3")
# apl-source:28
تأكد_يساوي(ف([3, 6, 1, 8]), [0, 1], "حالة 4")
# apl-source:29
