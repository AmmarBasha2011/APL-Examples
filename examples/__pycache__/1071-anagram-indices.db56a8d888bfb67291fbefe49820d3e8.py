
# apl-source:1
# مثال 1071 — مواضع الجناسات
# apl-source:2
# Find all anagram start indices
# apl-source:3
# Demonstrates: نافذة ثابتة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1071-anagram-indices.apl
# apl-source:6

# apl-source:7
# نافذة بطول النمط تنزلق على النص
# apl-source:8
# نقارن حروفها مرتبة بحروف النمط مرتبة
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
def مواضع(نص_, نمط):
  # apl-source:19
  م = len(نمط)
  # apl-source:20
  هدف = sorted(list(نمط))
  # apl-source:21
  ناتج = []
  # apl-source:22
  for ع in range((len(نص_) - م) + 1):
    # apl-source:23
    if sorted(list(نص_[ع:ع + م])) == هدف:
      # apl-source:24
      ناتج = ناتج + [ع]
  # apl-source:25
  return ناتج
# apl-source:26

# apl-source:27
تأكد_يساوي(مواضع("cbaebabacd", "abc"), [0, 6], "موضعان")
# apl-source:28
تأكد_يساوي(مواضع("abab", "ab"), [0, 1, 2], "ثلاثة")
# apl-source:29
تأكد_يساوي(مواضع("a", "ab"), [], "نص أقصر")
# apl-source:30
