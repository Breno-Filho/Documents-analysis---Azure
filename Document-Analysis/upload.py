from azure.storage.blob import BlobServiceClient

def upload_document(file_path, connect_str, container_name):
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    container_client = blob_service_client.get_container_client(container_name)
    with open(file_path, "rb") as data:
        container_client.upload_blob(name="seuarquivo.pdf", data=data)