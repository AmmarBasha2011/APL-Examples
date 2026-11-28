
# apl-source:1
# مثال 1957 — مجموع مسافات هامنج بين كل الأزواج
# apl-source:2
# Sum of Hamming distances
# apl-source:3
# Demonstrates: بتات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1957-hamming-distance-sum-all-pairs.apl
# apl-source:6

# apl-source:7
# # لكل موضع بت نضرب عدد الآحاد في عدد الأصفار
# apl-source:8
# # وهذا أسرع من مقارنة كل زوج
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
def مجموع(قائمة):
  # apl-source:19
  مج = 0
  # apl-source:20
  for ب in range(32):
    # apl-source:21
    آحاد = 0
    # apl-source:22
    for ع in قائمة:
      # apl-source:23
      if (ع >> ب) & 1:
        # apl-source:24
        آحاد = آحاد + 1
    # apl-source:25
    مج = مج + آحاد * (len(قائمة) - آحاد)
  # apl-source:26
  return مج
# apl-source:27

# apl-source:28
تأكد_يساوي(مجموع([4, 14, 2]), 6, "كلاسيكي")
# apl-source:29
تأكد_يساوي(مجموع([1, 1]), 0, "متساويان")
# apl-source:30
تأكد_يساوي(مجموع([0, 7]), 3, "ثلاثة بتات")
# apl-source:31
