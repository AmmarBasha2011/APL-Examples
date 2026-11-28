
# apl-source:1
# مثال 2129 — الأعداد السداسية المركزية
# apl-source:2
# Centered hexagonal numbers
# apl-source:3
# Demonstrates: متتاليات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2129-centered-hexagonal-numbers-list.apl
# apl-source:6

# apl-source:7
# # عدد النقاط في سداسي مركزي
# apl-source:8
# # 1 و7 و19 و37 و61
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
def مركزية(ن):
  # apl-source:19
  خرج = []
  # apl-source:20
  for ك in range(1, ن + 1):
    # apl-source:21
    خرج = خرج + [3 * ك * (ك - 1) + 1]
  # apl-source:22
  return خرج
# apl-source:23

# apl-source:24
تأكد_يساوي(مركزية(5), [1, 7, 19, 37, 61], "خمسة")
# apl-source:25
تأكد_يساوي(مركزية(1), [1], "واحد")
# apl-source:26
