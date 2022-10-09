import requests
import json
import jsonpath
import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from utility import APIUtility
from utility import OperationUtility
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

#GIVEN METHODS
@given(parsers.parse('I have set API request endpoint to "{endpoint}" for getting product details'))
def set_base_url(endpoint):
    apiutilsObj.setbaseURL(endpoint)


#WHEN METHODS
@when(parsers.parse('I am sending "{method}" Request with "{payloadType}" payload and blank Product ID "{argument}"'))
@when(parsers.parse('I am sending "{method}" Request with "{payloadType}" payload and valid Product ID "{argument}"'))
@when(parsers.parse('I am sending "{method}" Request with "{payloadType}" payload and valid Product IDs {argument}'))
@when(parsers.parse('I am sending "{method}" Request with "{payloadType}" payload and non-existing Product IDs {argument}'))
@when(parsers.parse('I am sending "{method}" Request with "{payloadType}" payload and "{argument}"'))

def send_post_request(method,payloadType,argument):
    """
    Sends API Request based on method, argument, payloadType
    method : defines method type POST or GET or UPDATE or DELETE
    argument : defines API request body argument
    payloadType : defines whether API Request should be sent with Valid or Invalid payload body
    """
    if method == "POST":
        if payloadType == "invalid":
            post_response = apiutilsObj.post_request(invalidBody%(argument))
        else:
            post_response = apiutilsObj.post_request(validBody%(argument))
        

#THEN METHODS
@then(parsers.parse('results are shown with success "{rCode}"'))
def validate_responsecode(rCode):
    """
    Asserts whether API Response code is as intended
    rcode : expected response code
    """
    assert apiutilsObj.response_code == int(rCode)

@then(parsers.parse('results are shown with error code "{rCode}" and with proper error message describing error in "{field}"'))
def validate_responsecode_and_responsemessage(rCode,field):
    assert apiutilsObj.response_code == int(rCode)
    expectedMessage =  """Cannot query field "%s" on type "Product".""" % field
    actualMessage = apiutilsObj.responseJson["errors"][0]["message"].casefold()
    assert expectedMessage.casefold() == actualMessage.casefold()

@then(parsers.parse('I expect response body of this request to be NON-EMPTY with "{param}" details'))
def validate_nonempty_response(param):
    assert apiutilsObj.responseJson is not None
    assert apiutilsObj.responseJson['data'] is not None
    assert apiutilsObj.responseJson['data'][param] is not None
    assert (len(apiutilsObj.responseJson['data'])) != 0
    assert (len(apiutilsObj.responseJson['data'][param]) ) != 0

@then(parsers.parse('I expect response body of this request to be EMPTY with no "{param}" details'))
def validate_empty_response(param):
    assert apiutilsObj.responseJson is not None
    assert apiutilsObj.responseJson['data'] is not None
    assert apiutilsObj.responseJson['data'][param] is not None
    assert (len(apiutilsObj.responseJson['data'])) != 0
    assert (len(apiutilsObj.responseJson['data'][param]) ) == 0
    
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
    assert requiredHeaders in apiutilsObj.responseHeader

@then('I expect API Response Header is Valid Json')
def validate_response_header_is_valid_json():
    isValid = utilsObj.validateJSON(json.dumps(apiutilsObj.responseHeader.__dict__['_store']))
    assert isValid

@then(parsers.parse('I expect API response "{field}" to have correct value "{fieldValue}"'))
@then(parsers.parse('I expect API response "{field}" to be "{fieldValue}"'))
@then(parsers.parse('I expect API response "{field}" to show "{fieldValue}"'))
@then(parsers.parse('I expect API response "{field}" to be one of these "{fieldValue}"')) 
@then(parsers.parse('I expect API response "{field}" to have correct value as {fieldValue}'))
def validate_response_parameter_value_is_valid(field, fieldValue):
    if "OR" not in fieldValue:
        print(type(utilsObj.getResponseJsonKeyValue(apiutilsObj.responseJson,field)))
        print(type(fieldValue))
        assert utilsObj.getResponseJsonKeyValue(apiutilsObj.responseJson,field).casefold() == fieldValue.casefold()
    else:    
        list = fieldValue.split(" OR ")
        assert utilsObj.getResponseJsonKeyValue(apiutilsObj.responseJson,field) in list

@then(parsers.parse('For Product that has "{field}" set to "{fieldValue}", I expect API response "{stringDependentfield}" to show "{stringDependentFieldValue}"'))
def dependent_field_value_check(field,fieldValue,stringDependentfield,stringDependentFieldValue):   
    if utilsObj.getResponseJsonKeyValue(apiutilsObj.responseJson,field) == fieldValue:
        assert utilsObj.getResponseJsonKeyValue(apiutilsObj.responseJson,stringDependentfield) == (stringDependentFieldValue)
        
