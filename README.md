# Number-plate-detection

dataset1- !wget --header="Host: storage.googleapis.com" --header="User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36" --header="Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3" --header="Accept-Language: en-GB,en-US;q=0.9,en;q=0.8" --header="Referer: https://www.kaggle.com/" "https://storage.googleapis.com/kagglesdsdata/datasets/36674/55880/Indian_Number_plates.json?GoogleAccessId=web-data@kaggle-161607.iam.gserviceaccount.com&Expires=1575899280&Signature=pfqwJEhrAlwOVOclYCDODMMHBN8S9OO5PFhp0D9WOiX%2FT%2Bfm8x%2BzOFNGD7Iw%2BV%2BqCKHrh%2Bq769FGFP8%2BlvfK8alwQicZDoNj3NvDmoGFH6IgDsRKoWNtZfuYMrkOdbxs4%2FIAKm4ZlyR9uxUxnCbKTOA3RAKbdZL0%2BflDBUXcO%2F8LLuVoYVS5ff7QVc%2B8G1Qjt1JTv2mGfpIctRSW3UfyhsU%2BQelptCDhS1NxQmjJm7V3pHkUtdM4sTohrSQs7feXPKcHRaWH2EpFy0xKG7T5aXpXFhwFwIaiUJtxRlwSxAaeom3ne4a8XO5hNM%2BL5ljM4Tva0yhEf%2FZsXGEcMULekQ%3D%3D&response-content-disposition=attachment%3B+filename%3DIndian_Number_plates.json" -O "Indian_Number_plates.json" -c

dataset2 - !git clone https://github.com/openalpr/benchmarks.git

For openalpr dataset
the coordinates in txt file are formatted as - Left x, top y, the width of the plate, the height of the plate
