
# apl-source:1
# مثال 2127 — الأعداد الخماسية
# apl-source:2
# Pentagonal numbers first terms
# apl-source:3
# Demonstrates: متتاليات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2127-pentagonal-numbers-first-terms.apl
# apl-source:6

# apl-source:7
# # أول خمسة حدود
# apl-source:8
# # 1 و5 و12 و22 و35
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
def خماسية(ن):
  # apl-source:19
  خرج = []
  # apl-source:20
  for ك in range(1, ن + 1):
    # apl-source:21
    خرج = خرج + [ك * (3 * ك - 1) // 2]
  # apl-source:22
  return خرج
# apl-source:23

# apl-source:24
تأكد_يساوي(خماسية(5), [1, 5, 12, 22, 35], "خمسة")
# apl-source:25
تأكد_يساوي(خماسية(0), [], "صفر")
# apl-source:26
