
# apl-source:1
# مثال 979 — ك أقرب الجيران
# apl-source:2
# k-nearest neighbors
# apl-source:3
# Demonstrates: تصويت الأقربين بالمسافة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/979-k-nearest.apl
# apl-source:6

# apl-source:7
# ك أقرب الجيران: تصنيف نقطة بتصويت أقرب ك جاراً إليها
# apl-source:8
# المسافة الإقليدية المربعة تكفي للمقارنة دون جذر
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
تدريب = [[1, 1], [2, 1], [1, 2], [10, 10], [11, 10], [10, 11]]
# apl-source:19
فئات = ["أ", "أ", "أ", "ب", "ب", "ب"]
# apl-source:20

# apl-source:21
def صنف(نقطة, ك):
  # apl-source:22
  مسافات = []
  # apl-source:23
  for i in range(len(تدريب)):
    # apl-source:24
    ف_س = تدريب[i][0] - نقطة[0]
    # apl-source:25
    ف_ص = تدريب[i][1] - نقطة[1]
    # apl-source:26
    مسافات = مسافات + [[(ف_س * ف_س) + (ف_ص * ف_ص), فئات[i]]]
  # apl-source:27
  مرتبة = []
  # apl-source:28
  for عنصر in مسافات:
    # apl-source:29
    وضع = len(مرتبة)
    # apl-source:30
    for ف in range(len(مرتبة)):
      # apl-source:31
      if (عنصر[0] < مرتبة[ف][0]) and (وضع == len(مرتبة)):
        # apl-source:32
        وضع = ف
    # apl-source:33
    مرتبة = مرتبة + [عنصر]
    # apl-source:34
    for ج in range(len(مرتبة) - 1, وضع, -1):
      # apl-source:35
      مرتبة[ج] = مرتبة[ج - 1]
    # apl-source:36
    مرتبة[وضع] = عنصر
  # apl-source:37
  أصوات_أ = 0
  # apl-source:38
  أصوات_ب = 0
  # apl-source:39
  for i in range(ك):
    # apl-source:40
    if مرتبة[i][1] == "أ":
      # apl-source:41
      أصوات_أ = أصوات_أ + 1
    # apl-source:42
    else:
      # apl-source:43
      أصوات_ب = أصوات_ب + 1
  # apl-source:44
  if أصوات_أ > أصوات_ب:
    # apl-source:45
    return "أ"
  # apl-source:46
  return "ب"
# apl-source:47

# apl-source:48
تأكد_يساوي(صنف([1.5, 1.5], 3), "أ", "نقطة قرب عنقود أ")
# apl-source:49
تأكد_يساوي(صنف([10, 10.5], 3), "ب", "نقطة قرب عنقود ب")
# apl-source:50
تأكد_يساوي(صنف([0, 0], 1), "أ", "أقرب جار واحد")
# apl-source:51
