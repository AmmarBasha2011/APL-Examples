
# apl-source:1
# مثال 1788 — مجموع المضاعفات تحت حد
# apl-source:2
# Sum of multiples below limit
# apl-source:3
# Demonstrates: نظرية الأعداد
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1788-sum-multiples-three-five-limit.apl
# apl-source:6

# apl-source:7
# نمر على الأعداد
# apl-source:8
# نجمع من قبل أحد الشرطين
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
def مجموع_مضاعفات(حد):
  # apl-source:19
  مجموع = 0
  # apl-source:20
  for ك in range(حد):
    # apl-source:21
    if ك % 3 == 0 or ك % 5 == 0:
      # apl-source:22
      مجموع = مجموع + ك
  # apl-source:23
  return مجموع
# apl-source:24

# apl-source:25
تأكد_يساوي(مجموع_مضاعفات(10), 23, "عشرة")
# apl-source:26
تأكد_يساوي(مجموع_مضاعفات(1000), 233168, "ألف")
# apl-source:27
تأكد_يساوي(مجموع_مضاعفات(1), 0, "واحد")
# apl-source:28
