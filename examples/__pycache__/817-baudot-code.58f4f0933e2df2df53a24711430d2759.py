
# apl-source:1
# مثال 817 — شفرة بودو
# apl-source:2
# Baudot ITA2
# apl-source:3
# Demonstrates: خمسة بتات، سجل حروف وأرقام
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/817-baudot-code.apl
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
# شفرة بودو-موراي ITA2 للتليكس: خمسة بتات مع سجل حروف وأرقام
# apl-source:25
# Demonstrates: جدولان بسجلين, رموز تحول 27 و31, ترميز ثنائي قديم
# apl-source:26

# apl-source:27
حروف = "#E\nA SIU\rDRJNFCKTZLWHYPQOBG*MXV="
# apl-source:28
أرقام = "#3\n- \a\r$4',!:(5\")2#6019?+*/.="
# apl-source:29
تحول_أرقام = 27
# apl-source:30
تحول_حروف = 31
# apl-source:31

# apl-source:32
def موقع_في(ح, جدول):
  # apl-source:33
  for ي in range(len(جدول)):
    # apl-source:34
    if جدول[ي] == ح:
      # apl-source:35
      return ي
  # apl-source:36
  return -1
# apl-source:37

# apl-source:38
def رقمية(ح):
  # apl-source:39
  return (موقع_في(ح, حروف) == -1) == False
# apl-source:40

# apl-source:41
def شفر_بودو(نص):
  # apl-source:42
  رموز = []
  # apl-source:43
  سجل = 0
  # apl-source:44
  for ح in نص:
    # apl-source:45
    if رقمية(ح) == False:
      # apl-source:46
      if سجل != 2:
        # apl-source:47
        رموز.append(تحول_أرقام)
        # apl-source:48
        سجل = 2
      # apl-source:49
      رموز.append(موقع_في(ح, أرقام))
    # apl-source:50
    else:
      # apl-source:51
      if سجل != 1:
        # apl-source:52
        رموز.append(تحول_حروف)
        # apl-source:53
        سجل = 1
      # apl-source:54
      رموز.append(موقع_في(ح, حروف))
  # apl-source:55
  return رموز
# apl-source:56

# apl-source:57
تأكد_يساوي(موقع_في("H", حروف), 20, "موقع H")
# apl-source:58
تأكد_يساوي(شفر_بودو("HELLO"), [31, 20, 1, 18, 18, 24], "كلمة حروف")
# apl-source:59
تأكد_يساوي(شفر_بودو("A1"), [31, 3, 27, 21], "حرف ثم رقم")
# apl-source:60
تأكد_يساوي(شفر_بودو("AB"), [31, 3, 25], "لا تحول زائد")
# apl-source:61
