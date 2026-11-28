
# apl-source:1
# مثال 725 — فك UTF-8 يدوي
# apl-source:2
# Manual UTF-8 decode
# apl-source:3
# Demonstrates: بايتات متابعة، نقاط كود، أقنعة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/725-utf8-decode-manual.apl
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
# فك ترميز UTF-8 يدويا من البايتات
# apl-source:25
# Demonstrates: بايتات قائدة وتابعة, أقنعة بتية, أربعة أطوال
# apl-source:26
# أ = D8 A3، يورو = E2 82 AC، وجه ضاحك = F0 9F 98 80
# apl-source:27

# apl-source:28
def فك_utf8(بايتات):
  # apl-source:29
  نقاط = []
  # apl-source:30
  ي = 0
  # apl-source:31
  while ي < len(بايتات):
    # apl-source:32
    ب = بايتات[ي]
    # apl-source:33
    if ب < 128:
      # apl-source:34
      نقاط.append(ب)
      # apl-source:35
      ي = ي + 1
    # apl-source:36
    elif ب < 224:
      # apl-source:37
      نقاط.append((ب % 32) * 64 + بايتات[ي + 1] % 64)
      # apl-source:38
      ي = ي + 2
    # apl-source:39
    elif ب < 240:
      # apl-source:40
      نقاط.append((ب % 16) * 4096 + (بايتات[ي + 1] % 64) * 64 + بايتات[ي + 2] % 64)
      # apl-source:41
      ي = ي + 3
    # apl-source:42
    else:
      # apl-source:43
      نقاط.append((ب % 8) * 262144 + (بايتات[ي + 1] % 64) * 4096 + (بايتات[ي + 2] % 64) * 64 + بايتات[ي + 3] % 64)
      # apl-source:44
      ي = ي + 4
  # apl-source:45
  return نقاط
# apl-source:46

# apl-source:47
def إلى_نص(نقاط):
  # apl-source:48
  ناتج = ""
  # apl-source:49
  for ن in نقاط:
    # apl-source:50
    ناتج = ناتج + chr(ن)
  # apl-source:51
  return ناتج
# apl-source:52

# apl-source:53
# "أA€😀" كبايتات
# apl-source:54
بايتات = [216, 163, 65, 226, 130, 172, 240, 159, 152, 128]
# apl-source:55
نقاط = فك_utf8(بايتات)
# apl-source:56
تأكد_يساوي(نقاط[0], 1571, "الألف العربية U+0623")
# apl-source:57
تأكد_يساوي(نقاط[1], 65, "A آسكي")
# apl-source:58
تأكد_يساوي(نقاط[2], 8364, "علامة اليورو U+20AC")
# apl-source:59
تأكد_يساوي(نقاط[3], 128512, "الوجه الضاحك U+1F600")
# apl-source:60
تأكد_يساوي(len(نقاط), 4, "أربعة محارف")
# apl-source:61
تأكد_يساوي(إلى_نص(نقاط), "أA€😀", "النص الكامل")
# apl-source:62
تأكد_يساوي(فك_utf8([104, 105]), [104, 105], "آسكي خام")
# apl-source:63
print(إلى_نص(نقاط))
# apl-source:64
