from config import connect_str, container_name, endpoint, key
from upload import upload_document
from process import process_document
from analysis import identificar_fraude, validar_autenticidade

def main():
    file_path = "seuarquivo.pdf"

    upload_document(file_path, connect_str, container_name)

    result = process_document(file_path, endpoint, key)

    identificar_fraude(result)
    validar_autenticidade(result)

if __name__ == "__main__":
    main()