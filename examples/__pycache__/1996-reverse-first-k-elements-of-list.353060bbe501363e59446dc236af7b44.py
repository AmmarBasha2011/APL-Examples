
# apl-source:1
# مثال 1996 — عكس أول ك عنصرا في القائمة
# apl-source:2
# Reverse first k elements
# apl-source:3
# Demonstrates: قوائم
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1996-reverse-first-k-elements-of-list.apl
# apl-source:6

# apl-source:7
# # نقسم القائمة عند الموضع ك
# apl-source:8
# # ونعكس الجزء الأول فقط
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
def اعكس_اول(ق, ك):
  # apl-source:19
  جزء = ق[:ك]
  # apl-source:20
  جزء.reverse()
  # apl-source:21
  return جزء + ق[ك:]
# apl-source:22

# apl-source:23
تأكد_يساوي(اعكس_اول([1, 2, 3, 4, 5], 3), [3, 2, 1, 4, 5], "ثلاثة")
# apl-source:24
تأكد_يساوي(اعكس_اول([1, 2, 3], 0), [1, 2, 3], "صفر")
# apl-source:25
تأكد_يساوي(اعكس_اول([1, 2, 3], 3), [3, 2, 1], "الكل")
# apl-source:26
