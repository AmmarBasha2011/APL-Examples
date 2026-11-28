
# apl-source:1
# مثال 1833 — أول وآخر موضع للعنصر
# apl-source:2
# First and last position in sorted array
# apl-source:3
# Demonstrates: بحث
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1833-first-last-position-sorted.apl
# apl-source:6

# apl-source:7
# نبحث عن أول ظهور
# apl-source:8
# ثم عن آخر ظهور
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
def حد(ق, هدف, أول):
  # apl-source:19
  يسار = 0
  # apl-source:20
  يمين = len(ق) - 1
  # apl-source:21
  نتيجة = -1
  # apl-source:22
  while يسار <= يمين:
    # apl-source:23
    وسط = (يسار + يمين) // 2
    # apl-source:24
    if ق[وسط] == هدف:
      # apl-source:25
      نتيجة = وسط
      # apl-source:26
      if أول:
        # apl-source:27
        يمين = وسط - 1
      # apl-source:28
      else:
        # apl-source:29
        يسار = وسط + 1
    # apl-source:30
    elif ق[وسط] < هدف:
      # apl-source:31
      يسار = وسط + 1
    # apl-source:32
    else:
      # apl-source:33
      يمين = وسط - 1
  # apl-source:34
  return نتيجة
# apl-source:35

# apl-source:36
def مدى(ق, هدف):
  # apl-source:37
  return [حد(ق, هدف, True), حد(ق, هدف, False)]
# apl-source:38

# apl-source:39
تأكد_يساوي(مدى([5, 7, 7, 8, 8, 10], 8), [3, 4], "مكرر")
# apl-source:40
تأكد_يساوي(مدى([5, 7, 7, 8, 8, 10], 6), [-1, -1], "غائب")
# apl-source:41
تأكد_يساوي(مدى([2], 2), [0, 0], "واحد")
# apl-source:42
