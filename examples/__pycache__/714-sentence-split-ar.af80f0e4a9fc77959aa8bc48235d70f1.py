
# apl-source:1
# مثال 714 — تقسيم الجمل العربية
# apl-source:2
# Arabic sentence splitter
# apl-source:3
# Demonstrates: نهايات جمل، استثناءات، تقليم
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/714-sentence-split-ar.apl
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
# تقسيم نص عربي إلى جمل
# apl-source:25
# Demonstrates: نهايات . ! ؟ ?, تقليم فراغات, تجاهل الرموز المتتابعة
# apl-source:26
# النقطة داخل رقم عشري لا تقطع
# apl-source:27

# apl-source:28
def نهاية(ح):
  # apl-source:29
  return ح == "." or ح == "!" or ح == "؟" or ح == "?"
# apl-source:30

# apl-source:31
def قسم(نص):
  # apl-source:32
  جمل = []
  # apl-source:33
  جارية = ""
  # apl-source:34
  for ي in range(len(نص)):
    # apl-source:35
    ح = نص[ي]
    # apl-source:36
    جارية = جارية + ح
    # apl-source:37
    if نهاية(ح):
      # apl-source:38
      تالية_رقم = False
      # apl-source:39
      if ح == "." and ي + 1 < len(نص):
        # apl-source:40
        if نص[ي + 1] in "0123456789" and ي > 0 and نص[ي - 1] in "0123456789":
          # apl-source:41
          تالية_رقم = True
      # apl-source:42
      if تالية_رقم == False:
        # apl-source:43
        مقلمة = جارية.strip()
        # apl-source:44
        if len(مقلمة) > 1:
          # apl-source:45
          جمل.append(مقلمة)
        # apl-source:46
        جارية = ""
  # apl-source:47
  بقية = جارية.strip()
  # apl-source:48
  if len(بقية) > 0:
    # apl-source:49
    جمل.append(بقية)
  # apl-source:50
  return جمل
# apl-source:51

# apl-source:52
نص1 = "ذهب الولد إلى المدرسة. كان الجو جميلا! هل وصل متأخرا؟ لا، بل مبكرا."
# apl-source:53
ج1 = قسم(نص1)
# apl-source:54
تأكد_يساوي(len(ج1), 4, "أربع جمل")
# apl-source:55
تأكد_يساوي(ج1[0], "ذهب الولد إلى المدرسة.", "الجملة الأولى")
# apl-source:56
تأكد_يساوي(ج1[2], "هل وصل متأخرا؟", "علامة الاستفهام العربية")
# apl-source:57
ج2 = قسم("النسخة 3.14 جديدة. صدرت اليوم.")
# apl-source:58
تأكد_يساوي(len(ج2), 2, "النقطة العشرية لا تقطع")
# apl-source:59
تأكد_يساوي(ج2[0], "النسخة 3.14 جديدة.", "الرقم سليم")
# apl-source:60
ج3 = قسم("جملة بلا نهاية")
# apl-source:61
تأكد_يساوي(ج3, ["جملة بلا نهاية"], "بقية بلا رمز")
# apl-source:62
ج4 = قسم("أولى!  ثانية.")
# apl-source:63
تأكد_يساوي(len(ج4), 2, "فراغ مزدوج يقلم")
# apl-source:64
print(ج1[1])
# apl-source:65
