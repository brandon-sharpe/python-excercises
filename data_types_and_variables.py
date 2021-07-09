#You have rented some movies for your kids: The little mermaid (for 3 days), 
#Brother Bear (for 5 days, they love it), and Hercules 
#(1 day, you don't know yet if they're going to like it).
# If price for a movie per day is 3 dollars, how much will you have to pay?

hercules=1
brother_bear = 5
little_mermaid = 3
price_per_day= 3
movie_rentals= ( hercules + brother_bear + little_mermaid)*price_per_day
print("$", + movie_rentals)

#Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook, 
# they pay you a different rate per hour. Google pays 400 dollars per hour, Amazon 380,
#  and Facebook 350. How much will you receive in payment for this week? 
# You worked 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon.
print()
g=400
a=380
f=350
print("$",(f*10)+(g*6)+(a*4))

#A student can be enrolled to a class only if the class is not full
# and the class schedule does not conflict with her current schedule.
print()
class_is_not_full = True
no_conflict = True
if class_is_not_full and no_conflict:
    print("Enroll in class")

#A product offer can be applied only if people buys more than 2 items, 
# and the offer has not expired. Premium members do not need to buy a 
# specific amount of products.

print()
more_than_two = True
not_expired = True 
premium_memeber = True
apply_offer=1
no_offer=0
if more_than_two and  not_expired or premium_memeber:
    apply_offer
    print("apply offer")
else:
    no_offer
    print("no offer")

