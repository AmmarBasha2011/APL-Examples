
# apl-source:1
# مثال 1245 — جمع قائمتين من الأرقام
# apl-source:2
# Add two numbers as reversed digit lists
# apl-source:3
# Demonstrates: حمل
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1245-add-two-digit-lists.apl
# apl-source:6

# apl-source:7
# نجمع خانة بخانة مع الحمل
# apl-source:8
# وننتهي عند فراغ القائمتين والحمل
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
def اجمع(أ, ب):
  # apl-source:19
  ناتج = []
  # apl-source:20
  حمل = 0
  # apl-source:21
  ع = 0
  # apl-source:22
  while (ع < len(أ)) or (ع < len(ب)) or (حمل > 0):
    # apl-source:23
    س = حمل
    # apl-source:24
    if ع < len(أ):
      # apl-source:25
      س = س + أ[ع]
    # apl-source:26
    if ع < len(ب):
      # apl-source:27
      س = س + ب[ع]
    # apl-source:28
    ناتج = ناتج + [س % 10]
    # apl-source:29
    حمل = س // 10
    # apl-source:30
    ع = ع + 1
  # apl-source:31
  return ناتج
# apl-source:32

# apl-source:33
تأكد_يساوي(اجمع([2,4,3], [5,6,4]), [7,0,8], "342 + 465")
# apl-source:34
تأكد_يساوي(اجمع([0], [0]), [0], "صفران")
# apl-source:35
تأكد_يساوي(اجمع([9,9,9], [1]), [0,0,0,1], "حمل أخير")
# apl-source:36
تأكد_يساوي(اجمع([5], [5]), [0,1], "عشرة")
# apl-source:37
