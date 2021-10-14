data = [
    {
        "id": "123",
        "name": "widget"
    },
    {
        "id": "456",
        "name": "widget"
    }
]

expected = {
    "123": {
        "id": "123",
        "name": "widget"
    },
    "456": {
        "id": "456",
        "name": "widget"
    }
}

# would do this to search through data faster


def transform(data_list, key_name):
    output = {}
    for i in data_list:
        print('i = ' + str(i) + '\n')
        print('i at key_name = ' + str(i[key_name]) + '\n')
        output[i[key_name]] = i
    return output

# example call to function


print(transform(data, "id"))
