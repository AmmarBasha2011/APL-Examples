
# apl-source:1
# مثال 2081 — نسبة التغير المئوية
# apl-source:2
# Percentage change
# apl-source:3
# Demonstrates: مالية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2081-percentage-change-rounded-one-decimal.apl
# apl-source:6

# apl-source:7
# # النتيجة السالبة تعني انخفاضا
# apl-source:8
# # نقرب لمنزلة عشرية
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
def تغير(قديم, جديد):
  # apl-source:19
  return round((جديد - قديم) * 100 / قديم, 1)
# apl-source:20

# apl-source:21
تأكد_يساوي(تغير(50, 75), 50.0, "ارتفاع")
# apl-source:22
تأكد_يساوي(تغير(80, 60), -25.0, "انخفاض")
# apl-source:23
تأكد_يساوي(تغير(40, 40), 0.0, "ثابت")
# apl-source:24
