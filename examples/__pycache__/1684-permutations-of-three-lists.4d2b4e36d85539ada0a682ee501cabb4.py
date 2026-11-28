
# apl-source:1
# مثال 1684 — تباديل ثلاثة عناصر
# apl-source:2
# All permutations of a short list
# apl-source:3
# Demonstrates: توافيق
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1684-permutations-of-three-lists.apl
# apl-source:6

# apl-source:7
# نختار عنصراً غير مستخدم
# apl-source:8
# نكرر على الباقي
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
def تباديل(ق):
  # apl-source:19
  if len(ق) <= 1:
    # apl-source:20
    return [ق]
  # apl-source:21
  ناتج = []
  # apl-source:22
  for ك in range(len(ق)):
    # apl-source:23
    باقي = []
    # apl-source:24
    for ي in range(len(ق)):
      # apl-source:25
      if ي != ك:
        # apl-source:26
        باقي.append(ق[ي])
    # apl-source:27
    for ت in تباديل(باقي):
      # apl-source:28
      ناتج.append([ق[ك]] + ت)
  # apl-source:29
  return ناتج
# apl-source:30

# apl-source:31
تأكد_يساوي(len(تباديل([1, 2, 3])), 6, "ستة")
# apl-source:32
تأكد_يساوي(تباديل([1, 2, 3])[0], [1, 2, 3], "الأول")
# apl-source:33
تأكد_يساوي(تباديل([1, 2, 3])[5], [3, 2, 1], "الأخير")
# apl-source:34
تأكد_يساوي(len(تباديل([1, 2, 3, 4])), 24, "أربعة")
# apl-source:35
