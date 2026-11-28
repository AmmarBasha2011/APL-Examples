
# apl-source:1
# مثال 1236 — موضع الإدراج
# apl-source:2
# Search insert position
# apl-source:3
# Demonstrates: بحث ثنائي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1236-search-insert-position.apl
# apl-source:6

# apl-source:7
# نبحث ثنائياً عن أول عنصر لا يقل عن القيمة
# apl-source:8
# وموضعه هو مكان الإدراج
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
def موضع(أ, ق):
  # apl-source:19
  ي = 0
  # apl-source:20
  ن = len(أ)
  # apl-source:21
  while ي < ن:
    # apl-source:22
    م = (ي + ن) // 2
    # apl-source:23
    if أ[م] < ق:
      # apl-source:24
      ي = م + 1
    # apl-source:25
    else:
      # apl-source:26
      ن = م
  # apl-source:27
  return ي
# apl-source:28

# apl-source:29
تأكد_يساوي(موضع([1,3,5,6], 5), 2, "موجود")
# apl-source:30
تأكد_يساوي(موضع([1,3,5,6], 2), 1, "بين عنصرين")
# apl-source:31
تأكد_يساوي(موضع([1,3,5,6], 7), 4, "في النهاية")
# apl-source:32
تأكد_يساوي(موضع([1,3,5,6], 0), 0, "في البداية")
# apl-source:33
تأكد_يساوي(موضع([], 3), 0, "فارغة")
# apl-source:34
