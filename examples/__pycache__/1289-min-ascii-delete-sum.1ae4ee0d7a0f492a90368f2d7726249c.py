
# apl-source:1
# مثال 1289 — أقل مجموع حذف
# apl-source:2
# Minimum ASCII delete sum for two strings
# apl-source:3
# Demonstrates: برمجة ديناميكية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1289-min-ascii-delete-sum.apl
# apl-source:6

# apl-source:7
# نحسب أكبر مجموع رموز لمتتالية مشتركة
# apl-source:8
# والباقي هو المحذوف
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
def اقل_مجموع_حذف(أ, ب):
  # apl-source:19
  د = []
  # apl-source:20
  for ع in range(len(أ) + 1):
    # apl-source:21
    د = د + [[0] * (len(ب) + 1)]
  # apl-source:22
  for ع in range(1, len(أ) + 1):
    # apl-source:23
    for ج in range(1, len(ب) + 1):
      # apl-source:24
      if أ[ع - 1] == ب[ج - 1]:
        # apl-source:25
        د[ع][ج] = د[ع - 1][ج - 1] + ord(أ[ع - 1])
      # apl-source:26
      else:
        # apl-source:27
        د[ع][ج] = max(د[ع - 1][ج], د[ع][ج - 1])
  # apl-source:28
  كل = 0
  # apl-source:29
  for ح in أ + ب:
    # apl-source:30
    كل = كل + ord(ح)
  # apl-source:31
  return كل - 2 * د[len(أ)][len(ب)]
# apl-source:32

# apl-source:33
تأكد_يساوي(اقل_مجموع_حذف("sea", "eat"), 231, "مثال أول")
# apl-source:34
تأكد_يساوي(اقل_مجموع_حذف("delete", "leet"), 403, "مثال ثان")
# apl-source:35
تأكد_يساوي(اقل_مجموع_حذف("a", "a"), 0, "متطابقان")
# apl-source:36
