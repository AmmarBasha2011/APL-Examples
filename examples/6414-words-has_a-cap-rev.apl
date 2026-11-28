# مثال 6414 — القائمة معكوسة: الكلمات التي فيها a ثم (أول حرف كبير)
# rev of cap over words has_a
# Demonstrates: معالجة النصوص
#
# Run:  python apl.py examples/6414-words-has_a-cap-rev.apl

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
    لو "a" in ك:
      ر = ر + [ك[0].upper() + ك[1:]]
  ارجع ر[::-1]

تأكد_يساوي(ف("the cat sat on the mat"), ["Mat", "Sat", "Cat"], "حالة 1")
تأكد_يساوي(ف("apl makes code simple and fun"), ["And", "Makes", "Apl"], "حالة 2")
تأكد_يساوي(ف("one two three four five six"), [], "حالة 3")
تأكد_يساوي(ف("a bb ccc dddd eeeee"), ["A"], "حالة 4")
تأكد_يساوي(ف("to be or not to be that is the question"), ["That"], "حالة 5")
تأكد_يساوي(ف("data data data code code apl"), ["Apl", "Data", "Data", "Data"], "حالة 6")
تأكد_يساوي(ف("learning to program is learning to think"), ["Learning", "Program", "Learning"], "حالة 7")
تأكد_يساوي(ف("hello"), [], "حالة 8")
