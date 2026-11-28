
# apl-source:1
# مثال 1772 — أكبر مستطيل في مدرج
# apl-source:2
# Largest rectangle in histogram
# apl-source:3
# Demonstrates: مكدسات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1772-largest-rectangle-histogram.apl
# apl-source:6

# apl-source:7
# نحسب المساحة عند كل انخفاض
# apl-source:8
# نضيف عموداً وهمياً صفرياً
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
def أكبر_مستطيل(ع):
  # apl-source:19
  ع = ع + [0]
  # apl-source:20
  مكدس = []
  # apl-source:21
  أفضل = 0
  # apl-source:22
  for ك in range(len(ع)):
    # apl-source:23
    while len(مكدس) > 0 and ع[مكدس[len(مكدس) - 1]] >= ع[ك]:
      # apl-source:24
      ارتفاع = ع[مكدس.pop()]
      # apl-source:25
      عرض = ك
      # apl-source:26
      if len(مكدس) > 0:
        # apl-source:27
        عرض = ك - مكدس[len(مكدس) - 1] - 1
      # apl-source:28
      أفضل = max(أفضل, ارتفاع * عرض)
    # apl-source:29
    مكدس.append(ك)
  # apl-source:30
  return أفضل
# apl-source:31

# apl-source:32
تأكد_يساوي(أكبر_مستطيل([2, 1, 5, 6, 2, 3]), 10, "كلاسيكي")
# apl-source:33
تأكد_يساوي(أكبر_مستطيل([2, 4]), 4, "اثنان")
# apl-source:34
تأكد_يساوي(أكبر_مستطيل([3, 3, 3]), 9, "متساوية")
# apl-source:35
