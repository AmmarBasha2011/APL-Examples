
# apl-source:1
# مثال 1371 — هل أفوز
# apl-source:2
# Can I win picking numbers
# apl-source:3
# Demonstrates: تراجع
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1371-can-i-win.apl
# apl-source:6

# apl-source:7
# اللاعب الذي يصل للمجموع أولاً يفوز
# apl-source:8
# نخزن الحالات بحسب الأرقام المستخدمة
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
def افوز(اقصى, هدف):
  # apl-source:19
  if هدف <= 0:
    # apl-source:20
    return True
  # apl-source:21
  if اقصى * (اقصى + 1) // 2 < هدف:
    # apl-source:22
    return False
  # apl-source:23
  مستخدم = [0] * (اقصى + 1)
  # apl-source:24
  ذاكرة = {}
  # apl-source:25
  def فوز(باقي):
    # apl-source:26
    مفتاح = str(مستخدم)
    # apl-source:27
    if مفتاح in ذاكرة:
      # apl-source:28
      return ذاكرة[مفتاح]
    # apl-source:29
    for ر in range(1, اقصى + 1):
      # apl-source:30
      if مستخدم[ر] == 0:
        # apl-source:31
        if ر >= باقي:
          # apl-source:32
          ذاكرة[مفتاح] = True
          # apl-source:33
          return True
        # apl-source:34
        مستخدم[ر] = 1
        # apl-source:35
        نتيجة = فوز(باقي - ر)
        # apl-source:36
        مستخدم[ر] = 0
        # apl-source:37
        if نتيجة == False:
          # apl-source:38
          ذاكرة[مفتاح] = True
          # apl-source:39
          return True
    # apl-source:40
    ذاكرة[مفتاح] = False
    # apl-source:41
    return False
  # apl-source:42
  return فوز(هدف)
# apl-source:43

# apl-source:44
تأكد_يساوي(افوز(10, 11), False, "يخسر")
# apl-source:45
تأكد_يساوي(افوز(10, 0), True, "هدف صفر")
# apl-source:46
تأكد_يساوي(افوز(10, 40), False, "هدف كبير")
# apl-source:47
