ratings=[5,3,3.5,4,4.5,3,3,4.5]

unique_ratings=set(ratings)
max_count=0
for rating in unique_ratings:
    count=ratings.count(rating)
    if count>max_count:
        max_count=count
        frequent=rating
print(frequent)        