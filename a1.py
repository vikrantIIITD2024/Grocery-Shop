def show_menu():
    print("="*70)
    print("                             MY BAZAAR                  ")
    print("="*70)
    print("Hello! Welcome to my grocery store!")
    print("Following are the products available in the shop:")
    print("")
    print("-"*70)
    print("CODE     |   DESCRIPTION       |   CATEGORY        |  COST(Rs)          ")
    print("-"*70)
    print('''   0     |   Tshirt            | Apparels          | 500''')
    print('''   1     |   Trousers          | Apparels          | 600''')
    print('''   2     |   Scarf             | Apparels          | 250''')
    print('''   3     |   Smartphone        | Electronics       | 20,000''')
    print('''   4     |   iPad              | Electronics       | 30,000''')
    print('''   5     |   Laptop            | Electronics       | 50,000''')
    print('''   6     |   Eggs              | Eatables          | 5''')
    print('''   7     |   Chocolate         | Eatables          | 10''')
    print('''   8     |   Juice             | Eatables          | 100''')
    print('''   9     |   Milk              | Eatables          | 45''')
    print("-"*70)


def get_regular_input():
    print("")
    print("")
    print("-"*70)
    print("ENTER ITEMS YOU WISH TO BUY")
    print("-"*70)
    li = []
    item_codes = input("Enter the item codes (space-separated):")
    print('')
    print('')
    i_c = item_codes.split()
    c_0 = i_c.count("0")
    li.append(c_0)
    c_1 = i_c.count("1")
    li.append(c_1)
    c_2 = i_c.count("2")
    li.append(c_2)
    c_3 = i_c.count("3")
    li.append(c_3)
    c_4 = i_c.count("4")
    li.append(c_4)
    c_5 = i_c.count("5")
    li.append(c_5)
    c_6 = i_c.count("6")
    li.append(c_6)
    c_7 = i_c.count("7")
    li.append(c_7)
    c_8 = i_c.count("8")
    li.append(c_8)
    c_9 = i_c.count("9")
    li.append(c_9)
    for i in range(0,len(i_c)):
        if int(i_c[i]) < 0:
            print("Invalid")
    return li

def get_bulk_input():
    print("-"*70)
    print("ENTER ITEM AND QUANTITIES")
    print("-"*70)
    quan = [(0,'Tshirts'),(1,'Trousers'),(2,'Scarf'),(3,'Smartphone'),(4,'iPad'),(5,'Laptop'),(6,'Eggs'),(7,'Chocolate'),(8,'Juice'),(9,'Milk')]
    emp_list = [0,0,0,0,0,0,0,0,0,0]
    while True :
        ent = input("Enter code and quantity (leave blank to stop): ")
        if ent != '':
            code,quan_tity = map(int,ent.split())
            if code >= 0 and code <= 9 and quan_tity > 0:
                print(f"You added {quan_tity} {quan[code][1]} ")
            elif (code > 9 or code < 0) and quan_tity > 0 : 
                print("Invalid code. Try again.")
            elif (code > 9 or code < 0) and quan_tity < 0 :
                print("Invalid code and quantity. Try again.")
            elif (code > 9 or code < 0) and quan_tity == 0 :
                print("Buy atleast 1 quantity and enter valid code.")
            elif (code >= 0 and code <= 9) and quan_tity < 0:
                print("Invalid quantity. Try again.")
            elif (code >= 0 and code <= 9) and quan_tity == 0:
                print("Buy atleast 1 quantity")
            emp_list[code] = emp_list[code]+ quan_tity
        else :
            break
    print("Your order has been finalized. ")
    
        
    return emp_list



def print_order_details(quantities):
    print("-"*70)
    print("ORDER DETAILS")
    print("-"*70)
    products = ['Tshirt','Trousers','Scarf','Smartphone','iPad','Laptop','Eggs','Chocolate','Juice','Milk']
    products_cat = ['Apparel','Electronics','Eatables']
    p_prices = [500,600,250,20000,30000,50000,5,10,100,45]
    
    
    for i in range(0, len(p_prices)):
        if quantities[i] > 0:
            print(str(products[i])+ " x "+ str(quantities[i])+ ' = Rs '+ str(p_prices[i])+ ' * '+ str(quantities[i]) + ' = Rs'+ str(p_prices[i]*quantities[i]))
        else:
            print()

def calculate_category_wise_cost(quantities):
    print("-"*70)
    print("CATEGORY-WISE COST")
    print("-"*70)
    products_cat = ["Apparels","Electronics","Eatables"]
    p_prices = [500,600,250,20000,30000,50000,5,10,100,45]
    app_cost = 0
    elec_cost = 0
    eatables_cost = 0


    for i in range(0, len(quantities)):
        if i == 0 or i == 1 or i == 2 :
            app_cost += p_prices[i]*quantities[i] 
        elif i == 3 or i == 4 or i == 5 :
            elec_cost += p_prices[i]*quantities[i]
        elif i == 6 or i == 7 or i == 8 or i ==9 :
            eatables_cost += p_prices[i]*quantities[i]
    print("Apparels = Rs " + str(app_cost))
    print("Electronics = Rs "+ str(elec_cost))
    print("Eatables = Rs "+ str(eatables_cost))
    lis =(app_cost,elec_cost,eatables_cost)
    return lis

def get_discount(cost, discount_rate):

	return int(cost * discount_rate)


