
# apl-source:1
# مثال 2293 — هل هي مصفوفة الوحدة
# apl-source:2
# Is identity
# apl-source:3
# Demonstrates: مصفوفات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2293-matrix-is-identity-check.apl
# apl-source:6

# apl-source:7
# # مصفوفة من قوائم
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
def ف(م):
  # apl-source:19
  for ي in range(len(م)):
    # apl-source:20
    for ك in range(len(م)):
      # apl-source:21
      if ي == ك and م[ي][ك] != 1:
        # apl-source:22
        return False
      # apl-source:23
      if ي != ك and م[ي][ك] != 0:
        # apl-source:24
        return False
  # apl-source:25
  return True
# apl-source:26

# apl-source:27
تأكد_يساوي(ف([[1, 2], [3, 4]]), False, "حالة 1")
# apl-source:28
تأكد_يساوي(ف([[5]]), False, "حالة 2")
# apl-source:29
تأكد_يساوي(ف([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), False, "حالة 3")
# apl-source:30
تأكد_يساوي(ف([[0, 1], [1, 0]]), False, "حالة 4")
# apl-source:31
تأكد_يساوي(ف([[2, -1, 0], [0, 3, 1], [1, 1, 1]]), False, "حالة 5")
# apl-source:32
تأكد_يساوي(ف([[1, 0], [0, 1]]), True, "حالة 6")
# apl-source:33
