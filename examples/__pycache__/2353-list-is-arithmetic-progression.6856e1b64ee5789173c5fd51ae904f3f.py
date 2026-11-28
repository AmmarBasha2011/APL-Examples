
# apl-source:1
# مثال 2353 — هل هي متوالية حسابية
# apl-source:2
# Is arithmetic progression
# apl-source:3
# Demonstrates: قوائم
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2353-list-is-arithmetic-progression.apl
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
  for ي in range(2, len(ق)):
    # apl-source:20
    if ق[ي] - ق[ي - 1] != ق[1] - ق[0]:
      # apl-source:21
      return False
  # apl-source:22
  return True
# apl-source:23

# apl-source:24
تأكد_يساوي(ف([1, 3, 5]), True, "حالة 1")
# apl-source:25
تأكد_يساوي(ف([1, 2, 4]), False, "حالة 2")
# apl-source:26
تأكد_يساوي(ف([5, 5, 5]), True, "حالة 3")
# apl-source:27
تأكد_يساوي(ف([10, 7, 4, 1]), True, "حالة 4")
# apl-source:28
تأكد_يساوي(ف([1, 2]), True, "حالة 5")
# apl-source:29
