
# apl-source:1
# مثال 2010 — إيجاد قمة بالبحث الثنائي
# apl-source:2
# Find peak element
# apl-source:3
# Demonstrates: بحث ثنائي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2010-find-peak-element-binary-search.apl
# apl-source:6

# apl-source:7
# # إن كان الجار الأيمن أكبر فالقمة على اليمين
# apl-source:8
# # وإلا فهي عند الموضع أو على اليسار
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
def قمة(ق):
  # apl-source:19
  ي = 0
  # apl-source:20
  ل = len(ق) - 1
  # apl-source:21
  while ي < ل:
    # apl-source:22
    وس = (ي + ل) // 2
    # apl-source:23
    if ق[وس] < ق[وس + 1]:
      # apl-source:24
      ي = وس + 1
    # apl-source:25
    else:
      # apl-source:26
      ل = وس
  # apl-source:27
  return ي
# apl-source:28

# apl-source:29
تأكد_يساوي(قمة([1, 2, 3, 1]), 2, "قمة واحدة")
# apl-source:30
تأكد_يساوي(قمة([1, 2, 1, 3, 5, 6, 4]), 5, "قمتان")
# apl-source:31
تأكد_يساوي(قمة([5]), 0, "عنصر")
# apl-source:32
