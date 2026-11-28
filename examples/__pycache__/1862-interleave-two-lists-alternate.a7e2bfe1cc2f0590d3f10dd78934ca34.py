
# apl-source:1
# مثال 1862 — تقاطع عناصر قائمتين بالتناوب
# apl-source:2
# Interleave two lists
# apl-source:3
# Demonstrates: مصفوفات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1862-interleave-two-lists-alternate.apl
# apl-source:6

# apl-source:7
# نمر حتى نهاية الأطول
# apl-source:8
# نتجاوز القائمة المنتهية
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
def تناوب(أ, ب):
  # apl-source:19
  ناتج = []
  # apl-source:20
  for ك in range(max(len(أ), len(ب))):
    # apl-source:21
    if ك < len(أ):
      # apl-source:22
      ناتج.append(أ[ك])
    # apl-source:23
    if ك < len(ب):
      # apl-source:24
      ناتج.append(ب[ك])
  # apl-source:25
  return ناتج
# apl-source:26

# apl-source:27
تأكد_يساوي(تناوب([1, 2, 3], [10, 20]), [1, 10, 2, 20, 3], "طولان")
# apl-source:28
تأكد_يساوي(تناوب([], [1]), [1], "فارغة")
# apl-source:29
تأكد_يساوي(تناوب([1], [2]), [1, 2], "عنصران")
# apl-source:30
