# GraphQL API Test Automation
This is an automation framework to test the given GraphQL Apis.



## Explanation

### The Problem
The given problem was to write api tests automation for Travel Product that uses the mentioned GraphQL based API. 

##### All Required Considerations
Tests should support below mentioned requirements:
- ✅ Tests must be runnable from commandline 
- ✅ Parallel execution of tests
- ✅ Configurable on various OS
- ✅ Follow BDD
- ✅ Detailed instructions to run each tests


### The Solution
As a solution I developed this test automation framework that raise GraphQL API request that validates api responses and values for various test scenarios. This solution is following the Behavior Driven Development (BDD) method for writing and executing tests. The test definitaions mentioned in the feature files and that will act as an input to the whole framework.

_All the above mentioned required considerations have been implemented in this framework._

## Features
- Tests Execution reporting
- Filtering Tests during execution based on requirement
- Platform independent
- Tests Executable in parallel
- Tests support validating various scenarios:
  - Test API calls with valid and invalid API Request calls
  - Tests API response Schema for API to have expected response schema, with all required keys and expected key types
  - Tests API response headers
  - Tests API response content
  - Tests individual response parameters to have expected values, it falls expected value range, positive/negative type
  - Tests individual response parameters of links/url type it validates there are no broken links and correct path are set 
  - Tests for validity of longitude and latitude fields



## Technology & Tools

For this solution I've used following technologies.

| Technology/tools | Details |
| ------ | ------ |
| Python | I think we can easily build this kind of solution in other languages as well like Javascript, Java, etc. However, I had to choose one. I was comfortable with Python and I have experience in developing tests in python in past so I chose Python for now. I am also comfortable to write similar tests in other tech as well.  |
| requests | For HTTP based requirements, This is one of the popular lib that is being used by everyone generally. This is also one of the reliable libs in python. |
| pytest | For testing purpose, to execute assertion|
| pytest-bdd | This lib provides a good help in building BDD scenarios and execute them with pytest|

you can checkout the full list of libs used in the project from requirements.txt


## Solution Structure
| Items | Details |
| ------ | ------ |
| features/ | Feature files used to explain the test scenarios to test the feature. All scenarios with pre-condition, test steps, and expected outcomes are written in simple language. |
| step_definitions/ | This is where all parameterized step definitions are mentioned, they are responsible to get executed based on the test-behaviour mentioned in the Feature files.|
| test_data/ | Schema and test data to test the actual response against the expected format is placed here.|
| utility/ | Helper functions have been developed here|

# BDD
### Explain BDD implementation

As we all know, Behaviour Driven Development (BDD) is one of the useful techniques to be followed for developing software and writing automations. By design this technique is very much useful for technical people like developers and testers, also, it is easy for communicating the same with non-technical audiences like product teams and business participants.

_Here, I developed this solution using BDD and it is implemented as following:_
- Feature file has a natural language format describing the feature or part of the feature with expected outcomes.
- Each feature contains scenarios, that explains the specific scenario to test
- Using **Given, When, Then, and And**, explains the step by step behaviour of the system and develop a test case with expected output


#### BDD Example implemented
```
Feature: Product Browsing
  Scenario: Valid POST Request with Valid existing product ID should return Correct Response Headers
    Given I set POST endpoint to "https://traveller-core.dev.pelago.co/graphql" for getting product details
    When I am sending POST Request with valid Product ID “phpv2”
    Then I expect API response to have Correct Response headers
    And I expect API Response Header is Valid Json
    And I expect “Connection” API Response Header exists in API Response
    And I expect API Response Header “Connection” to have value “keep-alive”
    And I expect API Response Header “Content-Type” to have value “application/json”
    And I expect API Response Header “Transfer-Encoding” to have value “chunked”
    And I expect API Response Header “Strict-Transport-Security” to have value “max-age=31536000”
```

## Test cases 
Following are the test cases providing details on pre-conditions, test data, steps, and expected results:

Link to Testcases : https://docs.google.com/spreadsheets/d/1zTvgwCPJzLnazwW0-iOCZYDVwpGQH607q0mDP_zGYU0/edit?usp=sharing



## How to install?

#### Use virtual env

For Linux / MacOS
```sh
 # create my virtual env
 python -m venv myenv
 
 # activate virtual env
 cd myenv
 source myenv/bin/activate
```

Windows
```sh
 # create my virtual env
 python -m venv myenv
 
 # activate virtual env
 cd myenv
 myenv\Scripts\activate.bat
```

#### Install dependencies 
```sh
cd testautomation
pip install -r requirements.txt
```

