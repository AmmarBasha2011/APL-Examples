
# apl-source:1
# مثال 1702 — أكبر مجموع لمصفوفة جزئية
# apl-source:2
# Maximum subarray sum Kadane
# apl-source:3
# Demonstrates: مصفوفات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1702-max-subarray-kadane.apl
# apl-source:6

# apl-source:7
# نمدد الجزء أو نبدأ من جديد
# apl-source:8
# نحتفظ بأفضل مجموع
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
def كادان(ق):
  # apl-source:19
  حالي = ق[0]
  # apl-source:20
  أفضل = ق[0]
  # apl-source:21
  for ك in range(1, len(ق)):
    # apl-source:22
    حالي = max(ق[ك], حالي + ق[ك])
    # apl-source:23
    أفضل = max(أفضل, حالي)
  # apl-source:24
  return أفضل
# apl-source:25

# apl-source:26
تأكد_يساوي(كادان([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6, "كلاسيكي")
# apl-source:27
تأكد_يساوي(كادان([-3, -1, -2]), -1, "سالبة")
# apl-source:28
تأكد_يساوي(كادان([5]), 5, "واحد")
# apl-source:29
