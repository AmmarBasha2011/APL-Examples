
# apl-source:1
# مثال 1003 — نقل الأصفار
# apl-source:2
# Move zeroes
# apl-source:3
# Demonstrates: مؤشر كتابة واحد
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1003-move-zeroes.apl
# apl-source:6

# apl-source:7
# نكتب العناصر غير الصفرية بالترتيب ثم نملأ الباقي أصفاراً
# apl-source:8
# بلا قائمة إضافية
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
def انقل_اصفار(ق):
  # apl-source:19
  ك = 0
  # apl-source:20
  for ع in range(len(ق)):
    # apl-source:21
    if ق[ع] != 0:
      # apl-source:22
      ق[ك] = ق[ع]
      # apl-source:23
      ك = ك + 1
  # apl-source:24
  for ع in range(ك, len(ق)):
    # apl-source:25
    ق[ع] = 0
  # apl-source:26
  return ق
# apl-source:27

# apl-source:28
تأكد_يساوي(انقل_اصفار([0, 1, 0, 3, 12]), [1, 3, 12, 0, 0], "مثال أول")
# apl-source:29
تأكد_يساوي(انقل_اصفار([0, 0, 1]), [1, 0, 0], "أصفار البداية")
# apl-source:30
تأكد_يساوي(انقل_اصفار([5, 6]), [5, 6], "بلا أصفار")
# apl-source:31
