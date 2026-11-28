
# apl-source:1
# مثال 631 — آلة بايت-كود افتراضية
# apl-source:2
# Bytecode VM
# apl-source:3
# Demonstrates: آلة افتراضية، مكدس، تعليمات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/631-bytecode-vm.apl
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
# آلة افتراضية كومة: مفسر بايت-كود مصغر
# apl-source:25
# Demonstrates: حلقة إرسال, مكدس operands, تعليمات
# apl-source:26
# هكذا تنفذ الآلات الافتراضية البرامج المترجمة
# apl-source:27

# apl-source:28
def نفذ(برنامج):
  # apl-source:29
  مكدس = []
  # apl-source:30
  مؤشر = 0
  # apl-source:31
  مطبوع = []
  # apl-source:32
  while مؤشر < len(برنامج):
    # apl-source:33
    تعليمة = برنامج[مؤشر]
    # apl-source:34
    مؤشر = مؤشر + 1
    # apl-source:35
    if تعليمة[0] == "ادفع":
      # apl-source:36
      مكدس.append(تعليمة[1])
    # apl-source:37
    if تعليمة[0] == "اجمع":
      # apl-source:38
      ب = مكدس.pop()
      # apl-source:39
      أ = مكدس.pop()
      # apl-source:40
      مكدس.append(أ + ب)
    # apl-source:41
    if تعليمة[0] == "اضرب":
      # apl-source:42
      ب = مكدس.pop()
      # apl-source:43
      أ = مكدس.pop()
      # apl-source:44
      مكدس.append(أ * ب)
    # apl-source:45
    if تعليمة[0] == "اطرح":
      # apl-source:46
      ب = مكدس.pop()
      # apl-source:47
      أ = مكدس.pop()
      # apl-source:48
      مكدس.append(أ - ب)
    # apl-source:49
    if تعليمة[0] == "اطبع":
      # apl-source:50
      مطبوع.append(مكدس.pop())
  # apl-source:51
  return مطبوع
# apl-source:52

# apl-source:53
برنامج = [["ادفع", 2], ["ادفع", 3], ["اجمع"], ["ادفع", 4], ["اضرب"], ["اطبع"], ["ادفع", 10], ["ادفع", 3], ["اطرح"], ["اطبع"]]
# apl-source:54
ناتج = نفذ(برنامج)
# apl-source:55
print("المطبوع:", ناتج)
# apl-source:56
تأكد_يساوي(ناتج, [20, 7], "(2+3)*4 ثم 10-3")
# apl-source:57
تأكد_يساوي(نفذ([["ادفع", 6], ["ادفع", 7], ["اضرب"], ["اطبع"]]), [42], "ضرب وحيد")
# apl-source:58
