
# apl-source:1
# مثال 1335 — مجموع أصغر المصفوفات الجزئية
# apl-source:2
# Sum of subarray minimums
# apl-source:3
# Demonstrates: مكدس أحادي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1335-sum-subarray-minimums.apl
# apl-source:6

# apl-source:7
# نحسب لكل عنصر عدد المصفوفات التي هو أصغرها
# apl-source:8
# نستخدم مكدساً متزايداً
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
def مجموع_اصغر(أرقام):
  # apl-source:19
  ن = len(أرقام)
  # apl-source:20
  يسار = [0] * ن
  # apl-source:21
  يمين = [0] * ن
  # apl-source:22
  مكدس = []
  # apl-source:23
  for ع in range(ن):
    # apl-source:24
    while (len(مكدس) > 0) and (أرقام[مكدس[len(مكدس) - 1]] > أرقام[ع]):
      # apl-source:25
      مكدس.pop()
    # apl-source:26
    if len(مكدس) == 0:
      # apl-source:27
      يسار[ع] = ع + 1
    # apl-source:28
    else:
      # apl-source:29
      يسار[ع] = ع - مكدس[len(مكدس) - 1]
    # apl-source:30
    مكدس = مكدس + [ع]
  # apl-source:31
  مكدس = []
  # apl-source:32
  for ع in range(ن - 1, -1, -1):
    # apl-source:33
    while (len(مكدس) > 0) and (أرقام[مكدس[len(مكدس) - 1]] >= أرقام[ع]):
      # apl-source:34
      مكدس.pop()
    # apl-source:35
    if len(مكدس) == 0:
      # apl-source:36
      يمين[ع] = ن - ع
    # apl-source:37
    else:
      # apl-source:38
      يمين[ع] = مكدس[len(مكدس) - 1] - ع
    # apl-source:39
    مكدس = مكدس + [ع]
  # apl-source:40
  مجموع = 0
  # apl-source:41
  for ع in range(ن):
    # apl-source:42
    مجموع = مجموع + أرقام[ع] * يسار[ع] * يمين[ع]
  # apl-source:43
  return مجموع
# apl-source:44

# apl-source:45
تأكد_يساوي(مجموع_اصغر([3,1,2,4]), 17, "أربعة")
# apl-source:46
تأكد_يساوي(مجموع_اصغر([11,81,94,43,3]), 444, "خمسة")
# apl-source:47
تأكد_يساوي(مجموع_اصغر([5]), 5, "عنصر")
# apl-source:48
