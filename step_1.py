from data import products_string

def transform_products_to_list(products_string):
    products_splote = products_string.split('\n')
    products_list = []
    
    for product in products_splote:
        if product:#basically if product exists
            clean_product = product.split(',')
            products_list.append(clean_product)
            
    return products_list


the_list = transform_products_to_list(products_string)

white = the_list[0][2][:6]

#this method to get the word white in the line above or it all split out below

first_item_in_the_list = the_list[0]
#print(first_item_in_the_list)

third_index_in_the_next_list = first_item_in_the_list[2]
#print(third_index_in_the_next_list)

just_the_word_white = third_index_in_the_next_list[0:6]
