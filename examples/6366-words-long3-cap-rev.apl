# مثال 6366 — القائمة معكوسة: الكلمات الأطول من 3 حروف ثم (أول حرف كبير)
# rev of cap over words long3
# Demonstrates: معالجة النصوص
#
# Run:  python apl.py examples/6366-words-long3-cap-rev.apl

# نقسم النص إلى كلمات
# نصفّي ثم نحوّل كل كلمة
# ونرجع: القائمة معكوسة

دالة تأكد_يساوي(فعلي, متوقع, اسم):
  لو فعلي != متوقع:
    اطبع "فشل:", اسم
    اطبع "  متوقع:", متوقع
    اطبع "  فعلي:", فعلي
    قياسي_نظام_اخرج(1)
  اطبع "ناجح:", اسم

دالة ف(ن):
  ر = []
  لكل ك في ن.split(" "):
    لو len(ك) > 3:
      ر = ر + [ك[0].upper() + ك[1:]]
  ارجع ر[::-1]

تأكد_يساوي(ف("the cat sat on the mat"), [], "حالة 1")
تأكد_يساوي(ف("apl makes code simple and fun"), ["Simple", "Code", "Makes"], "حالة 2")
تأكد_يساوي(ف("one two three four five six"), ["Five", "Four", "Three"], "حالة 3")
تأكد_يساوي(ف("a bb ccc dddd eeeee"), ["Eeeee", "Dddd"], "حالة 4")
تأكد_يساوي(ف("to be or not to be that is the question"), ["Question", "That"], "حالة 5")
تأكد_يساوي(ف("data data data code code apl"), ["Code", "Code", "Data", "Data", "Data"], "حالة 6")
تأكد_يساوي(ف("learning to program is learning to think"), ["Think", "Learning", "Program", "Learning"], "حالة 7")
تأكد_يساوي(ف("hello"), ["Hello"], "حالة 8")
