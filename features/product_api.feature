@feature-tag1
Feature: Product Browsing
    Scenario: Valid POST Request with Valid existing product ID
        Given I set POST endpoint to "https://traveller-core.dev.pelago.co/graphql" for getting product details
        When I am sending POST Request with valid Product ID "phpv2"
        Then results are shown with success "200"
        And I expect response body of this request to be non-empty
    
    @automatic @smoke
    Scenario: TrueVValid POST Request with Valid non-existing product ID
        Given I set POST endpoint to "https://traveller-core.dev.pelago.co/graphql" for getting product details
        When I am sending POST Request with valid Product ID "UNREAL"
        Then results are shown with success "200"
        And I expect response body of this request to be non-empty

    Scenario: VValid POST Request with EMPTY product ID
        Given I set POST endpoint to "https://traveller-core.dev.pelago.co/graphql" for getting product details
        When I am sending POST Request with valid Product ID " "
        Then results are shown with success "200"
        And I expect response body of this request to be non-empty
    
    @manual
    Scenario: Valid POST Request with INVALID payload
        Given I set POST endpoint to "https://traveller-core.dev.pelago.co/graphql" for getting product details
        When I am sending POST Request with "invalid" payload and "INCORRECTFIELD"
        Then results are shown with error code "400" and with proper error message describing error in "INCORRECTFIELD"
    
    @smoke
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

