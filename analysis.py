gallon_in_litres = 3.785411784
mile_in_km = 1.60934


def choose_metrics():
    metric = input("Choose your metric - (1) EU, (2) British: ")
    try:
        assert int(metric) == 1 or int(metric) == 2
    except:
        raise TypeError("Enter 1 for EU or 2 for British")
    return int(metric)


def get_inputs(metric):
    initial_price = input("Enter initial price of the car: ")
    annual_kilometrage = input("How many kms will you drive annually?: ")

    if metric == 1:
        gas_price = input("Enter average gas price (EU/litre): ")
        fuel_consumption = input("Enter fuel consumption (# litres/100km): ")
    else:
        gas_price = input("Enter average gas price (GBP/litre): ")
        fuel_consumption = input("Enter fuel consumption (# miles / gallon): ")

    annual_repairs = input("How much will you on average spend annually" + 
                            " on repairs?: ")
    annual_insurance = input("How much will you on average spend annually" + 
                            " on car insurance?: ")
    monthly_parking = input("How much do you spend monthly for parking?: ")
    duration = input("How many years would you like to keep the car for?: ")
    sell_price = input("What is the estimated price of the car when you sell it?: ")
    agent_fees = input("How much are the agent (or any ambigious) fees?: ")

    return float(initial_price), float(annual_kilometrage), float(gas_price), \
        float(fuel_consumption), float(annual_repairs), \
        float(annual_insurance), float(monthly_parking), float(duration), \
        float(sell_price), float(agent_fees)


def calculate_european_cost(metric,
                         initial_price,
                         annual_distance,
                         gas_price,
                         fuel_consumption,
                         annual_repairs,
                         annual_insurance,
                         monthly_parking,
                         duration,
                         sell_price,
                           agent_fees=0):
    parking_cost = monthly_parking * 12 * duration
    repair_cost  = annual_repairs * duration
    insurance_cost = annual_insurance * duration

    if metric == 1:
        gas_cost = calculate_eu_gas_cost(annual_distance, gas_price, fuel_consumption)
    else:
        gas_cost = calculate_uk_gas_cost(annual_distance, gas_price, fuel_consumption)

    total_cost = initial_price + parking_cost + repair_cost + insurance_cost + \
        gas_cost - sell_price + agent_fees
    annual_cost = total_cost / duration
    
    distance_cost = total_cost / (annual_distance * duration)
    
    return total_cost, annual_cost, distance_cost


def calculate_eu_gas_cost(annual_kilometrage, gas_price, fuel_consumption):
    return annual_kilometrage * gas_price * fuel_consumption / 100


def calculate_uk_gas_cost(annual_milage, gas_price, fuel_consumption):
    annual_kilometrage = annual_milage * mile_in_km
    fuel_consumption = fuel_consumption * mile_in_km / gallon_in_litres    
    return annual_kilometrage * gas_price * fuel_consumption


def main():
    metric = choose_metrics()

    initial_price, annual_kilometrage, gas_price, fuel_consumption, \
    annual_repairs, annual_insurance, monthly_parking, duration, \
    sell_price, agent_fees = get_inputs(metric)

    total_cost, annual_cost, distnace_cost = calculate_european_cost( \
                        initial_price,
                        annual_kilometrage,
                        gas_price,
                        fuel_consumption,
                        annual_repairs,
                        annual_insurance,
                        monthly_parking,
                        duration,
                        sell_price,
                        agent_fees)
    
    print(f'Total cost: {total_cost}')
    print(f'Annual cost: {annual_cost}')
    if metric == 1:
        print(f'Cost per km: {distnace_cost}')
    else:
        print(f'Cost per mile: {distnace_cost}')


main()