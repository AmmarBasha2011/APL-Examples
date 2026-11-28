
# apl-source:1
# مثال 1984 — مقارنة أرقام الإصدارات
# apl-source:2
# Semantic version compare
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1984-semantic-version-compare-three-parts.apl
# apl-source:6

# apl-source:7
# # 1.10 أكبر من 1.2 لأن المقارنة رقمية
# apl-source:8
# # ونرجع -1 أو 0 أو 1
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
def قارن(ا, ب):
  # apl-source:19
  ج1 = ا.split(".")
  # apl-source:20
  ج2 = ب.split(".")
  # apl-source:21
  ن = max(len(ج1), len(ج2))
  # apl-source:22
  for ك in range(ن):
    # apl-source:23
    س1 = 0
    # apl-source:24
    س2 = 0
    # apl-source:25
    if ك < len(ج1):
      # apl-source:26
      س1 = int(ج1[ك])
    # apl-source:27
    if ك < len(ج2):
      # apl-source:28
      س2 = int(ج2[ك])
    # apl-source:29
    if س1 < س2:
      # apl-source:30
      return -1
    # apl-source:31
    if س1 > س2:
      # apl-source:32
      return 1
  # apl-source:33
  return 0
# apl-source:34

# apl-source:35
تأكد_يساوي(قارن("1.2.3", "1.10.0"), -1, "أصغر")
# apl-source:36
تأكد_يساوي(قارن("2.0.0", "1.9.9"), 1, "أكبر")
# apl-source:37
تأكد_يساوي(قارن("1.0", "1.0.0"), 0, "متساويان")
# apl-source:38
تأكد_يساوي(قارن("1.0.1", "1.0"), 1, "جزء إضافي")
# apl-source:39
