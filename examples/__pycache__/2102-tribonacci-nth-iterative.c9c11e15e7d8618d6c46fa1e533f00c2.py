
# apl-source:1
# مثال 2102 — متتالية تريبوناتشي
# apl-source:2
# Tribonacci
# apl-source:3
# Demonstrates: متتاليات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2102-tribonacci-nth-iterative.apl
# apl-source:6

# apl-source:7
# # نبدأ بـ 0 و1 و1
# apl-source:8
# # ونحتفظ بآخر ثلاثة فقط
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
def تريب(ن):
  # apl-source:19
  if ن == 0:
    # apl-source:20
    return 0
  # apl-source:21
  ا = 0
  # apl-source:22
  ب = 1
  # apl-source:23
  ج = 1
  # apl-source:24
  for ك in range(ن - 1):
    # apl-source:25
    د = ا + ب + ج
    # apl-source:26
    ا = ب
    # apl-source:27
    ب = ج
    # apl-source:28
    ج = د
  # apl-source:29
  return ب
# apl-source:30

# apl-source:31
تأكد_يساوي(تريب(0), 0, "٠")
# apl-source:32
تأكد_يساوي(تريب(1), 1, "١")
# apl-source:33
تأكد_يساوي(تريب(4), 4, "٤")
# apl-source:34
تأكد_يساوي(تريب(25), 1389537, "٢٥")
# apl-source:35
