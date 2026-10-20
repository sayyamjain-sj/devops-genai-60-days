def greet(name):
    return f"Hello, {name}"

message = greet("Sayyam")
print(message)

def check_service(status):
    if status == "healthy":
        return True

    return False

print(check_service("healthy"))
print(check_service("down"))