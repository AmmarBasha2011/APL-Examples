
# apl-source:1
# مثال 1391 — مجموع فيبوناتشي الزوجي
# apl-source:2
# Sum of even Fibonacci terms
# apl-source:3
# Demonstrates: رياضيات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1391-even-fibonacci-sum.apl
# apl-source:6

# apl-source:7
# نولد الحدود ونجمع الزوجي منها
# apl-source:8
# كل ثالث حد زوجي
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
def مجموع_زوجي(حد):
  # apl-source:19
  أ = 1
  # apl-source:20
  ب = 2
  # apl-source:21
  مجموع = 0
  # apl-source:22
  while أ <= حد:
    # apl-source:23
    if أ % 2 == 0:
      # apl-source:24
      مجموع = مجموع + أ
    # apl-source:25
    ت = أ + ب
    # apl-source:26
    أ = ب
    # apl-source:27
    ب = ت
  # apl-source:28
  return مجموع
# apl-source:29

# apl-source:30
تأكد_يساوي(مجموع_زوجي(10), 10, "عشرة")
# apl-source:31
تأكد_يساوي(مجموع_زوجي(100), 44, "مئة")
# apl-source:32
تأكد_يساوي(مجموع_زوجي(4000000), 4613732, "أربعة ملايين")
# apl-source:33
