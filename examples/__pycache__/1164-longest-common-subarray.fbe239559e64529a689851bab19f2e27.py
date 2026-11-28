
# apl-source:1
# مثال 1164 — أطول مقطع مشترك
# apl-source:2
# Longest common subarray
# apl-source:3
# Demonstrates: برمجة ديناميكية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1164-longest-common-subarray.apl
# apl-source:6

# apl-source:7
# الخلية تساوي سابقتها القطرية زائد واحد عند التطابق
# apl-source:8
# وإلا صفر ونحتفظ بالأكبر
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
def اطول_مشترك(أ, ب):
  # apl-source:19
  سابق = [0] * (len(ب) + 1)
  # apl-source:20
  اقصى = 0
  # apl-source:21
  for ع in range(len(أ)):
    # apl-source:22
    حالي = [0] * (len(ب) + 1)
    # apl-source:23
    for ج in range(len(ب)):
      # apl-source:24
      if أ[ع] == ب[ج]:
        # apl-source:25
        حالي[ج + 1] = سابق[ج] + 1
        # apl-source:26
        if حالي[ج + 1] > اقصى:
          # apl-source:27
          اقصى = حالي[ج + 1]
    # apl-source:28
    سابق = حالي
  # apl-source:29
  return اقصى
# apl-source:30

# apl-source:31
تأكد_يساوي(اطول_مشترك([1,2,3,2,1], [3,2,1,4,7]), 3, "مثال أول")
# apl-source:32
تأكد_يساوي(اطول_مشترك([0,0,0,0,0], [0,0,0,0,0]), 5, "أصفار")
# apl-source:33
تأكد_يساوي(اطول_مشترك([1,2], [3,4]), 0, "لا مشترك")
# apl-source:34
تأكد_يساوي(اطول_مشترك([], [1]), 0, "فارغة")
# apl-source:35
