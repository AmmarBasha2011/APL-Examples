
# apl-source:1
# مثال 1670 — الفرق المتماثل لقائمتين
# apl-source:2
# Symmetric difference of two lists
# apl-source:3
# Demonstrates: مجموعات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1670-set-symmetric-difference-lists.apl
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
  ناتج = []
  # apl-source:20
  for ع in أ:
    # apl-source:21
    if (ع in ب) == False:
      # apl-source:22
      if (ع in ناتج) == False:
        # apl-source:23
        ناتج.append(ع)
  # apl-source:24
  for ع in ب:
    # apl-source:25
    if (ع in أ) == False:
      # apl-source:26
      if (ع in ناتج) == False:
        # apl-source:27
        ناتج.append(ع)
  # apl-source:28
  return ناتج
# apl-source:29

# apl-source:30
تأكد_يساوي(فرق_متماثل([1, 2, 3], [2, 3, 4]), [1, 4], "فرق")
# apl-source:31
تأكد_يساوي(فرق_متماثل([1], [1]), [], "متطابقتان")
# apl-source:32
تأكد_يساوي(فرق_متماثل([], [7]), [7], "فارغة")
# apl-source:33
