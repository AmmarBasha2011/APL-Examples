
# apl-source:1
# مثال 1329 — فتح القفل
# apl-source:2
# Open the lock minimum turns
# apl-source:3
# Demonstrates: بحث بالعرض
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1329-open-the-lock.apl
# apl-source:6

# apl-source:7
# كل لفة تغير رقماً واحداً بمقدار واحد
# apl-source:8
# نتجنب الأرقام الميتة
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
def افتح(ميتة, هدف):
  # apl-source:19
  if "0000" in ميتة:
    # apl-source:20
    return -1
  # apl-source:21
  مرئي = {"0000": True}
  # apl-source:22
  طابور = [["0000", 0]]
  # apl-source:23
  ع = 0
  # apl-source:24
  while ع < len(طابور):
    # apl-source:25
    ق = طابور[ع][0]
    # apl-source:26
    خ = طابور[ع][1]
    # apl-source:27
    ع = ع + 1
    # apl-source:28
    if ق == هدف:
      # apl-source:29
      return خ
    # apl-source:30
    for م in range(4):
      # apl-source:31
      for د in [1, 9]:
        # apl-source:32
        ر = (int(ق[م]) + د) % 10
        # apl-source:33
        ن = ق[:م] + str(ر) + ق[م + 1:]
        # apl-source:34
        if (ن not in مرئي) and (ن not in ميتة):
          # apl-source:35
          مرئي[ن] = True
          # apl-source:36
          طابور = طابور + [[ن, خ + 1]]
  # apl-source:37
  return -1
# apl-source:38

# apl-source:39
تأكد_يساوي(افتح(["0201","0101","0102","1212","2002"], "0202"), 6, "مثال أول")
# apl-source:40
تأكد_يساوي(افتح(["8888"], "0009"), 1, "لفة واحدة")
# apl-source:41
تأكد_يساوي(افتح(["0000"], "8888"), -1, "بداية ميتة")
# apl-source:42
تأكد_يساوي(افتح([], "0000"), 0, "الهدف بداية")
# apl-source:43
