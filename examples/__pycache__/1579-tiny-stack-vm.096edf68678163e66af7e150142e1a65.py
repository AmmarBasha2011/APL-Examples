
# apl-source:1
# مثال 1579 — آلة مكدس صغيرة
# apl-source:2
# Tiny stack virtual machine
# apl-source:3
# Demonstrates: محاكاة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1579-tiny-stack-vm.apl
# apl-source:6

# apl-source:7
# كل تعليمة إما دفع رقم أو عملية
# apl-source:8
# العملية تسحب رقمين وتدفع النتيجة
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
def نفّذ(برنامج):
  # apl-source:19
  مكدس = []
  # apl-source:20
  for ت in برنامج:
    # apl-source:21
    أجزاء = ت.split(" ")
    # apl-source:22
    if أجزاء[0] == "push":
      # apl-source:23
      مكدس.append(int(أجزاء[1]))
    # apl-source:24
    else:
      # apl-source:25
      ب = مكدس.pop()
      # apl-source:26
      أ = مكدس.pop()
      # apl-source:27
      if أجزاء[0] == "add":
        # apl-source:28
        مكدس.append(أ + ب)
      # apl-source:29
      elif أجزاء[0] == "mul":
        # apl-source:30
        مكدس.append(أ * ب)
      # apl-source:31
      elif أجزاء[0] == "sub":
        # apl-source:32
        مكدس.append(أ - ب)
  # apl-source:33
  return مكدس[len(مكدس) - 1]
# apl-source:34

# apl-source:35
تأكد_يساوي(نفّذ(["push 2", "push 3", "add"]), 5, "جمع")
# apl-source:36
تأكد_يساوي(نفّذ(["push 2", "push 3", "push 4", "mul", "add"]), 14, "ضرب وجمع")
# apl-source:37
تأكد_يساوي(نفّذ(["push 10", "push 4", "sub"]), 6, "طرح")
# apl-source:38
