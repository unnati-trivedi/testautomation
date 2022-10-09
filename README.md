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
  - Tests individual response parameters to have expected values, it falls expected value range, positive/negative type, and i
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

**Running tests with tags from [`regression`,`smoke`]**
in ~/testautomation
```sh
pytest --gherkin-terminal-reporter -vv -m regression
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
Feature: Product Browsing
    Scenario: Valid POST Request with Valid existing product ID
        Given I set POST endpoint to "https://traveller-core.dev.pelago.co/graphql" for getting product details
        When I am sending POST Request with valid Product IDs phpv2
        Then results are shown with success "200"
        And I expect response body of this request to be NON-EMPTY with "product" details
        And I expect API response "productId" to have correct value as phpv2
    PASSED


step_definitions/test_product_api_steps.py::test_valid_post_request_with_nonexisting_product_id[UNREAL] <- ..\myenv\lib\site-packages\pytest_bdd\scenario.py
Feature: Product Browsing
    Scenario: Valid POST Request with non-existing product ID
        Given I set POST endpoint to "https://traveller-core.dev.pelago.co/graphql" for getting product details
        When I am sending POST Request with valid Product IDs UNREAL
        Then results are shown with success "200"
        And I expect response body of this request to be EMPTY with no "product" details
    PASSED


step_definitions/test_product_api_steps.py::test_valid_post_request_with_nonexisting_product_id[123456] <- ..\myenv\lib\site-packages\pytest_bdd\scenario.py
Feature: Product Browsing
    Scenario: Valid POST Request with non-existing product ID
        Given I set POST endpoint to "https://traveller-core.dev.pelago.co/graphql" for getting product details
        When I am sending POST Request with valid Product IDs 123456
        Then results are shown with success "200"
        And I expect response body of this request to be EMPTY with no "product" details
    PASSED


step_definitions/test_product_api_steps.py::test_valid_post_request_with_empty_product_id <- ..\myenv\lib\site-packages\pytest_bdd\scenario.py
Feature: Product Browsing
    Scenario: Valid POST Request with EMPTY product ID
        Given I set POST endpoint to "https://traveller-core.dev.pelago.co/graphql" for getting product details
        When I am sending POST Request with blank Product ID " "
        Then results are shown with success "200"
        And I expect response body of this request to be EMPTY with no "product" details
    PASSED


step_definitions/test_product_api_steps.py::test_valid_post_request_with_invalid_payload <- ..\myenv\lib\site-packages\pytest_bdd\scenario.py
Feature: Product Browsing
    Scenario: Valid POST Request with INVALID payload
        Given I set POST endpoint to "https://traveller-core.dev.pelago.co/graphql" for getting product details
        When I am sending POST Request with "invalid" payload and "INCORRECTFIELD"
        Then results are shown with error code "400" and with proper error message describing error in "INCORRECTFIELD"
    PASSED


step_definitions/test_product_api_steps.py::test_valid_post_request_with_valid_existing_product_id_should_return_correct_response_schema <- ..\myenv\lib\site-packages\pytest_bdd\scenario.py
Feature: Product Browsing
    Scenario: Valid POST Request with Valid existing product ID should return Correct Response Schema
        Given I set POST endpoint to "https://traveller-core.dev.pelago.co/graphql" for getting product details
        When I am sending POST Request with valid Product ID "phpv2"
        Then I expect API response content to have Correct Json Schema
    PASSED


step_definitions/test_product_api_steps.py::test_valid_post_request_with_valid_existing_product_id_should_return_correct_response_headers <- ..\myenv\lib\site-packages\pytest_bdd\scenario.py
Feature: Product Browsing
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
    PASSED


step_definitions/test_product_api_steps.py::test_valid_post_request_with_valid_existing_product_id_should_return_expected_response_parameters <- ..\myenv\lib\site-packages\pytest_bdd\scenario.py <class 'str'>
<class 'str'>

Feature: Product Browsing
    Scenario: Valid POST Request with Valid existing product ID should return expected response parameters
        Given I set POST endpoint to "https://traveller-core.dev.pelago.co/graphql" for getting product details
        When I am sending POST Request with valid Product ID "phpv2"
        Then I expect API response "duration" to have correct value "2 - 3 Hours"
    PASSED


step_definitions/test_product_api_steps.py::test_valid_post_request_with_valid_existing_product_id_should_have_response_param_values_from_valid_value_range <- ..\myenv\lib\site-packages\pytest_bdd\scenario.py
Feature: Product Browsing
    Scenario: Valid POST Request with Valid existing product ID should have response param values from VALID Value range
        Given I set POST endpoint to "https://traveller-core.dev.pelago.co/graphql" for getting product details
        When I am sending POST Request with valid Product ID "phpv2"
        Then I expect API response "cancellationType" to be one of these "NO_CANCELLATION OR  OR ALLOWED_CANCELLATION OR CONDITIONAL_CANCELLATION"
        And I expect API response "destinationId" to be one of these "singapore OR india"
        And I expect API response "confirmationType" to be one of these "MANUAL OR AUTOMATED"
        And I expect API response "voucherType" to be one of these "EXTERNAL OR PELAGO"
    PASSED


step_definitions/test_product_api_steps.py::test_cancellation_window_checks <- ..\myenv\lib\site-packages\pytest_bdd\scenario.py
Feature: Product Browsing
    Scenario: Cancellation Window checks
        Given I set POST endpoint to "https://traveller-core.dev.pelago.co/graphql" for getting product details
        When I am sending POST Request with valid Product ID "phpv2"
        Then For Product that has "cancellationType" set to "NO_CANCELLATION", I expect API response "cancellationWindow" to be "0"
        Then For Product that has "cancellationType" set to "NO_CANCELLATION", I expect API response "cancellationWindowText" to show "No Cancellation Allowed"
    PASSED


step_definitions/test_product_api_steps.py::test_price_range_tests <- ..\myenv\lib\site-packages\pytest_bdd\scenario.py
Feature: Product Browsing
    Scenario: Price Range Tests
        Given I set POST endpoint to "https://traveller-core.dev.pelago.co/graphql" for getting product details
        When I am sending POST Request with valid Product ID "phpv2"
        Then I expect API response "priceRangeFrom" to be "positive" number
        And I expect API response "priceRangeTo" to be greater than "priceRangeFrom"
    PASSED


step_definitions/test_product_api_steps.py::test_media_data_images_should_have_correct_path_and_image_references[xsmall] <- ..\myenv\lib\site-packages\pytest_bdd\scenario.py
Feature: Product Browsing
    Scenario: Media Data Images Should have correct path and image references
        Given I set POST endpoint to "https://traveller-core.dev.pelago.co/graphql" for getting product details
        When I am sending POST Request with valid Product ID "phpv2"
        Then I expected All Products with "destinationId" set to "singapore" to have Media Data file xsmall path under "https://traveller.dev.pelago.co/img/products/SG-Singapore/"
        And I expect Media Data files to have all xsmall included with correct sizepath set for each
    PASSED


step_definitions/test_product_api_steps.py::test_media_data_images_should_have_correct_path_and_image_references[webpXsmall] <- ..\myenv\lib\site-packages\pytest_bdd\scenario.py
Feature: Product Browsing
    Scenario: Media Data Images Should have correct path and image references
        Given I set POST endpoint to "https://traveller-core.dev.pelago.co/graphql" for getting product details
        When I am sending POST Request with valid Product ID "phpv2"
        Then I expected All Products with "destinationId" set to "singapore" to have Media Data file webpXsmall path under "https://traveller.dev.pelago.co/img/products/SG-Singapore/"
        And I expect Media Data files to have all webpXsmall included with correct sizepath set for each
    PASSED


step_definitions/test_product_api_steps.py::test_media_data_images_should_have_correct_path_and_image_references[small] <- ..\myenv\lib\site-packages\pytest_bdd\scenario.py
Feature: Product Browsing
    Scenario: Media Data Images Should have correct path and image references
        Given I set POST endpoint to "https://traveller-core.dev.pelago.co/graphql" for getting product details
        When I am sending POST Request with valid Product ID "phpv2"
        Then I expected All Products with "destinationId" set to "singapore" to have Media Data file small path under "https://traveller.dev.pelago.co/img/products/SG-Singapore/"
        And I expect Media Data files to have all small included with correct sizepath set for each
    PASSED


step_definitions/test_product_api_steps.py::test_media_data_images_should_have_correct_path_and_image_references[webpSmall] <- ..\myenv\lib\site-packages\pytest_bdd\scenario.py
Feature: Product Browsing
    Scenario: Media Data Images Should have correct path and image references
        Given I set POST endpoint to "https://traveller-core.dev.pelago.co/graphql" for getting product details
        When I am sending POST Request with valid Product ID "phpv2"
        Then I expected All Products with "destinationId" set to "singapore" to have Media Data file webpSmall path under "https://traveller.dev.pelago.co/img/products/SG-Singapore/"
        And I expect Media Data files to have all webpSmall included with correct sizepath set for each
    PASSED


step_definitions/test_product_api_steps.py::test_media_data_images_should_have_correct_path_and_image_references[medium] <- ..\myenv\lib\site-packages\pytest_bdd\scenario.py
Feature: Product Browsing
    Scenario: Media Data Images Should have correct path and image references
        Given I set POST endpoint to "https://traveller-core.dev.pelago.co/graphql" for getting product details
        When I am sending POST Request with valid Product ID "phpv2"
        Then I expected All Products with "destinationId" set to "singapore" to have Media Data file medium path under "https://traveller.dev.pelago.co/img/products/SG-Singapore/"
        And I expect Media Data files to have all medium included with correct sizepath set for each
    PASSED


step_definitions/test_product_api_steps.py::test_media_data_images_should_have_correct_path_and_image_references[webpMedium] <- ..\myenv\lib\site-packages\pytest_bdd\scenario.py
Feature: Product Browsing
    Scenario: Media Data Images Should have correct path and image references
        Given I set POST endpoint to "https://traveller-core.dev.pelago.co/graphql" for getting product details
        When I am sending POST Request with valid Product ID "phpv2"
        Then I expected All Products with "destinationId" set to "singapore" to have Media Data file webpMedium path under "https://traveller.dev.pelago.co/img/products/SG-Singapore/"
        And I expect Media Data files to have all webpMedium included with correct sizepath set for each
    PASSED


step_definitions/test_product_api_steps.py::test_media_data_images_should_have_correct_path_and_image_references[large] <- ..\myenv\lib\site-packages\pytest_bdd\scenario.py
Feature: Product Browsing
    Scenario: Media Data Images Should have correct path and image references
        Given I set POST endpoint to "https://traveller-core.dev.pelago.co/graphql" for getting product details
        When I am sending POST Request with valid Product ID "phpv2"
        Then I expected All Products with "destinationId" set to "singapore" to have Media Data file large path under "https://traveller.dev.pelago.co/img/products/SG-Singapore/"
        And I expect Media Data files to have all large included with correct sizepath set for each
    PASSED


step_definitions/test_product_api_steps.py::test_media_data_images_should_have_correct_path_and_image_references[webpLarge] <- ..\myenv\lib\site-packages\pytest_bdd\scenario.py
Feature: Product Browsing
    Scenario: Media Data Images Should have correct path and image references
        Given I set POST endpoint to "https://traveller-core.dev.pelago.co/graphql" for getting product details
        When I am sending POST Request with valid Product ID "phpv2"
        Then I expected All Products with "destinationId" set to "singapore" to have Media Data file webpLarge path under "https://traveller.dev.pelago.co/img/products/SG-Singapore/"
        And I expect Media Data files to have all webpLarge included with correct sizepath set for each
    PASSED


step_definitions/test_product_api_steps.py::test_media_data_images_should_have_correct_path_and_image_references[xlarge] <- ..\myenv\lib\site-packages\pytest_bdd\scenario.py
Feature: Product Browsing
    Scenario: Media Data Images Should have correct path and image references
        Given I set POST endpoint to "https://traveller-core.dev.pelago.co/graphql" for getting product details
        When I am sending POST Request with valid Product ID "phpv2"
        Then I expected All Products with "destinationId" set to "singapore" to have Media Data file xlarge path under "https://traveller.dev.pelago.co/img/products/SG-Singapore/"
        And I expect Media Data files to have all xlarge included with correct sizepath set for each
    PASSED


step_definitions/test_product_api_steps.py::test_media_data_images_should_have_correct_path_and_image_references[webpXlarge] <- ..\myenv\lib\site-packages\pytest_bdd\scenario.py
Feature: Product Browsing
    Scenario: Media Data Images Should have correct path and image references
        Given I set POST endpoint to "https://traveller-core.dev.pelago.co/graphql" for getting product details
        When I am sending POST Request with valid Product ID "phpv2"
        Then I expected All Products with "destinationId" set to "singapore" to have Media Data file webpXlarge path under "https://traveller.dev.pelago.co/img/products/SG-Singapore/"
        And I expect Media Data files to have all webpXlarge included with correct sizepath set for each
    PASSED


step_definitions/test_product_api_steps.py::test_longitude_latitude <- ..\myenv\lib\site-packages\pytest_bdd\scenario.py
Feature: Product Browsing
    Scenario: Longitude Latitude
        Given I set POST endpoint to "https://traveller-core.dev.pelago.co/graphql" for getting product details
        When I am sending POST Request with valid Product ID "phpv2"
        Then I expect API response parameter "location" to have VALID "latitude" and "longitude"
    PASSED


step_definitions/test_product_api_steps.py::test_no_broken_links <- ..\myenv\lib\site-packages\pytest_bdd\scenario.py
Feature: Product Browsing
    Scenario: No Broken Links
        Given I set POST endpoint to "https://traveller-core.dev.pelago.co/graphql" for getting product details
        When I am sending POST Request with valid Product ID "phpv2"
        Then I expect API response parameter "mapUrl" under "location" to have no broken links
        And I expect API response parameter "url" under "mediaData" to have no broken links
    PASSED


================================================================================================= Report Summary =================================================================================================
Total Test Duration: 11.50 seconds
Total Tests Collected: 23
Deselected Tests: 0
Passed Count: 23
Failed Count: 0
============================================================================================= End of Report Summary ==============================================================================================
============================================================================================== 23 passed in 11.53s ===============================================================================================

```
