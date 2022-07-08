import requests
import pdb


def get_dad_joke():
    url = "https://icanhazdadjoke.com"
    headers = {'Accept':'application/json'}
    response = requests.get(url,headers=headers)
    response_json = response.json()
    return response_json["joke"]


def test():

    url = "https://icanhazdadjoke.com"

    headers = {'Accept':'application/json'}

    response = requests.get(url,headers=headers)

    print(f"The status code returned was {response.status_code}")

    if response.status_code == 200:
        try:
            response_json = response.json()
            id = response_json["id"]
            joke = response_json["joke"]
            status = response_json["status"]
        except:
            print("Did not receive JSON")
            quit()
    else:
        quit()
    

    print(response_json.keys())

    #id, joke, status = response_json.values()

    print(id)
    print(joke)
    print(status)


def main():
    num_dad_jokes = input("How many dad jokes do you want? <= 10\n")
    num_dad_jokes = int(num_dad_jokes)
    if num_dad_jokes > 0 and num_dad_jokes <= 10:
        i = 0
        while num_dad_jokes > 0:
            i += 1
            print(f"{i}. {get_dad_joke()}")
            num_dad_jokes -= 1

if __name__ == "__main__":
    #test()
    main()
    #pdb.set_trace()     #for debugging your code