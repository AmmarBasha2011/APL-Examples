
# apl-source:1
# مثال 2243 — دمج النصفين بالتبادل
# apl-source:2
# Interleave halves
# apl-source:3
# Demonstrates: قوائم
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2243-list-merge-two-halves-interleave.apl
# apl-source:6

# apl-source:7
# # نمرر القائمة
# apl-source:8
# # ونتحقق من الناتج
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
def ف(ق):
  # apl-source:19
  ن = len(ق) // 2
  # apl-source:20
  أ = ق[:ن]
  # apl-source:21
  ب = ق[ن:]
  # apl-source:22
  ر = []
  # apl-source:23
  for ي in range(len(ب)):
    # apl-source:24
    ر = ر + [ب[ي]]
    # apl-source:25
    if ي < len(أ):
      # apl-source:26
      ر = ر + [أ[ي]]
  # apl-source:27
  return ر
# apl-source:28

# apl-source:29
تأكد_يساوي(ف([3, 1, 2]), [1, 3, 2], "حالة 1")
# apl-source:30
تأكد_يساوي(ف([5]), [5], "حالة 2")
# apl-source:31
تأكد_يساوي(ف([1, 2, 3, 4, 5, 6]), [4, 1, 5, 2, 6, 3], "حالة 3")
# apl-source:32
تأكد_يساوي(ف([-2, 0, 7, 7, 4]), [7, -2, 7, 0, 4], "حالة 4")
# apl-source:33
تأكد_يساوي(ف([10, 20, 10, 30, 20, 10]), [30, 10, 20, 20, 10, 10], "حالة 5")
# apl-source:34
