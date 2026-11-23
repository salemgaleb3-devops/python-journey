
# packing with **Args   عند عمل ** المطلوب البيانات تكون قاموس 


show_skills = {

    "python" : " 90%",
    "Go" : "77%",
    "js" : " 20"
}


def my_skills(**skills) : 

    print(type(skills))

    for skill, value in skills.items():

        print(f" {skill} => {value}")

my_skills(HTML = "80%", CSS = "60%", PHP = " 55%")  # بما ان البارميتر ** نحط البيانات التي تريد 
my_skills(**show_skills)


