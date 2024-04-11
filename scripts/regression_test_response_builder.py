import os
import json
import requests
import pickle
import sys
from time import sleep


def decode_payload(payload: bytes):
    return pickle.loads(payload)


def encode_payload(payload: dict):
    return pickle.dumps(payload)


def call(url, payload, headers, attempts=3, interval_between_attempts=5):
    while attempts > 0:
        try:
            response = requests.post(
                url,
                payload,
                headers=headers,
            )

            if response.ok:
                return response.content

            print(
                f"It returned status code {response.status_code} with message {response.text}"
            )

            sleep(interval_between_attempts)
        except:
            pass
        finally:
            attempts -= 1
            print(f"{attempts} attempts remaining for {url}...")

    raise Exception()


def get_abspath(path: str):
    current_path = os.path.dirname(os.path.abspath(__file__))

    root_path = os.path.abspath(
        os.path.join(
            current_path,
            os.pardir,
        )
    )

    return os.path.join(
        root_path,
        path,
    )


def get_request_file_path(db):
    request_file = f"{db}.json"

    filepath = os.path.join(
        "tests",
        "integration",
        "fixtures",
        "request",
        request_file,
    )

    return get_abspath(filepath)


def get_response_file_path(db):
    request_file = f"{db}.json"

    filepath = os.path.join(
        "tests",
        "integration",
        "fixtures",
        "response",
        request_file,
    )

    return get_abspath(filepath)


def generate_response_output(response_file_path: str, data: dict):
    with open(response_file_path, "w") as file:
        content = json.dumps(data, default=lambda obj: repr(obj), indent=4)

        file.write(content)


def main(host: str, port: str, db: str):
    request_file_path = get_request_file_path(db)
    result = {}

    with open(request_file_path, "r") as file:
        requests = json.loads(file.read())

        for action, payload in requests.items():
            print(f"Generating response for {action}...")
            encoded_payload = encode_payload(
                {
                    "action": action,
                    "input": payload,
                }
            )
            url = f"http://{host}:{port}/function/query-engine"
            headers = {
                "Content-Type": "application/octet-stream",
                "Accept-Type": "application/octet-stream",
            }

            response = call(url, encoded_payload, headers)

            result[action] = decode_payload(response)
            print(f"Response generated for {action}")

    response_file_path = get_response_file_path(db)
    generate_response_output(response_file_path, result)

    print("Done.")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(
            f"Usage: python3 {sys.argv[0]} <host> <port> <animals | bio>\n\nExample: python3 {sys.argv[0]} 45.63.85.59 8080 animals"
        )
        sys.exit(1)

    host = sys.argv[1]
    port = sys.argv[2]
    db = sys.argv[3]

    main(host, port, db)
