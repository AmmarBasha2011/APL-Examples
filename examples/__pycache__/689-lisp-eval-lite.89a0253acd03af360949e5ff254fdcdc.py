
# apl-source:1
# مثال 689 — مفسر ليسب مصغر
# apl-source:2
# Lisp evaluator lite
# apl-source:3
# Demonstrates: تجزئة، شجرة، تقييم عودي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/689-lisp-eval-lite.apl
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
# مفسر ليسب مصغر: حساب بالبادئة فقط
# apl-source:25
# Demonstrates: تجزئة رموز, شجرة متداخلة بالعودية, تقييم عودي
# apl-source:26
# يدعم + - * / على الأعداد الصحيحة
# apl-source:27

# apl-source:28
def رموز(نص):
  # apl-source:29
  مبعد = نص.replace("(", " ( ").replace(")", " ) ")
  # apl-source:30
  return مبعد.split()
# apl-source:31

# apl-source:32
def حلل(قائمة, موضع):
  # apl-source:33
  رمز = قائمة[موضع]
  # apl-source:34
  if رمز == "(":
    # apl-source:35
    شجرة = []
    # apl-source:36
    موضع = موضع + 1
    # apl-source:37
    while قائمة[موضع] != ")":
      # apl-source:38
      زوج = حلل(قائمة, موضع)
      # apl-source:39
      شجرة.append(زوج[0])
      # apl-source:40
      موضع = زوج[1]
    # apl-source:41
    return [شجرة, موضع + 1]
  # apl-source:42
  if رمز in ["+", "-", "*", "/"]:
    # apl-source:43
    return [رمز, موضع + 1]
  # apl-source:44
  return [int(رمز), موضع + 1]
# apl-source:45

# apl-source:46
def قيم(عقدة):
  # apl-source:47
  if type(عقدة) == type(0):
    # apl-source:48
    return عقدة
  # apl-source:49
  عملية = عقدة[0]
  # apl-source:50
  أ = قيم(عقدة[1])
  # apl-source:51
  ب = قيم(عقدة[2])
  # apl-source:52
  if عملية == "+":
    # apl-source:53
    return أ + ب
  # apl-source:54
  if عملية == "-":
    # apl-source:55
    return أ - ب
  # apl-source:56
  if عملية == "*":
    # apl-source:57
    return أ * ب
  # apl-source:58
  return أ // ب
# apl-source:59

# apl-source:60
def احسب(نص):
  # apl-source:61
  زوج = حلل(رموز(نص), 0)
  # apl-source:62
  return قيم(زوج[0])
# apl-source:63

# apl-source:64
تأكد_يساوي(احسب("(+ 1 (* 2 3))"), 7, "جمع وضرب")
# apl-source:65
تأكد_يساوي(احسب("(- 10 (/ 8 2))"), 6, "طرح وقسمة")
# apl-source:66
تأكد_يساوي(احسب("(* (+ 1 2) (- 5 3))"), 6, "تداخل عميق")
# apl-source:67
تأكد_يساوي(احسب("42"), 42, "عدد مفرد")
# apl-source:68
تأكد_يساوي(احسب("(+ (+ (+ 1 1) 1) 1)"), 4, "تداخل أيسر")
# apl-source:69
print("الناتج:", احسب("(+ 1 (* 2 3))"))
# apl-source:70
