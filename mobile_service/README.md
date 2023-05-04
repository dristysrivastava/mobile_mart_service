**Mobile Service**

Consider an app which allows users to see all the mobile phones available in
the Indian market. Users can filter the list based on different criteria such as
Brand, Model, Colour, Price and can also sort the list based on price in
ascending or descending order.
Create REST APIs using Django which will serve as a backed for this app. The
backed should have the following APIs
    1. API to authenticate user(Login)
    2. API to add mobile devices(only for Authenticated User). API should save the following details:
          i. Brand
          ii. Model
          iii. Colour
          iv. Price
    3. API to delete mobile devices(only for Authenticated User)
    4. API to list all phones
    5. API to list all phones with filters(filter by Brand,Model,Colour)
    6. API to list all phones with price range
    7. API to list all phones in ascending or descending order based on user input. 