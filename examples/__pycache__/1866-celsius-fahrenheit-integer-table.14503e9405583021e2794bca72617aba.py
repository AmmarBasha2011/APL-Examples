
# apl-source:1
# مثال 1866 — جدول تحويل الحرارة
# apl-source:2
# Celsius to Fahrenheit table
# apl-source:3
# Demonstrates: حساب
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1866-celsius-fahrenheit-integer-table.apl
# apl-source:6

# apl-source:7
# ف = ص × 9 ÷ 5 + 32
# apl-source:8
# نختار قيماً قسمتها تامة
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
def إلى_فهرنهايت(ص):
  # apl-source:19
  return ص * 9 // 5 + 32
# apl-source:20

# apl-source:21
def جدول(قيم):
  # apl-source:22
  ناتج = []
  # apl-source:23
  for ع in قيم:
    # apl-source:24
    ناتج.append(إلى_فهرنهايت(ع))
  # apl-source:25
  return ناتج
# apl-source:26

# apl-source:27
تأكد_يساوي(إلى_فهرنهايت(0), 32, "تجمد")
# apl-source:28
تأكد_يساوي(إلى_فهرنهايت(100), 212, "غليان")
# apl-source:29
تأكد_يساوي(جدول([-40, 0, 5, 10]), [-40, 32, 41, 50], "جدول")
# apl-source:30
