from zohosdk.src.com.zoho.officeintegrator.v1.create_document_parameters import CreateDocumentParameters
from zohosdk.src.com.zoho.officeintegrator.v1.create_document_response import CreateDocumentResponse
from zohosdk.src.com.zoho.officeintegrator.v1.v1_operations import V1Operations

class CreateDocument:

    @staticmethod
    def execute():
        document = CreateDocumentParameters()
        v1Operations = V1Operations()

        response = v1Operations.create_document(document)

        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            response_object = response.get_object()
            
            if response_object is not None:
                
                if isinstance(response_object, CreateDocumentResponse):

                    print('Docment URL : ' + str(response_object.get_document_id()))
                    print('Docment URL : ' + str(response_object.get_document_url()))
                    
            
CreateDocument.execute()
                        

