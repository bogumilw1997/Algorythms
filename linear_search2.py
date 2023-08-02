def index_of_item(colletion, target):
    for i in range(len(colletion)):
        if target == colletion[i]:
            return i
    return None