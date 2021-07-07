import requests


class YaUploader:
    def __init__(self, token, file_path: str):
        self.token = token
        self.file_path = file_path

    def get_headers(self): #ЯДиск требует, чтобы в ContentType и Authorization были соответствующие параметры
        return {
            'ContentType': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    # def get_files_list(self):
    #     files_url = ' https://cloud-api.yandex.net/v1/disk/resources/files'
    #     headers = self.get_headers()
    #     response = requests.get(files_url, headers=headers)
    #     return response.json()

    def get_upload_link(self):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {"path": self.file_path, 'overwrite': 'true'}
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()

    def upload(self):
        href = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        self.get_upload_link()
        response = requests.put(href, data=open(self.file_path, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")

if __name__ == '__main__':
    token = 'AQAAAABJEzUOAADLW4KkmSFr80jKvpGfkda-RFM'

    uploader = YaUploader(token, 'photo.jpg')
    result = uploader.upload()
    print(result)
    header = uploader.get_headers()
    print(header)
    files_list = uploader.get_files_list()
    print(files_list)

