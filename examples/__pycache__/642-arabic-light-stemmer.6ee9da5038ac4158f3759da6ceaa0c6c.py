
# apl-source:1
# مثال 642 — تجذيع عربي خفيف
# apl-source:2
# Arabic light stemming
# apl-source:3
# Demonstrates: تجذيع، سوابق، لواحق
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/642-arabic-light-stemmer.apl
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
# تجذيع عربي خفيف: إزالة السوابق واللواحق الشائعة
# apl-source:25
# Demonstrates: قواعد قص أطول-أولا, بقاء الجذر, حد أدنى للطول
# apl-source:26
# تبسيط تعليمي؛ التجذيع الحقيقي يحتاج قواعد الصرف
# apl-source:27

# apl-source:28
سوابق = ["وال", "فال", "بال", "كال", "لل", "ال", "و", "ف", "ب", "ك", "ل", "س", "ي", "ت", "ن", "أ"]
# apl-source:29
لواحق = ["كما", "هما", "ات", "ون", "ين", "ان", "كم", "نا", "ها", "هم", "هن", "ة", "ه", "ي", "ك"]
# apl-source:30

# apl-source:31
def جذع(كلمة):
  # apl-source:32
  ناتج = كلمة
  # apl-source:33
  قص_سابق = False
  # apl-source:34
  for س in سوابق:
    # apl-source:35
    if قص_سابق == False and ناتج.startswith(س) and len(ناتج) - len(س) >= 3:
      # apl-source:36
      ناتج = ناتج[len(س):]
      # apl-source:37
      قص_سابق = True
  # apl-source:38
  قص_لاحق = False
  # apl-source:39
  for ل in لواحق:
    # apl-source:40
    if قص_لاحق == False and ناتج.endswith(ل) and len(ناتج) - len(ل) >= 3:
      # apl-source:41
      ناتج = ناتج[:len(ناتج) - len(ل)]
      # apl-source:42
      قص_لاحق = True
  # apl-source:43
  return ناتج
# apl-source:44

# apl-source:45
تأكد_يساوي(جذع("الكتاب"), "كتاب", "أل التعريف")
# apl-source:46
تأكد_يساوي(جذع("والمكتبات"), "مكتب", "سوابق ولاحقة")
# apl-source:47
تأكد_يساوي(جذع("مدرسة"), "مدرس", "تاء مربوطة")
# apl-source:48
تأكد_يساوي(جذع("يلعبون"), "لعب", "سابقة ولاحقة")
# apl-source:49
print("جذع والمكتبات:", جذع("والمكتبات"))
# apl-source:50
