from api_agify import APIAgify

def main():
    params = {'name': 'mary'}

    api = APIAgify(params, 10)
    status, message = api.call_api()
    if status == 0:
        print(api)
        return
    
    print('\nAn error occurred in the API call\n')
    print(message)

if __name__ == '__main__':
    main()