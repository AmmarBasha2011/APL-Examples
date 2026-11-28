
# apl-source:1
# مثال 1758 — أطول متتالية متزايدة
# apl-source:2
# Longest increasing subsequence length
# apl-source:3
# Demonstrates: برمجة ديناميكية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1758-longest-increasing-subsequence-len.apl
# apl-source:6

# apl-source:7
# نقارن مع كل عنصر قبله
# apl-source:8
# نأخذ أكبر قيمة
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
def أطول_متزايدة(ق):
  # apl-source:19
  if len(ق) == 0:
    # apl-source:20
    return 0
  # apl-source:21
  ط = []
  # apl-source:22
  for ك in ق:
    # apl-source:23
    ط.append(1)
  # apl-source:24
  for ي in range(len(ق)):
    # apl-source:25
    for ك in range(ي):
      # apl-source:26
      if ق[ك] < ق[ي]:
        # apl-source:27
        ط[ي] = max(ط[ي], ط[ك] + 1)
  # apl-source:28
  أفضل = 0
  # apl-source:29
  for ع in ط:
    # apl-source:30
    أفضل = max(أفضل, ع)
  # apl-source:31
  return أفضل
# apl-source:32

# apl-source:33
تأكد_يساوي(أطول_متزايدة([10, 9, 2, 5, 3, 7, 101, 18]), 4, "أربعة")
# apl-source:34
تأكد_يساوي(أطول_متزايدة([5, 4, 3]), 1, "هابطة")
# apl-source:35
تأكد_يساوي(أطول_متزايدة([]), 0, "فارغة")
# apl-source:36
