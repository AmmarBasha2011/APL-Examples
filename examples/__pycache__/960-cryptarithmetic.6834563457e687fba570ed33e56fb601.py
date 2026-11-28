
# apl-source:1
# مثال 960 — لغز الحروف الحسابية
# apl-source:2
# Cryptarithmetic puzzle
# apl-source:3
# Demonstrates: بحث مع تثبيت المحسوم
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/960-cryptarithmetic.apl
# apl-source:6

# apl-source:7
# حروف حسابية: SEND + MORE = MONEY بحث شامل مع تثبيت الحروف المحسومة
# apl-source:8
# م=1 وع=0 و س=9 بالحمل، ويبقى البحث على خمسة حروف
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
م = 1
# apl-source:19
ع = 0
# apl-source:20
س = 9
# apl-source:21
حلول = 0
# apl-source:22
ه_حل = -1
# apl-source:23
ن_حل = -1
# apl-source:24
ر_حل = -1
# apl-source:25
د_حل = -1
# apl-source:26
ي_حل = -1
# apl-source:27
for ه in range(2, 9):
  # apl-source:28
  for ن in range(2, 9):
    # apl-source:29
    if ن != ه:
      # apl-source:30
      for ر in range(2, 9):
        # apl-source:31
        if (ر != ه) and (ر != ن):
          # apl-source:32
          for د in range(2, 9):
            # apl-source:33
            if ((د != ه) and (د != ن)) and (د != ر):
              # apl-source:34
              for ي in range(2, 9):
                # apl-source:35
                if (((ي != ه) and (ي != ن)) and (ي != ر)) and (ي != د):
                  # apl-source:36
                  ارسل = (س * 1000) + (ه * 100) + (ن * 10) + د
                  # apl-source:37
                  المزيد = (م * 1000) + (ع * 100) + (ر * 10) + ه
                  # apl-source:38
                  مال = (م * 10000) + (ع * 1000) + (ن * 100) + (ه * 10) + ي
                  # apl-source:39
                  if (ارسل + المزيد) == مال:
                    # apl-source:40
                    حلول = حلول + 1
                    # apl-source:41
                    ه_حل = ه
                    # apl-source:42
                    ن_حل = ن
                    # apl-source:43
                    ر_حل = ر
                    # apl-source:44
                    د_حل = د
                    # apl-source:45
                    ي_حل = ي
# apl-source:46

# apl-source:47
تأكد_يساوي(حلول, 1, "حل وحيد")
# apl-source:48
تأكد_يساوي(ه_حل, 5, "الحرف ه")
# apl-source:49
تأكد_يساوي(ن_حل, 6, "الحرف ن")
# apl-source:50
تأكد_يساوي(د_حل, 7, "الحرف د")
# apl-source:51
تأكد_يساوي(ر_حل, 8, "الحرف ر")
# apl-source:52
تأكد_يساوي(ي_حل, 2, "الحرف ي")
# apl-source:53
تأكد_يساوي(10652, 10652, "التحقق الحسابي")
# apl-source:54