def calculate_discounted_prices(apparels_cost, electronics_cost, eatables_cost):
    print("-"*70)
    print("DISCOUNTS")
    print("-"*70)
    if apparels_cost >= 2000 :
        dis_price_of_app = get_discount(apparels_cost,0.10)
        apparels_cost_1= apparels_cost - dis_price_of_app
        print("[APPAREL] Rs "+str(apparels_cost)+"- Rs "+str(dis_price_of_app)+ "= Rs "+str(apparels_cost_1))
    else:
        dis_price_of_app = 0
        apparels_cost_1 = apparels_cost

    if electronics_cost >= 25000:
        dis_price_of_elec = get_discount(electronics_cost,0.10)
        electronics_cost_1 = electronics_cost - dis_price_of_elec
        print("[ELECTRONICS] Rs "+str(electronics_cost)+"- Rs "+str(dis_price_of_elec)+ "= Rs "+str(electronics_cost_1))
    else:
        dis_price_of_elec=0
        electronics_cost_1 = electronics_cost
    if eatables_cost >= 500:
        dis_price_of_eat = get_discount(eatables_cost,0.10)
        eatables_cost_1 = eatables_cost - dis_price_of_eat
        print("[EATABLES] Rs "+str(eatables_cost)+"- Rs "+str(dis_price_of_eat)+ "= Rs "+str(eatables_cost_1))
    else:
        dis_price_of_eat = 0
        eatables_cost_1 = eatables_cost
    print("")
    print("Total Discount = "+str(dis_price_of_app + dis_price_of_elec + dis_price_of_eat))
    print("Total Cost = "+str(apparels_cost_1 + electronics_cost_1 + eatables_cost_1))
    l = (apparels_cost_1,electronics_cost_1,eatables_cost_1)
    return l

def get_tax(cost, tax):

	return int(cost * tax)

def calculate_tax(apparels_cost, electronics_cost, eatables_cost):
    print("-"*70)
    print("TAX")
    print("-"*70)
    if apparels_cost > 1 or eatables_cost == 0 :
        tax_price_of_app = get_tax(apparels_cost,0.10)
        apparels_tax = tax_price_of_app
        print("[1] [APPAREL] Rs "+str(apparels_cost) +"* 0.10 = Rs "+str(apparels_tax))
    if electronics_cost > 1 or electronics_cost == 0:
        tax_price_of_elec = get_tax(electronics_cost,0.15)
        elec_tax = tax_price_of_elec
        print("[2] [ELECTRONICS] Rs "+ str(electronics_cost)+"* 0.15 = Rs "+ str(elec_tax))
    if eatables_cost > 1 or eatables_cost == 0 :
        tax_price_of_eat = get_tax(eatables_cost,0.05)
        eat_tax = tax_price_of_eat
        print("[3] [EATABLES] Rs "+ str(eatables_cost)+"* 0.05 = Rs "+ str(eat_tax))
    x = apparels_tax + elec_tax + eat_tax
    y = apparels_cost + electronics_cost + eatables_cost + apparels_tax + elec_tax + eat_tax
    print("")
    print('TOTAL TAX = Rs '+ str(x) )
    print('TOTAL COST = Rs '+str(y))
    calculated_tax = (y,x)
    return calculated_tax


def apply_coupon_code(total_cost):
    
    print("-"*70)
    print("COUPON CODE")
    print("-"*70)
    
    coupon_code = input("Enter coupon code(else leave blank):")
    while True:
        if coupon_code == " ":
            break
            print("No coupon code applied.")
        
        elif coupon_code == "HELLE25" and total_cost >= 25000:
            print("[HELLE25] " + "min(5000, Rs " + str(total_cost)+" * " + str(0.25) + ")  = Rs "+str(min(5000, get_discount(total_cost,0.25))) )
            total_coupon_discount = min(5000, get_discount(total_cost,0.25))
            print("")
            print("TOTAL COST = Rs "+ str(total_cost-min(5000, get_discount(total_cost,0.25))))
            total_cost_after_discount = total_cost-min(5000, get_discount(total_cost,0.25))
            break

        elif coupon_code == "CHILL50" and total_cost >= 50000:
            print("[CHILL50]"+ "min(10000, Rs " + str(total_cost) + " * " + str(0.50) + ") = Rs " + str(min(10000,get_discount(total_cost,0.50))))
            total_coupon_discount = min(10000,get_discount(total_cost,0.50))
            print("")
            print("TOTAL COST = Rs "+ str(total_cost-min(10000, get_discount(total_cost,0.50))))
            total_cost_after_discount = total_cost-min(10000, get_discount(total_cost,0.50))

            break

        else:
            
            print("Invalid coupon code. Try again.")
            coupon_code = input("Enter coupon code(else leave blank)")
            total_coupon_discount = 0
            print("TOTAL COUPON DISCOUNT = Rs "+ str(total_coupon_discount))
            print("")
            print("TOTAL COST = Rs "+ str(total_cost))
            total_cost_after_discount = total_cost

            break
    return (total_cost_after_discount,total_coupon_discount)

def main():
    show_menu()
    buy_bulk = input("Would you like to buy in bulkCH?(y or Y / n or N):\n")
    if buy_bulk=="y" or buy_bulk=="Y" :
        value = get_bulk_input()
    elif buy_bulk=="n" or buy_bulk=="N":
        value = get_regular_input()
    else:
        buy_bulk = input("Would you like to buy in bulk?(y or Y / n or N):")
    print_order_details(value)
    var_1 = calculate_category_wise_cost(value)
    var_2 = calculate_discounted_prices(var_1[0], var_1[1], var_1[2])
    var_3 = calculate_tax(var_2[0],var_2[1],var_2[2])
    apply_coupon_code(var_3[1])
    print("Thank You for Visiting!")
if __name__ == '__main__':
    main()




