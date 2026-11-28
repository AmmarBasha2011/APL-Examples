
# apl-source:1
# مثال 1059 — أقل مربعات كاملة
# apl-source:2
# Least number of perfect squares
# apl-source:3
# Demonstrates: برمجة ديناميكية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1059-perfect-squares-dp.apl
# apl-source:6

# apl-source:7
# لكل عدد نجرب طرح كل مربع كامل لا يتجاوزه
# apl-source:8
# ونأخذ أقل عدد مربعات للباقي مضافاً إليه واحد
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
def اقل_مربعات(ن):
  # apl-source:19
  د = [0] * (ن + 1)
  # apl-source:20
  for ع in range(1, ن + 1):
    # apl-source:21
    د[ع] = ع
    # apl-source:22
    ج = 1
    # apl-source:23
    while (ج * ج) <= ع:
      # apl-source:24
      if (د[ع - (ج * ج)] + 1) < د[ع]:
        # apl-source:25
        د[ع] = د[ع - (ج * ج)] + 1
      # apl-source:26
      ج = ج + 1
  # apl-source:27
  return د[ن]
# apl-source:28

# apl-source:29
تأكد_يساوي(اقل_مربعات(12), 3, "4 و4 و4")
# apl-source:30
تأكد_يساوي(اقل_مربعات(13), 2, "4 و9")
# apl-source:31
تأكد_يساوي(اقل_مربعات(1), 1, "واحد")
# apl-source:32
تأكد_يساوي(اقل_مربعات(7), 4, "4 و1 و1 و1")
# apl-source:33
