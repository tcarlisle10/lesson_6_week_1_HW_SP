file_system = [
    [
        "nothing.txt",
        "dog_pic.png",
        [
            "secret_plan.pdf"
        ]
    ],
    "notion.app",
    "slack.app",
    [
        "fun.txt",
        [
            "meaningless_file.txt",
            "chicken_dinner.txt"
        ],
        "not_fun.txt"
    ],
    "zoom.app"
]

target = "chicken_dinner.txt"

def find_file(file_system, target):

    for item in file_system:
        if item == target:
            return "HOORAY"
        elif isinstance(item, list):
            response = find_file(item, target)
            if response == "HOORAY":
                return response
            
    return "File Not Found"

print(find_file(file_system, target))
