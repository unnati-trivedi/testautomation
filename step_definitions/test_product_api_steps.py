import requests
import json
import jsonpath
import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from utility import APIUtility
from utility import OperationUtility


baseUrl = ""
path = ""
apiutilsObj = APIUtility.APIUtility()
utilsObj = OperationUtility.Utility()


validBody = """
{
product(productId: "%s") {
    ... on Product {
	productId
    productName
    productUri
    destinationId
    kfEarnMilesPromoText
    keyCallouts
    location
    shortDescription
    mediaData
    productTags { tagId }
    currency
    duration
    guideLanguages
    cancellationType
    cancellationWindow
    cancellationWindowText
    minGroupSize
    maxGroupSize
    openDateTicket
    collectPhysicalTicket
    confirmationType
    confirmationTypeText
    voucherType
    redemptionType
    priceRangeFrom
    priceRangeTo
    latitude
    longitude
    address
    availabilityStartDate
    availabilityEndDate
    productMetaView
    status
    rating
    reviewCount
    trackMeta
    wishlistedCustomerCount
    __typename
    }
}
}"""



invalidBody = """
{
product(productId: "phpv2") {
    ... on Product {
	%s
    productName
    productUri
    destinationId
    kfEarnMilesPromoText
    keyCallouts
    location
    shortDescription
    mediaData
    productTags { tagId }
    currency
    unnati
    duration
    guideLanguages
    cancellationType
    cancellationWindow
    cancellationWindowText
    minGroupSize
    maxGroupSize
    openDateTicket
    collectPhysicalTicket
    confirmationType
    confirmationTypeText
    voucherType
    redemptionType
    priceRangeFrom
    priceRangeTo
    latitude
    longitude
    address
    availabilityStartDate
    availabilityEndDate
    productMetaView
    status
    rating
    reviewCount
    trackMeta
    wishlistedCustomerCount
    __typename
    }
}
}"""

scenarios('../features/product_api.feature')

@given(parsers.parse('I set POST endpoint to "{endpoint}" for getting product details'))
def set_base_url(endpoint):
    apiutilsObj.setbaseURL(endpoint)

@when(parsers.parse('I am sending POST Request with valid Product ID "{productID}"'))
def send_post_request(productID):
    post_response = apiutilsObj.post_request(validBody%(productID))
 
@when(parsers.parse('I am sending POST Request with "{payloadType}" payload and "{field}"'))
def search_phrase(payloadType,field):   
    if payloadType == "invalid":     
        post_response = apiutilsObj.post_request(invalidBody%(field)) 
 
@then(parsers.parse('results are shown with success "{rCode}"'))
def search_results(rCode):
    assert apiutilsObj.response_code == int(rCode)

@then(parsers.parse('results are shown with error code "{rCode}" and with proper error message describing error in "{field}"'))
def search_results(rCode,field):
    assert apiutilsObj.response_code == int(rCode)
    expectedMessage =  """Cannot query field "%s" on type "Product".""" % field
    actualMessage = apiutilsObj.responseJson["errors"][0]["message"].casefold()
    assert expectedMessage.casefold() == actualMessage.casefold()

@then('I expect response body of this request to be non-empty')
def validate_nonempty_response():
    assert apiutilsObj.responseJson is not None

@then('I expect API response content to have Correct Json Schema')
def validate_json_with_schema():
    schemajson = utilsObj.readSchemaFromFile('test_data/product_schema.json')
    result = utilsObj.validateJsonWithSchema(schemajson, apiutilsObj.responseJson)
    assert result == True

@then('I expect API response to have Correct Response headers')
def validate_response_header():
    assert (apiutilsObj.responseHeader) is not None

@then(parsers.parse('I expect API Response Header "{rHeaderKey}" to have value "{rHeaderValue}"'))
def validate_response_header(rHeaderKey,rHeaderValue):
    headerValue = (apiutilsObj.responseHeader.get(rHeaderKey))
    assert headerValue == rHeaderValue

@then(parsers.parse('I expect "{requiredHeaders}" API Response Header exists in API Response'))
def validate_response_header(requiredHeaders):
    if requiredHeaders in apiutilsObj.responseHeader:
        print(requiredHeaders, " Exists ")
    else:
        assert False

@then('I expect API Response Header is Valid Json')
def validate_response_header_is_valid_json():
    isValid = utilsObj.validateJSON(json.dumps(apiutilsObj.responseHeader.__dict__['_store']))
    assert isValid
    
    