@then(parsers.parse('For Product that has "{field}" set to "{fieldValue}", I expect API response "{numericDependentfield}" to be "{numericDependentFieldValue}"'))
def dependent_field_value_check(field,fieldValue,numericDependentfield,numericDependentFieldValue):   
    if utilsObj.getResponseJsonKeyValue(apiutilsObj.responseJson,field) == fieldValue:
        assert utilsObj.getResponseJsonKeyValue(apiutilsObj.responseJson,numericDependentfield) == int(numericDependentFieldValue)


@then(parsers.parse('I expect API response "{field}" to be "{numberType}" number'))
def validate_response_parameter_value_is_positive_negative(field, numberType):
    if numberType == "positive":
        assert utilsObj.getResponseJsonKeyValue(apiutilsObj.responseJson,field) > 0
    elif numberType == "negative":
        assert utilsObj.getResponseJsonKeyValue(apiutilsObj.responseJson,field) < 0

@then(parsers.parse('I expect API response "{bigField}" to be greater than "{smallerField}"'))
def validate_response_parameter_value_is_positive_negative(bigField, smallerField):
    utilsObj.getResponseJsonKeyValue(apiutilsObj.responseJson,bigField) >  utilsObj.getResponseJsonKeyValue(apiutilsObj.responseJson,smallerField)
    
@then(parsers.parse('I expect Media Data files to have all {sizes} included with correct sizepath set for each'))  
def validate_exists(sizes):
    actualSizePath = utilsObj.getMediaDataKeysFromArray(apiutilsObj.responseJson['data']['product']['mediaData'],sizes) 
    assert utilsObj.checkKeyexistInArray(apiutilsObj.responseJson['data']['product']['mediaData'],sizes)
    if "web" in actualSizePath:
        webPath = sizes[4:].casefold()
        expectedSizePath = "-"+webPath+".webp"
    else:
        expectedSizePath = "-"+sizes+".jpg"

    assert actualSizePath.endswith(expectedSizePath)

@then(parsers.parse('I expected All Products with "{field}" set to "{testFieldValue}" to have Media Data file {sizes} path under "{expectedFieldValue}"'))  
def validate_exists(field,testFieldValue,sizes,expectedFieldValue):
    pathValue= str(utilsObj.getResponseJsonKeyValue(apiutilsObj.responseJson,field))
    if utilsObj.getResponseJsonKeyValue(apiutilsObj.responseJson,field) == testFieldValue:
        testPath = utilsObj.getMediaDataKeysFromArray(apiutilsObj.responseJson['data']['product']['mediaData'],sizes) 
        assert testPath.startswith(expectedFieldValue)

@then(parsers.parse('I expect API response parameter "{field}" to have VALID "{latitude}" and "{longitude}"'))  
def validate_exists(field,latitude,longitude):
    latitude =  utilsObj.getLocationKeysInArray(apiutilsObj.responseJson['data']['product']['location'],latitude)
    longitude =  utilsObj.getLocationKeysInArray(apiutilsObj.responseJson['data']['product']['location'],longitude)
    assert utilsObj.validate_latitude(latitude)
    assert utilsObj.validate_longitude(longitude)


@then(parsers.parse('I expect API response parameter "{field}" under "{parentField}" to have no broken links'))
def validate_response_parameter_value_is_positive_negative(field, parentField):
    if parentField == "location":
        fieldValue =  utilsObj.getLocationKeysInArray(apiutilsObj.responseJson['data']['product']['location'],field)
        
    elif parentField == "mediaData":
        fieldValue = utilsObj.getMediaDataKeysFromArray(apiutilsObj.responseJson['data']['product']['mediaData'],field) 
    
    assert utilsObj.validate_url(fieldValue)

@then(parsers.parse('I expect "{field}" value to be within range of "{minFieldValue}" to "{maxtFieldValue}"'))
def dependent_field_value_check(field,minFieldValue,maxFieldValue):   
    assert utilsObj.getResponseJsonKeyValue(apiutilsObj.responseJson,field) > minFieldValue
    assert utilsObj.getResponseJsonKeyValue(apiutilsObj.responseJson,field) < maxFieldValue
# 

@then(parsers.parse('I expect API response time should be less than "{sla}" seconds'))
def validate_response_time(sla):   
    assert apiutilsObj.responseTime <= int(sla)


    
