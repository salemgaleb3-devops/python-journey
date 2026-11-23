
# print(1, 2, 3, 4)
# mylst = [1, 2, 3, 4]
# print(mylst)
# print(*mylst)   # * packing
#
# def say_hello(*people):   # * قي الارقيومنت حط الي يكون لان هنا موجود *
#
#         for name in people:
#             print(f"Hello {name}")
#
# say_hello("salem", " Ahmed", "Ali")

def show_de(name, *skills) :

    print(f"{name.capitalize()} skills is : ")

    for skill in skills :

        print(skill.upper())

show_de("salem", "PHP", "CSS", "C#")
show_de("ali", "PHP", "CSS", "C#", "python", "js")

