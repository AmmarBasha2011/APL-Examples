
# apl-source:1
# مثال 1742 — كمية الماء المحبوس
# apl-source:2
# Trapping rain water
# apl-source:3
# Demonstrates: مؤشران
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1742-trapping-rain-water-total.apl
# apl-source:6

# apl-source:7
# أعلى جدار يساراً ويميناً
# apl-source:8
# الماء الأقل منهما ناقص العمود
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
def ماء_محبوس(ع):
  # apl-source:19
  ن = len(ع)
  # apl-source:20
  if ن == 0:
    # apl-source:21
    return 0
  # apl-source:22
  يسار = []
  # apl-source:23
  يمين = []
  # apl-source:24
  for ك in range(ن):
    # apl-source:25
    يسار.append(0)
    # apl-source:26
    يمين.append(0)
  # apl-source:27
  يسار[0] = ع[0]
  # apl-source:28
  for ك in range(1, ن):
    # apl-source:29
    يسار[ك] = max(يسار[ك - 1], ع[ك])
  # apl-source:30
  يمين[ن - 1] = ع[ن - 1]
  # apl-source:31
  for ك in range(ن - 2, -1, -1):
    # apl-source:32
    يمين[ك] = max(يمين[ك + 1], ع[ك])
  # apl-source:33
  مجموع = 0
  # apl-source:34
  for ك in range(ن):
    # apl-source:35
    مجموع = مجموع + min(يسار[ك], يمين[ك]) - ع[ك]
  # apl-source:36
  return مجموع
# apl-source:37

# apl-source:38
تأكد_يساوي(ماء_محبوس([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]), 6, "كلاسيكي")
# apl-source:39
تأكد_يساوي(ماء_محبوس([3, 0, 3]), 3, "حفرة")
# apl-source:40
تأكد_يساوي(ماء_محبوس([1, 2, 3]), 0, "صاعدة")
# apl-source:41
