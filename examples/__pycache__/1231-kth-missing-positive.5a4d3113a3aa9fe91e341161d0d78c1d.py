
# apl-source:1
# مثال 1231 — الرقم المفقود k
# apl-source:2
# Kth missing positive number
# apl-source:3
# Demonstrates: بحث ثنائي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1231-kth-missing-positive.apl
# apl-source:6

# apl-source:7
# عدد المفقودات قبل العنصر i هو a[i] ناقص i ناقص واحد
# apl-source:8
# نبحث ثنائياً عن أول موضع يتجاوز k
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
def مفقود_ك(أ, ك):
  # apl-source:19
  يسار = 0
  # apl-source:20
  يمين = len(أ)
  # apl-source:21
  while يسار < يمين:
    # apl-source:22
    وسط = (يسار + يمين) // 2
    # apl-source:23
    if أ[وسط] - وسط - 1 < ك:
      # apl-source:24
      يسار = وسط + 1
    # apl-source:25
    else:
      # apl-source:26
      يمين = وسط
  # apl-source:27
  return يسار + ك
# apl-source:28

# apl-source:29
تأكد_يساوي(مفقود_ك([2,3,4,7,11], 5), 9, "مثال أول")
# apl-source:30
تأكد_يساوي(مفقود_ك([1,2,3,4], 2), 6, "بعد النهاية")
# apl-source:31
تأكد_يساوي(مفقود_ك([5,6], 1), 1, "قبل البداية")
# apl-source:32
