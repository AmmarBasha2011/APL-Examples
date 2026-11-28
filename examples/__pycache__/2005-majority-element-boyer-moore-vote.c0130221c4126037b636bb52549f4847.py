
# apl-source:1
# مثال 2005 — العنصر الأغلبي بتصويت بوير مور
# apl-source:2
# Boyer-Moore majority vote
# apl-source:3
# Demonstrates: خوارزميات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2005-majority-element-boyer-moore-vote.apl
# apl-source:6

# apl-source:7
# # نغير المرشح عندما يصبح العداد صفرا
# apl-source:8
# # العنصر الأغلبي يبقى في النهاية
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
def اغلبي(ق):
  # apl-source:19
  مرشح = ق[0]
  # apl-source:20
  عداد = 0
  # apl-source:21
  for ع in ق:
    # apl-source:22
    if عداد == 0:
      # apl-source:23
      مرشح = ع
    # apl-source:24
    if ع == مرشح:
      # apl-source:25
      عداد = عداد + 1
    # apl-source:26
    else:
      # apl-source:27
      عداد = عداد - 1
  # apl-source:28
  return مرشح
# apl-source:29

# apl-source:30
تأكد_يساوي(اغلبي([2, 2, 1, 1, 1, 2, 2]), 2, "سبعة")
# apl-source:31
تأكد_يساوي(اغلبي([3, 2, 3]), 3, "ثلاثة")
# apl-source:32
تأكد_يساوي(اغلبي([5]), 5, "واحد")
# apl-source:33
