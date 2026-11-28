
# apl-source:1
# مثال 1421 — مقاطع ثنائية متساوية
# apl-source:2
# Count binary substrings
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1421-count-binary-substrings.apl
# apl-source:6

# apl-source:7
# نحسب أطوال المجموعات المتتالية
# apl-source:8
# كل جارين يعطيان أقل طولهما من المقاطع
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
def عد_ثنائية(نص_):
  # apl-source:19
  سابق = 0
  # apl-source:20
  حالي = 1
  # apl-source:21
  مجموع = 0
  # apl-source:22
  for ع in range(1, len(نص_)):
    # apl-source:23
    if نص_[ع] == نص_[ع - 1]:
      # apl-source:24
      حالي = حالي + 1
    # apl-source:25
    else:
      # apl-source:26
      مجموع = مجموع + min(سابق, حالي)
      # apl-source:27
      سابق = حالي
      # apl-source:28
      حالي = 1
  # apl-source:29
  return مجموع + min(سابق, حالي)
# apl-source:30

# apl-source:31
تأكد_يساوي(عد_ثنائية("00110011"), 6, "ستة")
# apl-source:32
تأكد_يساوي(عد_ثنائية("10101"), 4, "أربعة")
# apl-source:33
تأكد_يساوي(عد_ثنائية("0"), 0, "صفر")
# apl-source:34
