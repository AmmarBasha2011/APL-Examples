
# apl-source:1
# مثال 1752 — توافيق ن من ك
# apl-source:2
# Binomial coefficient iterative
# apl-source:3
# Demonstrates: توافيق
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1752-n-choose-k-iterative.apl
# apl-source:6

# apl-source:7
# نستخدم الأصغر من ك و ن-ك
# apl-source:8
# القسمة دائماً صحيحة
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
def توافيق(ن, ك):
  # apl-source:19
  ك = min(ك, ن - ك)
  # apl-source:20
  ناتج = 1
  # apl-source:21
  for ي in range(ك):
    # apl-source:22
    ناتج = ناتج * (ن - ي) // (ي + 1)
  # apl-source:23
  return ناتج
# apl-source:24

# apl-source:25
تأكد_يساوي(توافيق(5, 2), 10, "خمسة")
# apl-source:26
تأكد_يساوي(توافيق(10, 3), 120, "عشرة")
# apl-source:27
تأكد_يساوي(توافيق(6, 0), 1, "صفر")
# apl-source:28
تأكد_يساوي(توافيق(6, 6), 1, "كاملة")
# apl-source:29
