
# apl-source:1
# مثال 598 — مسار أويلر
# apl-source:2
# Eulerian path
# apl-source:3
# Demonstrates: أويلر، درجات فردية، هيرهولتزر
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/598-euler-path.apl
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
# مسار أويلر: زيارة كل حافة مرة واحدة
# apl-source:25
# Demonstrates: شرط الدرجات الفردية, خوارزمية هيرهولتزر, إعادة بناء المسار
# apl-source:26
# الرسم: مسار شجري، كل حافة فيه جسر
# apl-source:27

# apl-source:28
جوار = {0: [1, 3, 2], 1: [0, 2], 2: [1, 3, 0], 3: [2, 0]}
# apl-source:29
عدد_الحواف = 5
# apl-source:30

# apl-source:31
فردية = []
# apl-source:32
for عقدة in جوار.keys():
  # apl-source:33
  if len(جوار[عقدة]) % 2 == 1:
    # apl-source:34
    فردية.append(عقدة)
# apl-source:35
فردية.sort()
# apl-source:36
print("عقد فردية الدرجة:", فردية)
# apl-source:37
تأكد_يساوي(فردية, [0, 2], "شرط وجود المسار")
# apl-source:38

# apl-source:39
# هيرهولتزر
# apl-source:40
نسخة = {}
# apl-source:41
for عقدة in جوار.keys():
  # apl-source:42
  نسخة[عقدة] = جوار[عقدة].copy()
# apl-source:43
مكدس = [فردية[0]]
# apl-source:44
مسار = []
# apl-source:45
while len(مكدس) > 0:
  # apl-source:46
  قمة = مكدس[len(مكدس) - 1]
  # apl-source:47
  if len(نسخة[قمة]) > 0:
    # apl-source:48
    تال = نسخة[قمة].pop()
    # apl-source:49
    نسخة[تال].remove(قمة)
    # apl-source:50
    مكدس.append(تال)
  # apl-source:51
  else:
    # apl-source:52
    مسار.append(مكدس.pop())
# apl-source:53
مسار.reverse()
# apl-source:54
print("مسار أويلر:", مسار)
# apl-source:55
تأكد_يساوي(len(مسار), عدد_الحواف + 1, "كل الحواف مستخدمة")
# apl-source:56
تأكد_يساوي(مسار[0], 0, "يبدأ من عقدة فردية")
# apl-source:57
تأكد_يساوي(مسار[len(مسار) - 1], 2, "ينتهي عند العقدة الفردية الأخرى")
# apl-source:58
