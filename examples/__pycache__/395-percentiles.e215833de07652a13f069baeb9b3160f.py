
# apl-source:1
# مثال 395 — المئينيات
# apl-source:2
# Percentiles
# apl-source:3
# Demonstrates: الربعية والمئين
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/395-percentiles.apl
# apl-source:6

# apl-source:7
def مئين(قائمة, نسبة):
    # apl-source:8
    م = sorted(قائمة)
    # apl-source:9
    فهرس = (len(م) - 1) * نسبة / 100
    # apl-source:10
    أدنى = int(فهرس)
    # apl-source:11
    أعلى = أدنى + 1
    # apl-source:12
    if أعلى >= len(م):
        # apl-source:13
        return م[أدنى]
    # apl-source:14
    كسر = فهرس - أدنى
    # apl-source:15
    return م[أدنى] + (م[أعلى] - م[أدنى]) * كسر
# apl-source:16

# apl-source:17
درجات = [55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
# apl-source:18
print("المئين 25:", مئين(درجات, 25))
# apl-source:19
print("المئين 50:", مئين(درجات, 50))
# apl-source:20
print("المئين 90:", مئين(درجات, 90))
# apl-source:21
