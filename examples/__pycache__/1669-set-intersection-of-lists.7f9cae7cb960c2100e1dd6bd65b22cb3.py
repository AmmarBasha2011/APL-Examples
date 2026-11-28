
# apl-source:1
# مثال 1669 — تقاطع قائمتين
# apl-source:2
# Intersection of two lists
# apl-source:3
# Demonstrates: مجموعات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1669-set-intersection-of-lists.apl
# apl-source:6

# apl-source:7
# نمر على الأولى
# apl-source:8
# نضيف ما كان في الثانية ولم يُضف
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
def تقاطع(أ, ب):
  # apl-source:19
  ناتج = []
  # apl-source:20
  for ع in أ:
    # apl-source:21
    if ع in ب:
      # apl-source:22
      if (ع in ناتج) == False:
        # apl-source:23
        ناتج.append(ع)
  # apl-source:24
  return ناتج
# apl-source:25

# apl-source:26
تأكد_يساوي(تقاطع([1, 2, 2, 3], [2, 3, 4]), [2, 3], "مشترك")
# apl-source:27
تأكد_يساوي(تقاطع([1], [2]), [], "لا مشترك")
# apl-source:28
تأكد_يساوي(تقاطع([5, 5], [5]), [5], "تكرار")
# apl-source:29
