from tools import (
    calculate,
    multiply,
    subtract,
    divide,
    calculate_percentage,
    get_current_datetime,
    convert_units,
    get_weather,
    web_search,
)


print("=" * 50)
print("TESTING CALCULATOR TOOLS")
print("=" * 50)

print("Calculate:", calculate(10, 20))
print("Multiply:", multiply(10, 20))
print("Subtract:", subtract(20, 10))
print("Divide:", divide(20, 5))
print("Percentage:", calculate_percentage(200, 10))


print("\n" + "=" * 50)
print("TESTING DATE/TIME")
print("=" * 50)

print("Date/Time:", get_current_datetime())


print("\n" + "=" * 50)
print("TESTING UNIT CONVERSION")
print("=" * 50)

print("KM to Miles:", convert_units(10, "km", "miles"))
print("KG to Pounds:", convert_units(10, "kg", "lb"))


print("\n" + "=" * 50)
print("TESTING WEATHER")
print("=" * 50)

try:
    weather = get_weather("Lahore")
    print(weather)

except Exception as e:
    print("Weather Error:", e)


print("\n" + "=" * 50)
print("TESTING WEB SEARCH")
print("=" * 50)

try:
    search_result = web_search("latest artificial intelligence news")
    print(search_result)

except Exception as e:
    print("Web Search Error:", e)