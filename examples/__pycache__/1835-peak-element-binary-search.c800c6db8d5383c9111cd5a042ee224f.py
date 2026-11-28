
# apl-source:1
# مثال 1835 — موضع قمة في المصفوفة
# apl-source:2
# Find a peak element
# apl-source:3
# Demonstrates: بحث
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1835-peak-element-binary-search.apl
# apl-source:6

# apl-source:7
# إن كان الجار أكبر فالقمة يمينه
# apl-source:8
# وإلا فهي هنا أو يساره
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
def قمة(ق):
  # apl-source:19
  يسار = 0
  # apl-source:20
  يمين = len(ق) - 1
  # apl-source:21
  while يسار < يمين:
    # apl-source:22
    وسط = (يسار + يمين) // 2
    # apl-source:23
    if ق[وسط] < ق[وسط + 1]:
      # apl-source:24
      يسار = وسط + 1
    # apl-source:25
    else:
      # apl-source:26
      يمين = وسط
  # apl-source:27
  return يسار
# apl-source:28

# apl-source:29
تأكد_يساوي(قمة([1, 2, 3, 1]), 2, "قمة وسط")
# apl-source:30
تأكد_يساوي(قمة([1, 2, 3]), 2, "صاعدة")
# apl-source:31
تأكد_يساوي(قمة([3, 2, 1]), 0, "هابطة")
# apl-source:32
