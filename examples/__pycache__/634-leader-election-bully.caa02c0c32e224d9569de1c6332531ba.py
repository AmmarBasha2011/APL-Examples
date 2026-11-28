
# apl-source:1
# مثال 634 — انتخاب قائد بالتنمر
# apl-source:2
# Bully leader election
# apl-source:3
# Demonstrates: انتخاب، أعلى معرف، موزع
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/634-leader-election-bully.apl
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
# انتخاب قائد بخوارزمية التنمر (Bully)
# apl-source:25
# Demonstrates: أعلى معرف يفوز, استجابة الأحياء, إعلان القائد
# apl-source:26
# عند سقوط القائد ينتخب الأحياء الأعلى معرفا
# apl-source:27

# apl-source:28
def انتخب(أحياء, مرشح):
  # apl-source:29
  أعلى = []
  # apl-source:30
  for عقدة in أحياء:
    # apl-source:31
    if عقدة > مرشح:
      # apl-source:32
      أعلى.append(عقدة)
  # apl-source:33
  if len(أعلى) == 0:
    # apl-source:34
    return مرشح
  # apl-source:35
  ردود = أعلى.copy()
  # apl-source:36
  ردود.sort()
  # apl-source:37
  return ردود[len(ردود) - 1]
# apl-source:38

# apl-source:39
تأكد_يساوي(انتخب([1, 2, 3, 4], 2), 4, "الأعلى يفوز")
# apl-source:40
تأكد_يساوي(انتخب([1, 2], 2), 2, "لا أعلى منه فيتولى")
# apl-source:41
تأكد_يساوي(انتخب([5, 1, 3], 1), 5, "بعد سقوط 5 يبقى 5 إن كان حيا")
# apl-source:42
أحياء = [1, 3, 4]
# apl-source:43
print("القائد من:", أحياء, " هو", انتخب(أحياء, 3))
# apl-source:44
تأكد_يساوي(انتخب(أحياء, 3), 4, "سقوط القائد 5 يخلي 4")
# apl-source:45
