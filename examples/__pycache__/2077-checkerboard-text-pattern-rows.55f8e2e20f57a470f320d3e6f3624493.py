
# apl-source:1
# مثال 2077 — نمط رقعة الشطرنج النصي
# apl-source:2
# Checkerboard text pattern
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2077-checkerboard-text-pattern-rows.apl
# apl-source:6

# apl-source:7
# # نبدأ الصف بنفس العلامة إذا كان رقمه زوجيا
# apl-source:8
# # ونعكس في الصف الفردي
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
def رقعة(ن):
  # apl-source:19
  خرج = []
  # apl-source:20
  for ي in range(ن):
    # apl-source:21
    صف = ""
    # apl-source:22
    for ك in range(ن):
      # apl-source:23
      if (ي + ك) % 2 == 0:
        # apl-source:24
        صف = صف + "#"
      # apl-source:25
      else:
        # apl-source:26
        صف = صف + "."
    # apl-source:27
    خرج = خرج + [صف]
  # apl-source:28
  return خرج
# apl-source:29

# apl-source:30
تأكد_يساوي(رقعة(3), ["#.#", ".#.", "#.#"], "٣")
# apl-source:31
تأكد_يساوي(رقعة(1), ["#"], "١")
# apl-source:32
تأكد_يساوي(رقعة(0), [], "صفر")
# apl-source:33
