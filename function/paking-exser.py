

my_tubel = ( "html", "css", "js")

showw_skills = {

    "python" : " 90%",
    "Go" : "77%",
    "js" : " 20"
}


def show_slills(name, *skills, **skills_with_progress) :

    print(f"Hello {name} \nSkills with no progress is ")

    for skill in skills :

        print(f"{skill}")

    print(f"Skills with  progress is ")

    for skill_key, skill_value in skills_with_progress.items() :

        print(f"{skill_key} => {skill_value}")

show_slills("salem", *my_tubel, **showw_skills )


