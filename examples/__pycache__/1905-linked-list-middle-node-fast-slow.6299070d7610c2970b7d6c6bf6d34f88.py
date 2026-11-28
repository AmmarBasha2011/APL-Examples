
# apl-source:1
# مثال 1905 — العقدة الوسطى بمؤشرين
# apl-source:2
# Middle node with two pointers
# apl-source:3
# Demonstrates: هياكل بيانات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1905-linked-list-middle-node-fast-slow.apl
# apl-source:6

# apl-source:7
# السريع يتحرك خطوتين والبطيء خطوة
# apl-source:8
# عند نهاية السريع يكون البطيء في المنتصف
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
def وسط(تالي, رأس):
  # apl-source:19
  بطيء = رأس
  # apl-source:20
  سريع = رأس
  # apl-source:21
  while سريع != -1 and تالي[سريع] != -1:
    # apl-source:22
    بطيء = تالي[بطيء]
    # apl-source:23
    سريع = تالي[تالي[سريع]]
  # apl-source:24
  return بطيء
# apl-source:25

# apl-source:26
تأكد_يساوي(وسط([1, 2, 3, 4, -1], 0), 2, "خمس عقد")
# apl-source:27
تأكد_يساوي(وسط([1, 2, 3, -1], 0), 2, "أربع عقد")
# apl-source:28
تأكد_يساوي(وسط([-1], 0), 0, "عقدة واحدة")
# apl-source:29
