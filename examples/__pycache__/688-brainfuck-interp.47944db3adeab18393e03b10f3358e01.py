
# apl-source:1
# مثال 688 — مفسر براين فك
# apl-source:2
# Brainfuck interpreter
# apl-source:3
# Demonstrates: شريط ذاكرة، أقواس، مكدس
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/688-brainfuck-interp.apl
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
# مفسر براين فك المصغر (بدون إدخال)
# apl-source:25
# Demonstrates: شريط ذاكرة, مطابقة الأقواس بمكدس, حلقات []
# apl-source:26
# البرنامج: 6*11-1 = 65 يطبع A ثم +. يطبع B
# apl-source:27

# apl-source:28
def طابق_أقواس(برنامج):
  # apl-source:29
  أزواج = {}
  # apl-source:30
  مكدس = []
  # apl-source:31
  for ي in range(len(برنامج)):
    # apl-source:32
    if برنامج[ي] == "[":
      # apl-source:33
      مكدس.append(ي)
    # apl-source:34
    elif برنامج[ي] == "]":
      # apl-source:35
      فتح = مكدس.pop()
      # apl-source:36
      أزواج[فتح] = ي
      # apl-source:37
      أزواج[ي] = فتح
  # apl-source:38
  return أزواج
# apl-source:39

# apl-source:40
def نفذ(برنامج):
  # apl-source:41
  أزواج = طابق_أقواس(برنامج)
  # apl-source:42
  شريط = [0] * 64
  # apl-source:43
  مؤشر = 0
  # apl-source:44
  عداد = 0
  # apl-source:45
  ناتج = ""
  # apl-source:46
  while عداد < len(برنامج):
    # apl-source:47
    أمر = برنامج[عداد]
    # apl-source:48
    if أمر == ">":
      # apl-source:49
      مؤشر = مؤشر + 1
    # apl-source:50
    elif أمر == "<":
      # apl-source:51
      مؤشر = مؤشر - 1
    # apl-source:52
    elif أمر == "+":
      # apl-source:53
      شريط[مؤشر] = (شريط[مؤشر] + 1) % 256
    # apl-source:54
    elif أمر == "-":
      # apl-source:55
      شريط[مؤشر] = (شريط[مؤشر] + 255) % 256
    # apl-source:56
    elif أمر == ".":
      # apl-source:57
      ناتج = ناتج + chr(شريط[مؤشر])
    # apl-source:58
    elif أمر == "[":
      # apl-source:59
      if شريط[مؤشر] == 0:
        # apl-source:60
        عداد = أزواج[عداد]
    # apl-source:61
    elif أمر == "]":
      # apl-source:62
      if شريط[مؤشر] != 0:
        # apl-source:63
        عداد = أزواج[عداد]
    # apl-source:64
    عداد = عداد + 1
  # apl-source:65
  return ناتج
# apl-source:66

# apl-source:67
ناتج = نفذ("++++++[>+++++++++++<-]>-.+.")
# apl-source:68
تأكد_يساوي(ناتج, "AB", "البرنامج يطبع AB")
# apl-source:69
ناتج2 = نفذ("+++[>+++[>++<-]<-]>>.")
# apl-source:70
تأكد_يساوي(ناتج2, chr(18), "حلقتان متداخلتان 3*3*2=18")
# apl-source:71
ناتج3 = نفذ("++++++++++.")
# apl-source:72
تأكد_يساوي(ناتج3, chr(10), "سطر جديد من عشرة")
# apl-source:73
print("الناتج:", ناتج)
# apl-source:74
