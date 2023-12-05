def map(inputs, output_maps):
    outputs = []
    for input in inputs:
        is_in_map = False
        for output_map in output_maps:
            dest_start, source_start, range_length = output_map
            if source_start <= input < source_start + range_length:
                outputs.append(dest_start + input - source_start)
                is_in_map = True
                break
        if not is_in_map:
            outputs.append(input)
    return outputs


lines = []
with open("input.txt") as file:
    lines.extend(file.readlines())

seeds = [int(s) for s in lines[0].replace("seeds:", "").strip().split(" ")]
seeds_to_soil = [[int(c) for c in l.strip().split(" ")] for l in lines[3:31]]
soil_to_fertilizer = [[int(c) for c in l.strip().split(" ")] for l in lines[33:43]]
fertilizer_to_water = [[int(c) for c in l.strip().split(" ")] for l in lines[45:54]]
water_to_light = [[int(c) for c in l.strip().split(" ")] for l in lines[56:79]]
light_to_temperature = [[int(c) for c in l.strip().split(" ")] for l in lines[81:113]]
temperature_to_humidity = [[int(c) for c in l.strip().split(" ")] for l in lines[115:160]]
humidity_to_location = [[int(c) for c in l.strip().split(" ")] for l in lines[162:211]]

print("soils")
soils = map(seeds, seeds_to_soil)
print("fertilizers")
fertilizers = map(soils, soil_to_fertilizer)
print("waters")
waters = map(fertilizers, fertilizer_to_water)
print("lights")
lights = map(waters, water_to_light)
print("temperatures")
temperatures = map(lights, light_to_temperature)
print("humidities")
humidities = map(temperatures, temperature_to_humidity)
print("location")
location = map(humidities, humidity_to_location)
print(min(location))
