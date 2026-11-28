
# apl-source:1
# مثال 1302 — منتصف القائمة
# apl-source:2
# Middle of linked list
# apl-source:3
# Demonstrates: مؤشران
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1302-linked-list-middle-array.apl
# apl-source:6

# apl-source:7
# السريع يتحرك خطوتين والبطيء خطوة
# apl-source:8
# فيصل البطيء للمنتصف عند نهاية السريع
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
def منتصف(قيم):
  # apl-source:19
  بطيء = 0
  # apl-source:20
  سريع = 0
  # apl-source:21
  while (سريع < len(قيم)) and (سريع + 1 < len(قيم)):
    # apl-source:22
    بطيء = بطيء + 1
    # apl-source:23
    سريع = سريع + 2
  # apl-source:24
  return قيم[بطيء]
# apl-source:25

# apl-source:26
تأكد_يساوي(منتصف([1,2,3,4,5]), 3, "فردي")
# apl-source:27
تأكد_يساوي(منتصف([1,2,3,4,5,6]), 4, "زوجي")
# apl-source:28
تأكد_يساوي(منتصف([7]), 7, "واحد")
# apl-source:29
