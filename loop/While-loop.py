
# def plant_recommendation(care):
#     if care == 'low':
#         print('aloe')
#     elif care == 'medium':
#         print('pothos')
#     elif care == 'high':
#         print('orchid')

# plant_recommendation('low')
# plant_recommendation('medium')
# plant_recommendation('high')

myF = ["Os", "Ah", "Gh", "Al", "Sa", "Ta", "Ma", "Mo", "Wo", "Ra"]

# print(len(myF))

a = 0

while a < len(myF):

    print(f"#{str(a+1).zfill(3)} {myF[a]}")

    a += 1


