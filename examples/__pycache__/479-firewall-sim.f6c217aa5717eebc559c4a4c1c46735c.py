
# apl-source:1
# مثال 479 — محاكي جدار ناري
# apl-source:2
# Firewall simulator
# apl-source:3
# Demonstrates: قواعد سماح ومنع
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/479-firewall-sim.apl
# apl-source:6

# apl-source:7
ممنوعة = ["10.0.0.5", "192.168.1.99"]
# apl-source:8
منافذ_مفتوحة = [80, 443]
# apl-source:9

# apl-source:10
def افحص(عنوان, منفذ):
    # apl-source:11
    if ممنوعة.count(عنوان) > 0:
        # apl-source:12
        return "محظور: عنوان ممنوع"
    # apl-source:13
    if منافذ_مفتوحة.count(منفذ) == 0:
        # apl-source:14
        return "محظور: منفذ مغلق"
    # apl-source:15
    return "مسموح"
# apl-source:16

# apl-source:17
print(افحص("10.0.0.5", 80))
# apl-source:18
print(افحص("8.8.8.8", 22))
# apl-source:19
print(افحص("8.8.8.8", 443))
# apl-source:20
