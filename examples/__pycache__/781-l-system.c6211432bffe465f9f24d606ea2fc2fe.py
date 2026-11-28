
# apl-source:1
# مثال 781 — أنظمة ليندنماير
# apl-source:2
# L-systems
# apl-source:3
# Demonstrates: إعادة كتابة متوازية، نمو أسّي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/781-l-system.apl
# apl-source:6

# apl-source:7
# Assertion style:
# apl-source:8
#   دالة تأكد_يساوي(فعلي, متوقع, اسم):
# apl-source:9
#     لو فعلي != متوقع:
# apl-source:10
#       اطبع "فشل:", اسم
# apl-source:11
#       اطبع "  متوقع:", متوقع
# apl-source:12
#       اطبع "  فعلي:", فعلي
# apl-source:13
#       قياسي_نظام_اخرج(1)
# apl-source:14
#     اطبع "ناجح:", اسم
# apl-source:15

# apl-source:16
def تأكد_يساوي(فعلي, متوقع, اسم):
  # apl-source:17
  if فعلي != متوقع:
    # apl-source:18
    print("فشل:", اسم)
    # apl-source:19
    print("  متوقع:", متوقع)
    # apl-source:20
    print("  فعلي:", فعلي)
    # apl-source:21
    قياسي_نظام_اخرج(1)
  # apl-source:22
  print("ناجح:", اسم)
# apl-source:23

# apl-source:24
# أنظمة ليندنماير: إعادة كتابة متوازية للنصوص
# apl-source:25
# Demonstrates: استبدال متزامن لكل حرف, نمو أسّي, نموذج الطحالب وكوخ
# apl-source:26

# apl-source:27
def جيل(نص, مفاتيح, قيم):
  # apl-source:28
  جديد = ""
  # apl-source:29
  for حرف in نص:
    # apl-source:30
    if حرف in مفاتيح:
      # apl-source:31
      جديد = جديد + قيم[مفاتيح.index(حرف)]
    # apl-source:32
    else:
      # apl-source:33
      جديد = جديد + حرف
  # apl-source:34
  return جديد
# apl-source:35

# apl-source:36
def أجيال(بداية, مفاتيح, قيم, ن):
  # apl-source:37
  نص = بداية
  # apl-source:38
  for ي in range(ن):
    # apl-source:39
    نص = جيل(نص, مفاتيح, قيم)
  # apl-source:40
  return نص
# apl-source:41

# apl-source:42
تأكد_يساوي(أجيال("a", ["a", "b"], ["ab", "a"], 1), "ab", "طحالب جيل 1")
# apl-source:43
تأكد_يساوي(أجيال("a", ["a", "b"], ["ab", "a"], 2), "aba", "طحالب جيل 2")
# apl-source:44
تأكد_يساوي(أجيال("a", ["a", "b"], ["ab", "a"], 3), "abaab", "طحالب جيل 3")
# apl-source:45
تأكد_يساوي(أجيال("a", ["a", "b"], ["ab", "a"], 4), "abaababa", "طحالب جيل 4")
# apl-source:46
تأكد_يساوي(أجيال("a", ["a", "b"], ["ab", "a"], 5), "abaababaabaab", "طحالب جيل 5")
# apl-source:47
تأكد_يساوي(len(أجيال("a", ["a", "b"], ["ab", "a"], 7)), 34, "طول فيبوناتشي جيل 7")
# apl-source:48
تأكد_يساوي(أجيال("F", ["F"], ["F+F--F+F"], 1), "F+F--F+F", "كوخ جيل 1")
# apl-source:49
تأكد_يساوي(len(أجيال("F", ["F"], ["F+F--F+F"], 2)), 36, "كوخ طول جيل 2")
# apl-source:50
تأكد_يساوي(len(أجيال("F", ["F"], ["F+F--F+F"], 3)), 148, "كوخ طول جيل 3")
# apl-source:51
تأكد_يساوي(أجيال("X", ["X", "F"], ["F+[[X]-X]-F[-FX]+X", "FF"], 1), "F+[[X]-X]-F[-FX]+X", "نبات جيل 1")
# apl-source:52
