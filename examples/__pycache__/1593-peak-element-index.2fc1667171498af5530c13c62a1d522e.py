
# apl-source:1
# مثال 1593 — موضع قمة في المصفوفة
# apl-source:2
# Find a peak element index
# apl-source:3
# Demonstrates: مصفوفات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1593-peak-element-index.apl
# apl-source:6

# apl-source:7
# بحث ثنائي على الميل
# apl-source:8
# إن كان التالي أكبر فالقمة يمين
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
def موضع_قمة(أ):
  # apl-source:19
  ي = 0
  # apl-source:20
  ج = len(أ) - 1
  # apl-source:21
  while ي < ج:
    # apl-source:22
    م = (ي + ج) // 2
    # apl-source:23
    if أ[م] < أ[م + 1]:
      # apl-source:24
      ي = م + 1
    # apl-source:25
    else:
      # apl-source:26
      ج = م
  # apl-source:27
  return ي
# apl-source:28

# apl-source:29
نتيجة1 = موضع_قمة([1, 2, 3, 1])
# apl-source:30
تأكد_يساوي(نتيجة1, 2, "قمة")
# apl-source:31
قمة_ما = موضع_قمة([1, 2, 1, 3, 5, 6, 4])
# apl-source:32
تأكد_يساوي(قمة_ما == 1 or قمة_ما == 5, True, "قمتان")
# apl-source:33
تأكد_يساوي(موضع_قمة([5]), 0, "وحيد")
# apl-source:34
