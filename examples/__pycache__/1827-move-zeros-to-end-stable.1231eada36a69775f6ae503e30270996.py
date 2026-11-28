
# apl-source:1
# مثال 1827 — نقل الأصفار للنهاية
# apl-source:2
# Move zeros to the end
# apl-source:3
# Demonstrates: مصفوفات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1827-move-zeros-to-end-stable.apl
# apl-source:6

# apl-source:7
# نكتب غير الأصفار أولاً
# apl-source:8
# نملأ الباقي أصفاراً
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
def انقل_الأصفار(ق):
  # apl-source:19
  ناتج = []
  # apl-source:20
  for ع in ق:
    # apl-source:21
    if ع != 0:
      # apl-source:22
      ناتج.append(ع)
  # apl-source:23
  for ك in range(len(ق) - len(ناتج)):
    # apl-source:24
    ناتج.append(0)
  # apl-source:25
  return ناتج
# apl-source:26

# apl-source:27
تأكد_يساوي(انقل_الأصفار([0, 1, 0, 3, 12]), [1, 3, 12, 0, 0], "خمسة")
# apl-source:28
تأكد_يساوي(انقل_الأصفار([0]), [0], "صفر")
# apl-source:29
تأكد_يساوي(انقل_الأصفار([1, 2]), [1, 2], "بلا أصفار")
# apl-source:30
