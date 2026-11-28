
# apl-source:1
# مثال 1928 — عدد مرات ظهور نص كتتابع
# apl-source:2
# Count distinct subsequence matches
# apl-source:3
# Demonstrates: برمجة ديناميكية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1928-count-distinct-subsequence-matches.apl
# apl-source:6

# apl-source:7
# مصفوفة عدّ بطول الهدف
# apl-source:8
# نحدث من اليمين لنتجنب الاستعمال المزدوج
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
def عدد_تتابعات(س, هدف):
  # apl-source:19
  د = [1]
  # apl-source:20
  for ك in range(len(هدف)):
    # apl-source:21
    د = د + [0]
  # apl-source:22
  for ح in س:
    # apl-source:23
    for ي in range(len(هدف), 0, -1):
      # apl-source:24
      if هدف[ي - 1] == ح:
        # apl-source:25
        د[ي] = د[ي] + د[ي - 1]
  # apl-source:26
  return د[len(هدف)]
# apl-source:27

# apl-source:28
تأكد_يساوي(عدد_تتابعات("rabbbit", "rabbit"), 3, "rabbit")
# apl-source:29
تأكد_يساوي(عدد_تتابعات("babgbag", "bag"), 5, "bag")
# apl-source:30
تأكد_يساوي(عدد_تتابعات("abc", "d"), 0, "لا يوجد")
# apl-source:31
