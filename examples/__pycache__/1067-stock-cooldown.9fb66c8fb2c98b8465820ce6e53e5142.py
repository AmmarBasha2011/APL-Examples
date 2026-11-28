
# apl-source:1
# مثال 1067 — الأسهم مع فترة انتظار
# apl-source:2
# Best time to buy and sell stock with cooldown
# apl-source:3
# Demonstrates: آلة حالات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1067-stock-cooldown.apl
# apl-source:6

# apl-source:7
# ثلاث حالات: ممسك بسهم، باع اليوم، في راحة
# apl-source:8
# ننقل الأرباح بين الحالات يوماً بعد يوم
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
def ربح_راحة(اسعار):
  # apl-source:24
  ممسك = -1000000000
  # apl-source:25
  باع = 0
  # apl-source:26
  راحة = 0
  # apl-source:27
  for س in اسعار:
    # apl-source:28
    باع_سابق = باع
    # apl-source:29
    باع = ممسك + س
    # apl-source:30
    ممسك = اعظم(ممسك, راحة - س)
    # apl-source:31
    راحة = اعظم(راحة, باع_سابق)
  # apl-source:32
  return اعظم(باع, راحة)
# apl-source:33

# apl-source:34
تأكد_يساوي(ربح_راحة([1, 2, 3, 0, 2]), 3, "مثال")
# apl-source:35
تأكد_يساوي(ربح_راحة([1]), 0, "يوم واحد")
# apl-source:36
تأكد_يساوي(ربح_راحة([6, 1, 3, 2, 4, 7]), 6, "صعود متأخر")
# apl-source:37
