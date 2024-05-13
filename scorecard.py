games = [
    ["Skyrim", 8],
    ["Minecraft", 7],
    ["Manor Lords", 5]
]


def formatted_string(txt):
    template = "this is a test : {} that will replace the bracers with data"
    return template.format(txt)

def read_template():
    "read the template from a file"
    template_file = open("template.html", "r", encoding="utf8")
    template = template_file.read()
    template_file.close()
    return template


def format_template(template, data:list):
    "put the data into the template, the template requires 3 data inputs"
    game_comments =[] # this list sould contain 3 strings when complete
    for game in games:
        comment_temp = "The game {} has a score of {} out of 10"
        game_comments.append(comment_temp.format(game[0], game[1]))
    return template.format(game_comments[0], game_comments[1], game_comments[2])
    ...

def save_to_HTML(data, filename):
    "takes the processed tempate and save it to a file"
    ...

def display_page(filename):
    "open the web browser for the page"
    ...

#TESTS  
print(formatted_string("hello"))
print(formatted_string("how about this"))
print(read_template())
print(format_template(read_template(), games))











