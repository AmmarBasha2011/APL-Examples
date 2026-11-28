# مثال 6363 — قائمة: الكلمات الأطول من 3 حروف ثم (أول حرف كبير)
# list of cap over words long3
# Demonstrates: معالجة النصوص
#
# Run:  python apl.py examples/6363-words-long3-cap-list.apl

# نقسم النص إلى كلمات
# نصفّي ثم نحوّل كل كلمة
# ونرجع: قائمة

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
  ارجع ر

تأكد_يساوي(ف("the cat sat on the mat"), [], "حالة 1")
تأكد_يساوي(ف("apl makes code simple and fun"), ["Makes", "Code", "Simple"], "حالة 2")
تأكد_يساوي(ف("one two three four five six"), ["Three", "Four", "Five"], "حالة 3")
تأكد_يساوي(ف("a bb ccc dddd eeeee"), ["Dddd", "Eeeee"], "حالة 4")
تأكد_يساوي(ف("to be or not to be that is the question"), ["That", "Question"], "حالة 5")
تأكد_يساوي(ف("data data data code code apl"), ["Data", "Data", "Data", "Code", "Code"], "حالة 6")
تأكد_يساوي(ف("learning to program is learning to think"), ["Learning", "Program", "Learning", "Think"], "حالة 7")
تأكد_يساوي(ف("hello"), ["Hello"], "حالة 8")
