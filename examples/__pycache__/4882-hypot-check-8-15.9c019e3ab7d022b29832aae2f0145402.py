
# apl-source:1
# مثال 4882 — هل مثلث أضلاعه مضاعفات (8,15) قائم؟
# apl-source:2
# Right triangle check with scale of (8,15)
# apl-source:3
# Demonstrates: مالية وهندسة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/4882-hypot-check-8-15.apl
# apl-source:6

# apl-source:7
# نتحقق من فيثاغورس: أ² + ب² = ج²
# apl-source:8

# apl-source:9
def تأكد_يساوي(فعلي, متوقع, اسم):
  # apl-source:10
  if فعلي != متوقع:
    # apl-source:11
    print("فشل:", اسم)
    # apl-source:12
    print("  متوقع:", متوقع)
    # apl-source:13
    print("  فعلي:", فعلي)
    # apl-source:14
    قياسي_نظام_اخرج(1)
  # apl-source:15
  print("ناجح:", اسم)
# apl-source:16

# apl-source:17
def ف(م, ج):
  # apl-source:18
  أ = 8 * م
  # apl-source:19
  ب = 15 * م
  # apl-source:20
  return أ * أ + ب * ب == ج * ج
# apl-source:21

# apl-source:22
تأكد_يساوي(ف(1, 1), False, "حالة 1")
# apl-source:23
تأكد_يساوي(ف(1, 5), False, "حالة 2")
# apl-source:24
تأكد_يساوي(ف(2, 10), False, "حالة 3")
# apl-source:25
تأكد_يساوي(ف(3, 3), False, "حالة 4")
# apl-source:26
