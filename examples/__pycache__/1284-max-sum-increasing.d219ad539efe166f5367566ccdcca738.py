
# apl-source:1
# مثال 1284 — أكبر مجموع متزايد
# apl-source:2
# Maximum sum increasing subsequence
# apl-source:3
# Demonstrates: برمجة ديناميكية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1284-max-sum-increasing.apl
# apl-source:6

# apl-source:7
# أفضل مجموع ينتهي بكل عنصر
# apl-source:8
# نبنيه من الأصغر قبله
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
def اكبر_مجموع(أ):
  # apl-source:19
  if len(أ) == 0:
    # apl-source:20
    return 0
  # apl-source:21
  د = list(أ)
  # apl-source:22
  for ع in range(len(أ)):
    # apl-source:23
    for ج in range(ع):
      # apl-source:24
      if (أ[ج] < أ[ع]) and (د[ج] + أ[ع] > د[ع]):
        # apl-source:25
        د[ع] = د[ج] + أ[ع]
  # apl-source:26
  اقصى = د[0]
  # apl-source:27
  for ق in د:
    # apl-source:28
    if ق > اقصى:
      # apl-source:29
      اقصى = ق
  # apl-source:30
  return اقصى
# apl-source:31

# apl-source:32
تأكد_يساوي(اكبر_مجموع([1,101,2,3,100,4,5]), 106, "مثال أول")
# apl-source:33
تأكد_يساوي(اكبر_مجموع([3,4,5,10]), 22, "تصاعدي")
# apl-source:34
تأكد_يساوي(اكبر_مجموع([10,5,4,3]), 10, "تنازلي")
# apl-source:35
