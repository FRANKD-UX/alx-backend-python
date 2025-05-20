Unittests and Integration Tests
This project focuses on unit testing and integration testing in Python. It demonstrates how to write tests using the unittest module with various techniques like mocking, patching, and parameterized testing.
Learning Objectives

The difference between unit and integration tests
Common testing patterns such as mocking, parametrizations and fixtures
How to write and execute tests using the unittest framework
How to utilize mock objects and patch decorators/context managers
How to parameterize tests and test classes
How to implement integration tests

Requirements

All files will be interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7
All files should end with a new line
All files must be executable
The first line of all files should be exactly #!/usr/bin/env python3
Code should use the pycodestyle style (version 2.5)
All modules, classes, and functions must have proper documentation
All functions must be type-annotated

Files

test_utils.py: Unit tests for the utils module functions
test_client.py: Unit and integration tests for the GithubOrgClient class

Tasks
0. Parameterize a unit test
Write tests for the access_nested_map function using parameterization.
1. Parameterize a unit test exception
Test exceptions raised by the access_nested_map function.
2. Mock HTTP calls
Test the get_json function by mocking HTTP calls.
3. Parameterize and patch
Test the memoize decorator functionality.
4. Parameterize and patch as decorators
Test the GithubOrgClient.org method using patch as a decorator.
5. Mocking a property
Test the private _public_repos_url property of the GithubOrgClient class.
6. More patching
Test the public_repos method of the GithubOrgClient class.
7. Parameterize
Test the has_license method with different inputs.
8. Integration test: fixtures
Create integration tests for the GithubOrgClient class using fixtures.
9. Integration tests
Implement integration tests for the public_repos method with and without a license filter.
