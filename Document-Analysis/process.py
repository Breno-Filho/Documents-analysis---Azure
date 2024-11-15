from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential

def process_document(file_path, endpoint, key):
    document_analysis_client = DocumentAnalysisClient(endpoint=endpoint, credential=AzureKeyCredential(key))
    with open(file_path, "rb") as fd:
        poller = document_analysis_client.begin_analyze_document("prebuilt-document", document=fd)
        result = poller.result()
    return result