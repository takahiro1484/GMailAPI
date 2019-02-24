import httplib2

from apiclient.discovery import build
from lib.auth_request import AuthRequest


SCOPE = "https://www.googleapis.com/auth/gmail.readonly"

def main():
    auth_request = AuthRequest()
    credential = auth_request.get_credential(SCOPE)

    http = httplib2.Http()
    credential_http = credential.authorize(http)

    # GMailAPIServiceのインスタンスを作成
    service = build("gmail", "v1", http=credential_http)

    messages = service.users().messages()

    # メールボックス内のメッセージを一覧を取得
    messages_dict = messages.list(userId="me", maxResults=10).execute()

    for message in messages_dict["messages"]:
        message = messages.get(userId="me", id=message["id"]).execute()
        print(message["payload"].get("parts"))


if __name__ == "__main__":
    main()