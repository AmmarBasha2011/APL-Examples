
# apl-source:1
# مثال 1290 — إزالة متناظرة
# apl-source:2
# Minimum removals to make palindrome
# apl-source:3
# Demonstrates: برمجة ديناميكية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1290-palindrome-removal.apl
# apl-source:6

# apl-source:7
# الحذف الأدنى هو الطول ناقص أطول متتالية متناظرة
# apl-source:8
# نحسبها بجدول مجالات
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
def اقل_حذف_متناظرة(س):
  # apl-source:19
  ن = len(س)
  # apl-source:20
  if ن == 0:
    # apl-source:21
    return 0
  # apl-source:22
  د = []
  # apl-source:23
  for ع in range(ن):
    # apl-source:24
    د = د + [[0] * ن]
  # apl-source:25
  for ع in range(ن - 1, -1, -1):
    # apl-source:26
    د[ع][ع] = 1
    # apl-source:27
    for ج in range(ع + 1, ن):
      # apl-source:28
      if س[ع] == س[ج]:
        # apl-source:29
        د[ع][ج] = د[ع + 1][ج - 1] + 2
      # apl-source:30
      else:
        # apl-source:31
        د[ع][ج] = max(د[ع + 1][ج], د[ع][ج - 1])
  # apl-source:32
  return ن - د[0][ن - 1]
# apl-source:33

# apl-source:34
تأكد_يساوي(اقل_حذف_متناظرة("abca"), 1, "حذف واحد")
# apl-source:35
تأكد_يساوي(اقل_حذف_متناظرة("abcde"), 4, "كلها مختلفة")
# apl-source:36
تأكد_يساوي(اقل_حذف_متناظرة("racecar"), 0, "متناظرة")
# apl-source:37
تأكد_يساوي(اقل_حذف_متناظرة("aab"), 1, "اثنان متشابهان")
# apl-source:38
