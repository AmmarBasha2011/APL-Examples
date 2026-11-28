
# apl-source:1
# مثال 1678 — اتجاه الدوران بين ثلاث نقاط
# apl-source:2
# Turn direction of three points
# apl-source:3
# Demonstrates: هندسة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1678-cross-product-sign-turn.apl
# apl-source:6

# apl-source:7
# نحسب جداء المتجهين
# apl-source:8
# موجب يسار وسالب يمين وصفر استقامة
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
def اتجاه(أ, ب, ج):
  # apl-source:19
  ق = (ب[0] - أ[0]) * (ج[1] - أ[1]) - (ب[1] - أ[1]) * (ج[0] - أ[0])
  # apl-source:20
  if ق > 0:
    # apl-source:21
    return "يسار"
  # apl-source:22
  if ق < 0:
    # apl-source:23
    return "يمين"
  # apl-source:24
  return "مستقيم"
# apl-source:25

# apl-source:26
تأكد_يساوي(اتجاه([0, 0], [1, 0], [1, 1]), "يسار", "يسار")
# apl-source:27
تأكد_يساوي(اتجاه([0, 0], [1, 0], [1, -1]), "يمين", "يمين")
# apl-source:28
تأكد_يساوي(اتجاه([0, 0], [1, 1], [2, 2]), "مستقيم", "مستقيم")
# apl-source:29
