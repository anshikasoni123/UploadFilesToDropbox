import dropbox

class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token

    def upload_file(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(),file_to)

def main():
    access_token = "sl.A_cZ9sXOZ7DbDwvGnb8Xv813F_iqX7CCNkmvoUICkazw2KQ-FUAVqG6M3orXMThRdPDTux3exFVNcwmgwLlYwHu9KWISE5aaHdcSp8HamXBSbvFzpqXBnOaKTsJ4nGbmZ8EZ1hkuDWM"
    transferData = TransferData(access_token)

    file_from = input("Write your file path here :- ")
    file_to = input("Write your dropbox file path here :- ")

    transferData.upload_file(file_from,file_to)
    print("Your file has transfered!!!")


main()