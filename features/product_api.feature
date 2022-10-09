@automatic
Feature: Product Browsing

     Scenario Outline: Valid POST Request with Valid existing product ID
        Given I set POST endpoint to "https://traveller-core.dev.pelago.co/graphql" for getting product details
        When I am sending POST Request with valid Product IDs <productId>
        Then results are shown with success "200"
        And I expect response body of this request to be NON-EMPTY with "product" details
        And I expect API response "productId" to have correct value as <productId> 
        Examples:
            | productId |
            | phpv2     |

    Scenario Outline: Valid POST Request with non-existing product ID
        Given I set POST endpoint to "https://traveller-core.dev.pelago.co/graphql" for getting product details
        When I am sending POST Request with valid Product IDs <productId>
        Then results are shown with success "200"
        And I expect response body of this request to be EMPTY with no "product" details
        Examples:
            | productId |
            | UNREAL    |
            | 123456    |

    Scenario: Valid POST Request with EMPTY product ID
        Given I set POST endpoint to "https://traveller-core.dev.pelago.co/graphql" for getting product details
        When I am sending POST Request with blank Product ID " "
        Then results are shown with success "200"
        And I expect response body of this request to be EMPTY with no "product" details

    Scenario: Valid POST Request with INVALID payload
        Given I set POST endpoint to "https://traveller-core.dev.pelago.co/graphql" for getting product details
        When I am sending POST Request with "invalid" payload and "INCORRECTFIELD"
        Then results are shown with error code "400" and with proper error message describing error in "INCORRECTFIELD"
        
    Scenario: Valid POST Request with Valid existing product ID should return Correct Response Schema
        Given I set POST endpoint to "https://traveller-core.dev.pelago.co/graphql" for getting product details
        When I am sending POST Request with valid Product ID "phpv2"
        Then I expect API response content to have Correct Json Schema

    Scenario: Valid POST Request with Valid existing product ID should return Correct Response Headers
        Given I set POST endpoint to "https://traveller-core.dev.pelago.co/graphql" for getting product details
        When I am sending POST Request with valid Product ID "phpv2"
        Then I expect API response to have Correct Response headers
        And I expect API Response Header is Valid Json
        And I expect "Connection" API Response Header exists in API Response
        And I expect API Response Header "Connection" to have value "keep-alive"
        And I expect API Response Header "Content-Type" to have value "application/json"
        And I expect API Response Header "Transfer-Encoding" to have value "chunked"
        And I expect API Response Header "Strict-Transport-Security" to have value "max-age=31536000"

    Scenario: Valid POST Request with Valid existing product ID should return expected response parameters
        Given I set POST endpoint to "https://traveller-core.dev.pelago.co/graphql" for getting product details
        When I am sending POST Request with valid Product ID "phpv2" 
        Then I expect API response "duration" to have correct value "2 - 3 Hours"
    
    Scenario: Valid POST Request with Valid existing product ID should have response param values from VALID Value range
        Given I set POST endpoint to "https://traveller-core.dev.pelago.co/graphql" for getting product details
        When I am sending POST Request with valid Product ID "phpv2" 
        Then I expect API response "cancellationType" to be one of these "NO_CANCELLATION OR  OR ALLOWED_CANCELLATION OR CONDITIONAL_CANCELLATION"
        And I expect API response "destinationId" to be one of these "singapore OR india"
        And I expect API response "confirmationType" to be one of these "MANUAL OR AUTOMATED"
        And I expect API response "voucherType" to be one of these "EXTERNAL OR PELAGO"

    Scenario: Cancellation Window checks
        Given I set POST endpoint to "https://traveller-core.dev.pelago.co/graphql" for getting product details
        When I am sending POST Request with valid Product ID "phpv2" 
        Then For Product that has "cancellationType" set to "NO_CANCELLATION", I expect API response "cancellationWindow" to be "0"
        Then For Product that has "cancellationType" set to "NO_CANCELLATION", I expect API response "cancellationWindowText" to show "No Cancellation Allowed"

    Scenario: Price Range Tests
        Given I set POST endpoint to "https://traveller-core.dev.pelago.co/graphql" for getting product details
        When I am sending POST Request with valid Product ID "phpv2" 
        Then I expect API response "priceRangeFrom" to be "positive" number
        And I expect API response "priceRangeTo" to be greater than "priceRangeFrom"

    Scenario Outline: Media Data Images Should have correct path and image references
        Given I set POST endpoint to "https://traveller-core.dev.pelago.co/graphql" for getting product details
        When I am sending POST Request with valid Product ID "phpv2" 
        Then I expected All Products with "destinationId" set to "singapore" to have Media Data file <sizes> path under "https://traveller.dev.pelago.co/img/products/SG-Singapore/"
        And I expect Media Data files to have all <sizes> included with correct sizepath set for each
        Examples:
            | sizes      |
            | xsmall     |
            | webpXsmall |
            | small      |
            | webpSmall  |
            | medium     |
            | webpMedium |
            | large      |
            | webpLarge  |
            | xlarge     |
            | webpXlarge |  


    Scenario: Longitude Latitude
        Given I set POST endpoint to "https://traveller-core.dev.pelago.co/graphql" for getting product details
        When I am sending POST Request with valid Product ID "phpv2" 
        Then I expect API response parameter "location" to have VALID "latitude" and "longitude"

    Scenario: No Broken Links
        Given I set POST endpoint to "https://traveller-core.dev.pelago.co/graphql" for getting product details
        When I am sending POST Request with valid Product ID "phpv2" 
        Then I expect API response parameter "mapUrl" under "location" to have no broken links
        And I expect API response parameter "url" under "mediaData" to have no broken links
