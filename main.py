import turtle
import pandas

def get_mouse_click_coor(x, y):
    print(x, y)

data = pandas.read_csv("50_states.csv")
screen = turtle.Screen()
screen.title("America Game")
image = "america.gif"
screen.addshape(image)
turtle.shape(image)
game_on = True
Countries = data.country
ia = turtle.Turtle()
ia.hideturtle()
ia.penup()
screen.setup(height=1111)
correct_num = 0
correct_answers = []

while correct_num != 50:
    user_input = screen.textinput(title=f"{correct_num}/36 Countries Correct", prompt="What's another Country?").lower()
    if user_input == "exit":
        break
    if user_input not in correct_answers:
        for country in Countries:
            if user_input == country.lower():
                country_data = data[data.country == country]
                ia.goto(x=int(country_data.x), y=int(country_data.y))
                ia.write(f"{country}", font=("Courier", 16, "bold"))
                correct_answers.append(country)
                correct_num += 1
    print(correct_answers)

countries_to_learn = data.country.tolist()
for answer in correct_answers:
    index = countries_to_learn.index(answer)
    countries_to_learn.pop(index)

data_dict = {
    "States To Learn": countries_to_learn
}
data = pandas.DataFrame(data_dict)
data.to_csv("countries_to_learn.csv")
