Scenario: Verify successful user signup
  Given the user is on the signup page
  When the user enters valid signup details
  And clicks on the create account button
  Then the user should be registered successfully

Scenario: Signup with an already registered email
  Given the user is on the signup page
  When the user enters an already registered email
  And clicks on the create account button
  Then an error message should be displayed

Scenario: Signup with an invalid email format
  Given the user is on the signup page
  When the user enters an invalid email format
  And clicks on the create account button
  Then an error message should be displayed

Scenario: Signup with an weak password
  Given the user is on the signup page
  When the user enters a weak password
  And clicks on the create account button
  Then an error message should be displayed

Scenario: Signup with missing required fields
  Given the user is on the signup page
  When the user leaves required fields empty
  And clicks on the create account button
  Then an error message should be displayed


