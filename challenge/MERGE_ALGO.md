The following details the algorithm for extracting and merging contact details from multiple sources.

1. Iterate through the companies
     Subiterate through the response sources
       Subiterate through the unique combinations of response sources
   
2.a. If two names are equivalent, mark to merge
  b. If two phone numbers are equivalent, and names are not different, mark to merge
  c. If forename initial & surname and email match, mark to merge

3. Increase confidence score based on quantity of marks to merge (ignore provider_confidence as there is no calibration)


