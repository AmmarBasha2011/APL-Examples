
# apl-source:1
# مثال 2044 — إضافة واحد إلى عدد في قائمة أرقام
# apl-source:2
# Plus one on digit list
# apl-source:3
# Demonstrates: قوائم
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2044-plus-one-digit-list-carry.apl
# apl-source:6

# apl-source:7
# # التسعة تصبح صفرا مع حمل
# apl-source:8
# # وإن بقي حمل نضيف 1 في البداية
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
def زد_واحد(ق):
  # apl-source:19
  خرج = []
  # apl-source:20
  for ع in ق:
    # apl-source:21
    خرج = خرج + [ع]
  # apl-source:22
  ك = len(خرج) - 1
  # apl-source:23
  while ك >= 0:
    # apl-source:24
    if خرج[ك] < 9:
      # apl-source:25
      خرج[ك] = خرج[ك] + 1
      # apl-source:26
      return خرج
    # apl-source:27
    خرج[ك] = 0
    # apl-source:28
    ك = ك - 1
  # apl-source:29
  return [1] + خرج
# apl-source:30

# apl-source:31
تأكد_يساوي(زد_واحد([1, 2, 3]), [1, 2, 4], "عادي")
# apl-source:32
تأكد_يساوي(زد_واحد([9, 9]), [1, 0, 0], "تسعات")
# apl-source:33
تأكد_يساوي(زد_واحد([0]), [1], "صفر")
# apl-source:34
