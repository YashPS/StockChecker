> 'Necessity is the mother of invention' - Mahatma Gandhi
# STOCK CHECKER with TELEGRAM NOTIFICATION INTEGRATION
#### by Yash Pratap Singh
*Setup telegram to receive notifications when your item is in stock! (recommend you to Google through this setup)*

*Capable of checking websites with dynamic changes after loading, using Chrome-driver of Selenium*


## HOW TO USE

1. Add a 'config' directory, create a 'config.yaml' file

2. Insert the following into the yaml file -
```yaml
token: <your_telegram_bot_token>
chat_id: <your_telegram_chat_id>
request_url: <product_url>
test_url: <url_of_product_in_stock{for testing only}> 
item_name: <display_name_for_telegram_notification>
class_name: <class_identifier_to_find_in_request_url_html>
check_phrase: <unique_text_in_out_of_stock_page{something like 'out of stock'}> 
```

3. Run checker.py

4. Thank me if it works

5. ... it didn't work... Well... 


6. We are on a rock floating in expanding nothingness... 




7. *It'll work out at the end. :)*