#### Run Tests

**Running all tests**
in ~/testautomation
```sh
pytest --gherkin-terminal-reporter -vv
```

**Running tests with tags from [`feature-product`,`scenario-product`, `scenario-product-responseheaderchecks`, `scenario-product-response-valuechecks` ]**
in ~/testautomation
```sh
pytest --gherkin-terminal-reporter -vv -m feature-product
```

**Running all tests in parallel**
in ~/testautomation
```sh
pytest -n 2 -vv
```

Make use of the following in commandline: 
- `-n 2` or `-n <concurrent number>` if you want to run things in parallel.
- `--gherkin-terminal-reporter` for gherrkin fromatted output
- `-m <tag>` or `-m regression` to run tests only which are defined for `regression`


## Output

```
================================================= test session starts =================================================
platform win32 -- Python 3.9.6, pytest-7.1.3, pluggy-1.0.0 -- c:\tests\myenv\scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Tests\testautomation, configfile: pytest.ini
plugins: bdd-6.0.1, forked-1.4.0, xdist-2.5.0
collected 24 items

step_definitions/test_product_api_steps.py::test_valid_graphql_request_with_valid_product_id_arguments[phpv2] <- ..\myenv\lib\site-packages\pytest_bdd\scenario.py
Feature: Product GraphQL Tests
    Scenario: Valid GraphQL Request with Valid Product ID Arguments
        Given I have set API request endpoint to "https://traveller-core.dev.pelago.co/graphql" for getting product details
        When I am sending "POST" Request with "valid" payload and valid Product IDs phpv2
        Then results are shown with success "200"
        And I expect response body of this request to be NON-EMPTY with "product" details
        And I expect API response "productId" to have correct value as phpv2
    PASSED


step_definitions/test_product_api_steps.py::test_api_response_time_should_not_more_than_defined_sla__5_seconds_[phpv2] <- ..\myenv\lib\site-packages\pytest_bdd\scenario.py
Feature: Product GraphQL Tests
    Scenario: API Response Time should not more than defined SLA ( 5 Seconds )
        Given I have set API request endpoint to "https://traveller-core.dev.pelago.co/graphql" for getting product details
        When I am sending "POST" Request with "valid" payload and valid Product IDs phpv2
        Then I expect API response time should be less than "5" seconds
    PASSED


step_definitions/test_product_api_steps.py::test_valid_graphql_request_with_nonexisting_product_id_arguments[UNREAL] <- ..\myenv\lib\site-packages\pytest_bdd\scenario.py
Feature: Product GraphQL Tests
    Scenario: Valid GraphQL Request with Non-Existing Product ID Arguments
        Given I have set API request endpoint to "https://traveller-core.dev.pelago.co/graphql" for getting product details
        When I am sending "POST" Request with "valid" payload and non-existing Product IDs UNREAL
        Then results are shown with success "200"
        And I expect response body of this request to be EMPTY with no "product" details
    PASSED


step_definitions/test_product_api_steps.py::test_valid_graphql_request_with_nonexisting_product_id_arguments[123456] <- ..\myenv\lib\site-packages\pytest_bdd\scenario.py
Feature: Product GraphQL Tests
    Scenario: Valid GraphQL Request with Non-Existing Product ID Arguments
        Given I have set API request endpoint to "https://traveller-core.dev.pelago.co/graphql" for getting product details
        When I am sending "POST" Request with "valid" payload and non-existing Product IDs 123456
        Then results are shown with success "200"
        And I expect response body of this request to be EMPTY with no "product" details
    PASSED


step_definitions/test_product_api_steps.py::test_valid_graphql_request_with_nonexisting_empty_product_id_arguments <- ..\myenv\lib\site-packages\pytest_bdd\scenario.py
Feature: Product GraphQL Tests
    Scenario: Valid GraphQL Request with Non-Existing EMPTY Product ID Arguments
        Given I have set API request endpoint to "https://traveller-core.dev.pelago.co/graphql" for getting product details
        When I am sending "POST" Request with "valid" payload and blank Product ID " "
        Then results are shown with success "200"
        And I expect response body of this request to be EMPTY with no "product" details
    PASSED


step_definitions/test_product_api_steps.py::test_invalid_graphql_request_with_nonexisting_product_id_arguments <- ..\myenv\lib\site-packages\pytest_bdd\scenario.py
Feature: Product GraphQL Tests
    Scenario: Invalid GraphQL Request with Non-Existing Product ID Arguments
        Given I have set API request endpoint to "https://traveller-core.dev.pelago.co/graphql" for getting product details
        When I am sending "POST" Request with "invalid" payload and "INCORRECTFIELD"
        Then results are shown with error code "400" and with proper error message describing error in "INCORRECTFIELD"
    PASSED


step_definitions/test_product_api_steps.py::test_validate_schema_with_valid_graphql_request_having_valid_product_id_arguments <- ..\myenv\lib\site-packages\pytest_bdd\scenario.py
Feature: Product GraphQL Tests
    Scenario: Validate Schema with Valid GraphQL Request having Valid Product ID Arguments
        Given I have set API request endpoint to "https://traveller-core.dev.pelago.co/graphql" for getting product details
        When I am sending "POST" Request with "valid" payload and valid Product ID "phpv2"
        Then I expect API response content to have Correct Json Schema
    PASSED


step_definitions/test_product_api_steps.py::test_validate_correct_response_headers_with_valid_graphql_request_having_valid_product_id_arguments <- ..\myenv\lib\site-packages\pytest_bdd\scenario.py
Feature: Product GraphQL Tests
    Scenario: Validate Correct Response Headers with Valid GraphQL Request having Valid Product ID Arguments
        Given I have set API request endpoint to "https://traveller-core.dev.pelago.co/graphql" for getting product details
        When I am sending "POST" Request with "valid" payload and valid Product ID "phpv2"
        Then I expect API response to have Correct Response headers
        And I expect API Response Header is Valid Json
        And I expect "Connection" API Response Header exists in API Response
        And I expect API Response Header "Connection" to have value "keep-alive"
        And I expect API Response Header "Content-Type" to have value "application/json"
        And I expect API Response Header "Transfer-Encoding" to have value "chunked"
        And I expect API Response Header "Strict-Transport-Security" to have value "max-age=31536000"
    PASSED


step_definitions/test_product_api_steps.py::test_validate_response_parameters_values_with_valid_graphql_request_having_valid_product_id_arguments <- ..\myenv\lib\site-packages\pytest_bdd\scenario.py
Feature: Product GraphQL Tests
    Scenario: Validate Response Parameters values with Valid GraphQL Request having Valid Product ID Arguments
        Given I have set API request endpoint to "https://traveller-core.dev.pelago.co/graphql" for getting product details
        When I am sending "POST" Request with "valid" payload and valid Product ID "phpv2"
        Then I expect API response "duration" to have correct value "2 - 3 Hours"
    PASSED


step_definitions/test_product_api_steps.py::test_validate_response_parameter_values_are_in_expected_range_with_valid_graphql_request_having_valid_product_id_arguments <- ..\myenv\lib\site-packages\pytest_bdd\scenario.py
Feature: Product GraphQL Tests
    Scenario: Validate Response parameter values are in expected range with Valid GraphQL Request having Valid Product ID Arguments
        Given I have set API request endpoint to "https://traveller-core.dev.pelago.co/graphql" for getting product details
        When I am sending "POST" Request with "valid" payload and valid Product ID "phpv2"
        Then I expect API response "cancellationType" to be one of these "NO_CANCELLATION OR  OR ALLOWED_CANCELLATION OR CONDITIONAL_CANCELLATION"
        And I expect API response "destinationId" to be one of these "singapore OR india"
        And I expect API response "confirmationType" to be one of these "MANUAL OR AUTOMATED"
        And I expect API response "voucherType" to be one of these "EXTERNAL OR PELAGO"
    PASSED


step_definitions/test_product_api_steps.py::test_validate_cancellation_related_fields_to_have_correct_values_based_on_the_cancellation_type <- ..\myenv\lib\site-packages\pytest_bdd\scenario.py
Feature: Product GraphQL Tests
    Scenario: Validate Cancellation related fields to have correct values based on the Cancellation Type
        Given I have set API request endpoint to "https://traveller-core.dev.pelago.co/graphql" for getting product details
        When I am sending "POST" Request with "valid" payload and valid Product ID "phpv2"
        Then For Product that has "cancellationType" set to "NO_CANCELLATION", I expect API response "cancellationWindow" to be "0"
        Then For Product that has "cancellationType" set to "NO_CANCELLATION", I expect API response "cancellationWindowText" to show "No Cancellation Allowed"
    PASSED


step_definitions/test_product_api_steps.py::test_validate_response_parameter_price_range <- ..\myenv\lib\site-packages\pytest_bdd\scenario.py
Feature: Product GraphQL Tests
    Scenario: Validate Response Parameter Price Range
        Given I have set API request endpoint to "https://traveller-core.dev.pelago.co/graphql" for getting product details
        When I am sending "POST" Request with "valid" payload and valid Product ID "phpv2"
        Then I expect API response "priceRangeFrom" to be "positive" number
        And I expect API response "priceRangeTo" to be greater than "priceRangeFrom"
    PASSED


step_definitions/test_product_api_steps.py::test_validate_media_data_images_should_have_correct_links_and_image_references[xsmall] <- ..\myenv\lib\site-packages\pytest_bdd\scenario.py
Feature: Product GraphQL Tests
    Scenario: Validate Media Data Images Should have correct links and image references
        Given I have set API request endpoint to "https://traveller-core.dev.pelago.co/graphql" for getting product details
        When I am sending "POST" Request with "valid" payload and valid Product ID "phpv2"
        Then I expected All Products with "destinationId" set to "singapore" to have Media Data file xsmall path under "https://traveller.dev.pelago.co/img/products/SG-Singapore/"
        And I expect Media Data files to have all xsmall included with correct sizepath set for each
    PASSED


step_definitions/test_product_api_steps.py::test_validate_media_data_images_should_have_correct_links_and_image_references[webpXsmall] <- ..\myenv\lib\site-packages\pytest_bdd\scenario.py
Feature: Product GraphQL Tests
    Scenario: Validate Media Data Images Should have correct links and image references
        Given I have set API request endpoint to "https://traveller-core.dev.pelago.co/graphql" for getting product details
        When I am sending "POST" Request with "valid" payload and valid Product ID "phpv2"
        Then I expected All Products with "destinationId" set to "singapore" to have Media Data file webpXsmall path under "https://traveller.dev.pelago.co/img/products/SG-Singapore/"
        And I expect Media Data files to have all webpXsmall included with correct sizepath set for each
    PASSED


step_definitions/test_product_api_steps.py::test_validate_media_data_images_should_have_correct_links_and_image_references[small] <- ..\myenv\lib\site-packages\pytest_bdd\scenario.py
Feature: Product GraphQL Tests
    Scenario: Validate Media Data Images Should have correct links and image references
        Given I have set API request endpoint to "https://traveller-core.dev.pelago.co/graphql" for getting product details
        When I am sending "POST" Request with "valid" payload and valid Product ID "phpv2"
        Then I expected All Products with "destinationId" set to "singapore" to have Media Data file small path under "https://traveller.dev.pelago.co/img/products/SG-Singapore/"
        And I expect Media Data files to have all small included with correct sizepath set for each
    PASSED


step_definitions/test_product_api_steps.py::test_validate_media_data_images_should_have_correct_links_and_image_references[webpSmall] <- ..\myenv\lib\site-packages\pytest_bdd\scenario.py
Feature: Product GraphQL Tests
    Scenario: Validate Media Data Images Should have correct links and image references
        Given I have set API request endpoint to "https://traveller-core.dev.pelago.co/graphql" for getting product details
        When I am sending "POST" Request with "valid" payload and valid Product ID "phpv2"
        Then I expected All Products with "destinationId" set to "singapore" to have Media Data file webpSmall path under "https://traveller.dev.pelago.co/img/products/SG-Singapore/"
        And I expect Media Data files to have all webpSmall included with correct sizepath set for each
    PASSED


step_definitions/test_product_api_steps.py::test_validate_media_data_images_should_have_correct_links_and_image_references[medium] <- ..\myenv\lib\site-packages\pytest_bdd\scenario.py
Feature: Product GraphQL Tests
    Scenario: Validate Media Data Images Should have correct links and image references
        Given I have set API request endpoint to "https://traveller-core.dev.pelago.co/graphql" for getting product details
        When I am sending "POST" Request with "valid" payload and valid Product ID "phpv2"
        Then I expected All Products with "destinationId" set to "singapore" to have Media Data file medium path under "https://traveller.dev.pelago.co/img/products/SG-Singapore/"
        And I expect Media Data files to have all medium included with correct sizepath set for each
    PASSED


step_definitions/test_product_api_steps.py::test_validate_media_data_images_should_have_correct_links_and_image_references[webpMedium] <- ..\myenv\lib\site-packages\pytest_bdd\scenario.py
Feature: Product GraphQL Tests
    Scenario: Validate Media Data Images Should have correct links and image references
        Given I have set API request endpoint to "https://traveller-core.dev.pelago.co/graphql" for getting product details
        When I am sending "POST" Request with "valid" payload and valid Product ID "phpv2"
        Then I expected All Products with "destinationId" set to "singapore" to have Media Data file webpMedium path under "https://traveller.dev.pelago.co/img/products/SG-Singapore/"
        And I expect Media Data files to have all webpMedium included with correct sizepath set for each
    PASSED


step_definitions/test_product_api_steps.py::test_validate_media_data_images_should_have_correct_links_and_image_references[large] <- ..\myenv\lib\site-packages\pytest_bdd\scenario.py
Feature: Product GraphQL Tests
    Scenario: Validate Media Data Images Should have correct links and image references
        Given I have set API request endpoint to "https://traveller-core.dev.pelago.co/graphql" for getting product details
        When I am sending "POST" Request with "valid" payload and valid Product ID "phpv2"
        Then I expected All Products with "destinationId" set to "singapore" to have Media Data file large path under "https://traveller.dev.pelago.co/img/products/SG-Singapore/"
        And I expect Media Data files to have all large included with correct sizepath set for each
    PASSED


step_definitions/test_product_api_steps.py::test_validate_media_data_images_should_have_correct_links_and_image_references[webpLarge] <- ..\myenv\lib\site-packages\pytest_bdd\scenario.py
Feature: Product GraphQL Tests
    Scenario: Validate Media Data Images Should have correct links and image references
        Given I have set API request endpoint to "https://traveller-core.dev.pelago.co/graphql" for getting product details
        When I am sending "POST" Request with "valid" payload and valid Product ID "phpv2"
        Then I expected All Products with "destinationId" set to "singapore" to have Media Data file webpLarge path under "https://traveller.dev.pelago.co/img/products/SG-Singapore/"
        And I expect Media Data files to have all webpLarge included with correct sizepath set for each
    PASSED


step_definitions/test_product_api_steps.py::test_validate_media_data_images_should_have_correct_links_and_image_references[xlarge] <- ..\myenv\lib\site-packages\pytest_bdd\scenario.py
Feature: Product GraphQL Tests
    Scenario: Validate Media Data Images Should have correct links and image references
        Given I have set API request endpoint to "https://traveller-core.dev.pelago.co/graphql" for getting product details
        When I am sending "POST" Request with "valid" payload and valid Product ID "phpv2"
        Then I expected All Products with "destinationId" set to "singapore" to have Media Data file xlarge path under "https://traveller.dev.pelago.co/img/products/SG-Singapore/"
        And I expect Media Data files to have all xlarge included with correct sizepath set for each
    PASSED


step_definitions/test_product_api_steps.py::test_validate_media_data_images_should_have_correct_links_and_image_references[webpXlarge] <- ..\myenv\lib\site-packages\pytest_bdd\scenario.py
Feature: Product GraphQL Tests
    Scenario: Validate Media Data Images Should have correct links and image references
        Given I have set API request endpoint to "https://traveller-core.dev.pelago.co/graphql" for getting product details
        When I am sending "POST" Request with "valid" payload and valid Product ID "phpv2"
        Then I expected All Products with "destinationId" set to "singapore" to have Media Data file webpXlarge path under "https://traveller.dev.pelago.co/img/products/SG-Singapore/"
        And I expect Media Data files to have all webpXlarge included with correct sizepath set for each
    PASSED


step_definitions/test_product_api_steps.py::test_validate_longitude_latitude_fields_are_returning_valid_value <- ..\myenv\lib\site-packages\pytest_bdd\scenario.py
Feature: Product GraphQL Tests
    Scenario: Validate Longitude Latitude fields are returning valid value
        Given I have set API request endpoint to "https://traveller-core.dev.pelago.co/graphql" for getting product details
        When I am sending "POST" Request with "valid" payload and valid Product ID "phpv2"
        Then I expect API response parameter "location" to have VALID "latitude" and "longitude"
    PASSED


step_definitions/test_product_api_steps.py::test_validate_url_fields_has_no_broken_links <- ..\myenv\lib\site-packages\pytest_bdd\scenario.py
Feature: Product GraphQL Tests
    Scenario: Validate URL fields has No Broken Links
        Given I have set API request endpoint to "https://traveller-core.dev.pelago.co/graphql" for getting product details
        When I am sending "POST" Request with "valid" payload and valid Product ID "phpv2"
        Then I expect API response parameter "mapUrl" under "location" to have no broken links
        And I expect API response parameter "url" under "mediaData" to have no broken links
    PASSED


=================================================== Report Summary ====================================================
Total Test Duration: 11.06 seconds
Total Tests Collected: 24
Deselected Tests: 0
Passed Count: 24
Failed Count: 0
================================================ End of Report Summary ================================================
================================================= 24 passed in 11.06s =================================================

```
