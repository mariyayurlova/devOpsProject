import requests

def terminate_server(server_url):
    try:
        response = requests.get(f'{server_url}/shutdown')
        if response.status_code == 200:
            print(f"Successfully terminated {server_url}")
        else:
            print(f"Failed to terminate {server_url}")
    except Exception as e:
        print(f"Error terminating {server_url}: {e}")

if __name__ == '__main__':
    terminate_server('http://127.0.0.1:5000')
    terminate_server('http://127.0.0.1:5001')