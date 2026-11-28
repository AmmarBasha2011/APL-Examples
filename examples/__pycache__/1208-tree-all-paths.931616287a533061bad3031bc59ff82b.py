
# apl-source:1
# مثال 1208 — كل المسارات
# apl-source:2
# All root to leaf paths
# apl-source:3
# Demonstrates: تكرار ذاتي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1208-tree-all-paths.apl
# apl-source:6

# apl-source:7
# نحمل المسار الحالي أثناء النزول
# apl-source:8
# وعند الورقة نسجل نسخة منه
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
def مسارات(ش, حالي):
  # apl-source:19
  if len(ش) == 0:
    # apl-source:20
    return []
  # apl-source:21
  جديد = حالي + [ش[0]]
  # apl-source:22
  if (len(ش[1]) == 0) and (len(ش[2]) == 0):
    # apl-source:23
    return [جديد]
  # apl-source:24
  return مسارات(ش[1], جديد) + مسارات(ش[2], جديد)
# apl-source:25

# apl-source:26
شجرة = [1, [2, [], [5, [], []]], [3, [], []]]
# apl-source:27
تأكد_يساوي(مسارات(شجرة, []), [[1, 2, 5], [1, 3]], "مسارا الشجرة")
# apl-source:28
تأكد_يساوي(مسارات([7, [], []], []), [[7]], "عقدة")
# apl-source:29
تأكد_يساوي(مسارات([], []), [], "فارغة")
# apl-source:30
