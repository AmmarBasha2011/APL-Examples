
# apl-source:1
# مثال 2250 — عدد المقاطع بمجموع ستة
# apl-source:2
# Subarrays with sum six
# apl-source:3
# Demonstrates: قوائم
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2250-list-count-subarrays-sum-equals-six.apl
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
  ع = 0
  # apl-source:20
  for ي in range(len(ق)):
    # apl-source:21
    م = 0
    # apl-source:22
    for ك in range(ي, len(ق)):
      # apl-source:23
      م = م + ق[ك]
      # apl-source:24
      if م == 6:
        # apl-source:25
        ع = ع + 1
  # apl-source:26
  return ع
# apl-source:27

# apl-source:28
تأكد_يساوي(ف([1, 2, 3]), 1, "حالة 1")
# apl-source:29
تأكد_يساوي(ف([6]), 1, "حالة 2")
# apl-source:30
تأكد_يساوي(ف([3, 3, 3]), 2, "حالة 3")
# apl-source:31
تأكد_يساوي(ف([1, 5, 0, 6]), 4, "حالة 4")
# apl-source:32
