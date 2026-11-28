
# apl-source:1
# مثال 1577 — أكبر قيمة في كل نافذة
# apl-source:2
# Sliding window maximum
# apl-source:3
# Demonstrates: نوافذ
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1577-sliding-window-maximum-naive.apl
# apl-source:6

# apl-source:7
# نمرر نافذة طولها ك
# apl-source:8
# نأخذ أكبر ما فيها في كل موضع
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
def أكبر_النوافذ(أ, ك):
  # apl-source:19
  ناتج = []
  # apl-source:20
  for ع in range(len(أ) - ك + 1):
    # apl-source:21
    أكبر_ = أ[ع]
    # apl-source:22
    for ز in range(ك):
      # apl-source:23
      if أ[ع + ز] > أكبر_:
        # apl-source:24
        أكبر_ = أ[ع + ز]
    # apl-source:25
    ناتج.append(أكبر_)
  # apl-source:26
  return ناتج
# apl-source:27

# apl-source:28
تأكد_يساوي(أكبر_النوافذ([1, 3, -1, -3, 5, 3, 6, 7], 3), [3, 3, 5, 5, 6, 7], "كلاسيكي")
# apl-source:29
تأكد_يساوي(أكبر_النوافذ([4, 2], 1), [4, 2], "نافذة واحدة")
# apl-source:30
تأكد_يساوي(أكبر_النوافذ([9, 8, 7], 3), [9], "نافذة كاملة")
# apl-source:31
