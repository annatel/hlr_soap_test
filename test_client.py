from zeep import Client
from zeep.exceptions import Error, XMLParseError

soap_client = Client("PUT_HERE_THE_URL_TO_THE_WSDL")
try:
    soap_client.service.getSubscriberInfo(operatorName='Annatel', subscriberId='551a91e2-5da0-4c52-a140-50a9c68a5d76')
except XMLParseError:
  print("XMLParseError - Failed to parse the xml response.")
else:
  print("All is good!")