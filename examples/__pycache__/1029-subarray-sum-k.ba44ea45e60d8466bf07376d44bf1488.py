
# apl-source:1
# مثال 1029 — مجموع مصفوفة جزئية
# apl-source:2
# Subarray sum equals k
# apl-source:3
# Demonstrates: مجاميع تراكمية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1029-subarray-sum-k.apl
# apl-source:6

# apl-source:7
# المجموع التراكمي عند ن ناقص عند م يساوي مجموع الجزء
# apl-source:8
# نعد كم مرة ظهر المجموع المطلوب سابقاً
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
def عدد_اجزاء(ق, ك):
  # apl-source:19
  مجاميع = [0]
  # apl-source:20
  عدد_ = 0
  # apl-source:21
  تراكم = 0
  # apl-source:22
  for س in ق:
    # apl-source:23
    تراكم = تراكم + س
    # apl-source:24
    for م in مجاميع:
      # apl-source:25
      if (تراكم - م) == ك:
        # apl-source:26
        عدد_ = عدد_ + 1
    # apl-source:27
    مجاميع = مجاميع + [تراكم]
  # apl-source:28
  return عدد_
# apl-source:29

# apl-source:30
تأكد_يساوي(عدد_اجزاء([1, 1, 1], 2), 2, "ثلاثة آحاد")
# apl-source:31
تأكد_يساوي(عدد_اجزاء([1, 2, 3], 3), 2, "اثنان")
# apl-source:32
تأكد_يساوي(عدد_اجزاء([1, -1, 0], 0), 3, "أصفار وسالب")
# apl-source:33
