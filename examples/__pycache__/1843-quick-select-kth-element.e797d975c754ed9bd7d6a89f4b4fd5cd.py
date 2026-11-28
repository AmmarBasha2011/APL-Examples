
# apl-source:1
# مثال 1843 — اختيار العنصر ذو الترتيب ك
# apl-source:2
# Quickselect kth smallest
# apl-source:3
# Demonstrates: فرز
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1843-quick-select-kth-element.apl
# apl-source:6

# apl-source:7
# نقسم حول المحور
# apl-source:8
# نكمل في الجزء الذي فيه الترتيب
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
def اختر(ق, ك):
  # apl-source:19
  محور = ق[0]
  # apl-source:20
  أصغر_قائمة = []
  # apl-source:21
  مساوي = []
  # apl-source:22
  أكبر_قائمة = []
  # apl-source:23
  for ع in ق:
    # apl-source:24
    if ع < محور:
      # apl-source:25
      أصغر_قائمة.append(ع)
    # apl-source:26
    elif ع == محور:
      # apl-source:27
      مساوي.append(ع)
    # apl-source:28
    else:
      # apl-source:29
      أكبر_قائمة.append(ع)
  # apl-source:30
  if ك < len(أصغر_قائمة):
    # apl-source:31
    return اختر(أصغر_قائمة, ك)
  # apl-source:32
  if ك < len(أصغر_قائمة) + len(مساوي):
    # apl-source:33
    return محور
  # apl-source:34
  return اختر(أكبر_قائمة, ك - len(أصغر_قائمة) - len(مساوي))
# apl-source:35

# apl-source:36
تأكد_يساوي(اختر([7, 2, 9, 4, 1], 0), 1, "الأصغر")
# apl-source:37
تأكد_يساوي(اختر([7, 2, 9, 4, 1], 2), 4, "الأوسط")
# apl-source:38
تأكد_يساوي(اختر([7, 2, 9, 4, 1], 4), 9, "الأكبر")
# apl-source:39
