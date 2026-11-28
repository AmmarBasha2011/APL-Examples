
# apl-source:1
# مثال 708 — إكسبكتيماكس
# apl-source:2
# Expectimax
# apl-source:3
# Demonstrates: عقد حظ، عقد قصوى، متوسط
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/708-expectimax-lite.apl
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
# إكسبكتيماكس: قرارات تحت عدم اليقين
# apl-source:25
# Demonstrates: عقد قصوى, عقد حظ بمتوسط موزون, شجرة قرار
# apl-source:26
# لعبة: ارم عملة؛ صورة تكسب 10 ثم قرار، كتابة تكسب 4 فورا
# apl-source:27

# apl-source:28
def قيمة(عقدة):
  # apl-source:29
  if عقدة[0] == "ورقة":
    # apl-source:30
    return عقدة[1] * 1.0
  # apl-source:31
  if عقدة[0] == "أقصى":
    # apl-source:32
    أفضل = -1000000.0
    # apl-source:33
    for فرع in عقدة[1]:
      # apl-source:34
      ق = قيمة(فرع)
      # apl-source:35
      if ق > أفضل:
        # apl-source:36
        أفضل = ق
    # apl-source:37
    return أفضل
  # apl-source:38
  مجموع = 0.0
  # apl-source:39
  عدد = len(عقدة[1])
  # apl-source:40
  for فرع in عقدة[1]:
    # apl-source:41
    مجموع = مجموع + قيمة(فرع)
  # apl-source:42
  return مجموع / عدد
# apl-source:43

# apl-source:44
# حظ: [ورقة 10, ورقة 4]
# apl-source:45
حظ = ["حظ", [["ورقة", 10], ["ورقة", 4]]]
# apl-source:46
تأكد_يساوي(قيمة(حظ), 7.0, "متوسط الحظ 7")
# apl-source:47
# أقصى: خذ 8 مؤكدة أو جرب الحظ
# apl-source:48
قرار = ["أقصى", [["ورقة", 8], حظ]]
# apl-source:49
تأكد_يساوي(قيمة(قرار), 8.0, "الثمانية المؤكدة أفضل")
# apl-source:50
قرار2 = ["أقصى", [["ورقة", 5], حظ]]
# apl-source:51
تأكد_يساوي(قيمة(قرار2), 7.0, "الحظ أفضل من خمسة")
# apl-source:52
# شجرة أعمق: حظ ثم قرار
# apl-source:53
عميق = ["حظ", [["أقصى", [["ورقة", 20], ["ورقة", 2]]], ["ورقة", 6]]]
# apl-source:54
تأكد_يساوي(قيمة(عميق), 13.0, "متوسط (20 و 6) يساوي 13")
# apl-source:55
تأكد_يساوي(قيمة(["أقصى", [عميق, ["ورقة", 15]]]), 15.0, "15 تتفوق على 13")
# apl-source:56
print("قيمة القرار:", قيمة(قرار2))
# apl-source:57
