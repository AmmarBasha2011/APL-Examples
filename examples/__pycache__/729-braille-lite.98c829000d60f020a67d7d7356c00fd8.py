
# apl-source:1
# مثال 729 — برايل مصغر
# apl-source:2
# Braille lite
# apl-source:3
# Demonstrates: نقاط، خريطة حروف، يونيكود
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/729-braille-lite.apl
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
# برايل للاتينية: نقاط إلى أنماط يونيكود
# apl-source:25
# Demonstrates: بتات النقاط الثماني, أساس U+2800, ترميز أحرف
# apl-source:26
# a نقطة واحدة، z خمس نقاط، الفراغ نمط فارغ
# apl-source:27

# apl-source:28
def نقاط_حرف(ح):
  # apl-source:29
  خريطة = {
    # apl-source:30
    "a": [1], "b": [1, 2], "c": [1, 4], "d": [1, 4, 5], "e": [1, 5],
    # apl-source:31
    "f": [1, 2, 4], "g": [1, 2, 4, 5], "h": [1, 2, 5], "i": [2, 4], "j": [2, 4, 5],
    # apl-source:32
    "k": [1, 3], "l": [1, 2, 3], "m": [1, 3, 4], "n": [1, 3, 4, 5], "o": [1, 3, 5],
    # apl-source:33
    "p": [1, 2, 3, 4], "q": [1, 2, 3, 4, 5], "r": [1, 2, 3, 5], "s": [2, 3, 4], "t": [2, 3, 4, 5],
    # apl-source:34
    "u": [1, 3, 6], "v": [1, 2, 3, 6], "w": [2, 4, 5, 6], "x": [1, 3, 4, 6],
    # apl-source:35
    "y": [1, 3, 4, 5, 6], "z": [1, 3, 5, 6]
  # apl-source:36
  }
  # apl-source:37
  return خريطة.get(ح, [])
# apl-source:38

# apl-source:39
def برايل_حرف(ح):
  # apl-source:40
  if ح == " ":
    # apl-source:41
    return chr(10240)
  # apl-source:42
  مجموع = 0
  # apl-source:43
  for ن in نقاط_حرف(ح):
    # apl-source:44
    if ن == 1:
      # apl-source:45
      مجموع = مجموع + 1
    # apl-source:46
    elif ن == 2:
      # apl-source:47
      مجموع = مجموع + 2
    # apl-source:48
    elif ن == 3:
      # apl-source:49
      مجموع = مجموع + 4
    # apl-source:50
    elif ن == 4:
      # apl-source:51
      مجموع = مجموع + 8
    # apl-source:52
    elif ن == 5:
      # apl-source:53
      مجموع = مجموع + 16
    # apl-source:54
    else:
      # apl-source:55
      مجموع = مجموع + 32
  # apl-source:56
  return chr(10240 + مجموع)
# apl-source:57

# apl-source:58
def برايل(نص):
  # apl-source:59
  ناتج = ""
  # apl-source:60
  for ي in range(len(نص)):
    # apl-source:61
    ناتج = ناتج + برايل_حرف(نص[ي])
  # apl-source:62
  return ناتج
# apl-source:63

# apl-source:64
تأكد_يساوي(برايل_حرف("a"), "⠁", "a نقطة أولى")
# apl-source:65
تأكد_يساوي(برايل_حرف("b"), "⠃", "b نقطتان")
# apl-source:66
تأكد_يساوي(برايل_حرف("c"), "⠉", "c نقطتان متباعدتان")
# apl-source:67
تأكد_يساوي(برايل_حرف("z"), "⠵", "z خمس نقاط")
# apl-source:68
تأكد_يساوي(برايل_حرف(" "), "⠀", "فراغ فارغ")
# apl-source:69
تأكد_يساوي(برايل("abc"), "⠁⠃⠉", "كلمة قصيرة")
# apl-source:70
تأكد_يساوي(ord(برايل_حرف("a")), 10241, "الأساس زائد واحد")
# apl-source:71
print(برايل("hello"))
# apl-source:72
