
# apl-source:1
# مثال 1068 — الأسهم بصفقتين
# apl-source:2
# Best time to buy and sell stock twice
# apl-source:3
# Demonstrates: أربع حالات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1068-stock-two-transactions.apl
# apl-source:6

# apl-source:7
# نتتبع أفضل رصيد بعد أول شراء وأول بيع وثاني شراء وثاني بيع
# apl-source:8
# ونحدثها يوماً بعد يوم
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
def اعظم(أ, ب):
  # apl-source:19
  if أ > ب:
    # apl-source:20
    return أ
  # apl-source:21
  return ب
# apl-source:22

# apl-source:23
def ربح_صفقتين(اسعار):
  # apl-source:24
  ش1 = -1000000000
  # apl-source:25
  ب1 = 0
  # apl-source:26
  ش2 = -1000000000
  # apl-source:27
  ب2 = 0
  # apl-source:28
  for س in اسعار:
    # apl-source:29
    ش1 = اعظم(ش1, -س)
    # apl-source:30
    ب1 = اعظم(ب1, ش1 + س)
    # apl-source:31
    ش2 = اعظم(ش2, ب1 - س)
    # apl-source:32
    ب2 = اعظم(ب2, ش2 + س)
  # apl-source:33
  return ب2
# apl-source:34

# apl-source:35
تأكد_يساوي(ربح_صفقتين([3, 3, 5, 0, 0, 3, 1, 4]), 6, "صفقتان")
# apl-source:36
تأكد_يساوي(ربح_صفقتين([1, 2, 3, 4, 5]), 4, "صعود دائم")
# apl-source:37
تأكد_يساوي(ربح_صفقتين([7, 6, 4, 3, 1]), 0, "هبوط دائم")
# apl-source:38
