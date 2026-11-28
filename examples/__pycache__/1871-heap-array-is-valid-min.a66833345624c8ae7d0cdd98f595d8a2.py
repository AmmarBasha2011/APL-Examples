
# apl-source:1
# مثال 1871 — هل المصفوفة كومة صغرى
# apl-source:2
# Check array is a min heap
# apl-source:3
# Demonstrates: هياكل بيانات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1871-heap-array-is-valid-min.apl
# apl-source:6

# apl-source:7
# الابنان عند 2ك+1 و2ك+2
# apl-source:8
# نفحص كل أب
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
def كومة_صغرى(ق):
  # apl-source:19
  for ك in range(len(ق)):
    # apl-source:20
    يسار = 2 * ك + 1
    # apl-source:21
    يمين = 2 * ك + 2
    # apl-source:22
    if يسار < len(ق) and ق[ك] > ق[يسار]:
      # apl-source:23
      return False
    # apl-source:24
    if يمين < len(ق) and ق[ك] > ق[يمين]:
      # apl-source:25
      return False
  # apl-source:26
  return True
# apl-source:27

# apl-source:28
تأكد_يساوي(كومة_صغرى([1, 3, 2, 4, 5]), True, "صحيحة")
# apl-source:29
تأكد_يساوي(كومة_صغرى([3, 1, 2]), False, "خاطئة")
# apl-source:30
تأكد_يساوي(كومة_صغرى([]), True, "فارغة")
# apl-source:31
