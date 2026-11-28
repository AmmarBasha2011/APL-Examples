
# apl-source:1
# مثال 1122 — تسطيح القوائم المتداخلة
# apl-source:2
# Flatten nested list iterator
# apl-source:3
# Demonstrates: تفكيك من الأمام
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1122-flatten-nested.apl
# apl-source:6

# apl-source:7
# نأخذ العنصر الأول من المقدمة
# apl-source:8
# لو كان قائمة فككناه ووضعنا عناصره في المقدمة وإلا أخرجناه
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
def سطّح(قائمة_):
  # apl-source:19
  مقدمة = list(قائمة_)
  # apl-source:20
  ناتج = []
  # apl-source:21
  while len(مقدمة) > 0:
    # apl-source:22
    ع = مقدمة.pop(0)
    # apl-source:23
    if isinstance(ع, list):
      # apl-source:24
      مقدمة = ع + مقدمة
    # apl-source:25
    else:
      # apl-source:26
      ناتج = ناتج + [ع]
  # apl-source:27
  return ناتج
# apl-source:28

# apl-source:29
تأكد_يساوي(سطّح([[1, 1], 2, [1, 1]]), [1, 1, 2, 1, 1], "مثال أول")
# apl-source:30
تأكد_يساوي(سطّح([1, [4, [6]]]), [1, 4, 6], "ثلاثة مستويات")
# apl-source:31
تأكد_يساوي(سطّح([]), [], "فارغة")
# apl-source:32
تأكد_يساوي(سطّح([[[]], []]), [], "قوائم فارغة متداخلة")
# apl-source:33
