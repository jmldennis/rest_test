import requests
import pdb


def get_chuck_joke():
    url = "https://api.chucknorris.io/jokes/random"
    headers = {'Accept':'application/json'}
    response = requests.get(url,headers=headers)
    response_json = response.json()
    return response_json["value"]


def test():

    url = "https://api.chucknorris.io/jokes/random"

    headers = {'Accept':'application/json'}

    response = requests.get(url,headers=headers)

    print(f"The status code returned was {response.status_code}")

    if response.status_code == 200:
        try:
            response_json = response.json()
            id = response_json["id"]
            joke = response_json["value"]
        except:
            print("Did not receive JSON")
            quit()
    else:
        quit()
    

    #print(response_json.keys())

    #id, joke, status = response_json.values()

    #print(id)
    print(joke)


def main():
    num_chuck_jokes = input("How many Chuck Norris jokes do you want? <= 10\n")
    num_chuck_jokes = int(num_chuck_jokes)
    if num_chuck_jokes > 0 and num_chuck_jokes <= 10:
        i = 0
        while num_chuck_jokes > 0:
            i += 1
            print(f"{i}. {get_chuck_joke()}")
            num_chuck_jokes -= 1
    else:
        print("Error: Number of Jokes should be between 1 and 10")

if __name__ == "__main__":
    #test()
    main()
    #pdb.set_trace()     #for debugging your code