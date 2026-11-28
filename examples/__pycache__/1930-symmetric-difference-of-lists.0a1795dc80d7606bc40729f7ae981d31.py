
# apl-source:1
# مثال 1930 — الفرق المتماثل بين قائمتين
# apl-source:2
# Symmetric difference of two lists
# apl-source:3
# Demonstrates: مجموعات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1930-symmetric-difference-of-lists.apl
# apl-source:6

# apl-source:7
# نأخذ ما في الأولى وليس في الثانية
# apl-source:8
# ثم العكس
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
def فرق_متماثل(أ, ب):
  # apl-source:19
  خرج = []
  # apl-source:20
  for ع in أ:
    # apl-source:21
    if (ع in ب) == False:
      # apl-source:22
      خرج = خرج + [ع]
  # apl-source:23
  for ع in ب:
    # apl-source:24
    if (ع in أ) == False:
      # apl-source:25
      خرج = خرج + [ع]
  # apl-source:26
  return خرج
# apl-source:27

# apl-source:28
تأكد_يساوي(فرق_متماثل([1, 2, 3], [2, 3, 4]), [1, 4], "مشترك")
# apl-source:29
تأكد_يساوي(فرق_متماثل([1], [2]), [1, 2], "منفصلتان")
# apl-source:30
تأكد_يساوي(فرق_متماثل([5, 6], [5, 6]), [], "متطابقتان")
# apl-source:31
