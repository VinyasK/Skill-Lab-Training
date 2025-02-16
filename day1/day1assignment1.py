sales_list=[2000,3000,5500,7000,6400,10000,9999]

highest_sale=max(sales_list)

index=sales_list.index(highest_sale)

print("Day {} has highest sales of {}".format(index+1,highest_sale))