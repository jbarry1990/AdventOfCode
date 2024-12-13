import re

def ReadFile(filename):
    with open(filename, "r") as f:
        content = f.readlines()
        stripped_content = []
        for line in content:
            stripped_content.append(line.strip())
        return stripped_content

def GenerateSeedNumberRange(sourceSeedRange, Map):
    seeds = sourceSeedRange
    new_seeds = []
    while len(seeds) != 0:
        s,e = seeds.pop()
        for a,b,c in Map:
            os = max(s,b)
            oe = min(e,(b+c))
            if os < oe:
                new_seeds.append((os-b+a,oe-b+a))
                if os > s:
                    sourceSeedRange.append((s,os))
                if oe < e:
                    sourceSeedRange.append((oe, e))
                break
        else:
            new_seeds.append((s,e))
    return new_seeds

    for num in Map:
        if num[1]<= sourceSeedNum < num[1]+num[2]:
            sourceSeedNum = num[0] + (sourceSeedNum-num[1])
            break
    return sourceSeedNum

def GenerateSeedNumber(sourceSeedNum, Map):
    for num in Map:
        if num[1]<= sourceSeedNum < num[1]+num[2]:
            sourceSeedNum = num[0] + (sourceSeedNum-num[1])
            break
    return sourceSeedNum
            
        

def PartASolve(file_contents):
    seeds = [int(n) for n in file_contents[0].split(":")[1].split()]
    maps = []
    start = 3
    end = 3
    while end != len(file_contents):
        end = file_contents.index("",start) if "" in file_contents[start:] else -1
        if end == -1:
            end = len(file_contents)
        maps.append(file_contents[start:end])
        start = end+2

    seed_to_soil = [[int(n) for n in x.split()]for x in maps[0]]
    soil_to_fertilizer = [[int(n) for n in x.split()]for x in maps[1]]
    fertilizer_to_water = [[int(n) for n in x.split()]for x in maps[2]]
    water_to_light = [[int(n) for n in x.split()]for x in maps[3]]
    light_to_temp = [[int(n) for n in x.split()]for x in maps[4]]
    temp_to_humidity = [[int(n) for n in x.split()]for x in maps[5]]
    humidity_to_location = [[int(n) for n in x.split()]for x in maps[6]]

    info = []
    locations = []
    for seed in seeds:
        soil_num = -1
        fertilizer_num = -1
        water_num = -1
        light_num = -1
        temp_num = -1
        humidity_num = -1
        location_num = -1

        soil_num = GenerateSeedNumber(seed,seed_to_soil)
        if soil_num == -1:
            soil_num = seed
        fertilizer_num = GenerateSeedNumber(soil_num, soil_to_fertilizer)
        water_num = GenerateSeedNumber(fertilizer_num, fertilizer_to_water)
        light_num = GenerateSeedNumber(water_num, water_to_light)
        temp_num = GenerateSeedNumber(light_num, light_to_temp)
        humidity_num = GenerateSeedNumber(temp_num, temp_to_humidity)
        location_num = GenerateSeedNumber(humidity_num, humidity_to_location)

        info.append([seed, soil_num, fertilizer_num, water_num, light_num, temp_num, humidity_num, location_num])
        locations.append(location_num)        
    
    return min(locations)
                
def PartBSolve(file_contents):
    seed_ranges = [int(n) for n in file_contents[0].split(":")[1].split()]
    maps = []
    start = 3
    end = 3
    while end != len(file_contents):
        end = file_contents.index("",start) if "" in file_contents[start:] else -1
        if end == -1:
            end = len(file_contents)
        maps.append(file_contents[start:end])
        start = end+2

    seed_to_soil = [[int(n) for n in x.split()]for x in maps[0]]
    soil_to_fertilizer = [[int(n) for n in x.split()]for x in maps[1]]
    fertilizer_to_water = [[int(n) for n in x.split()]for x in maps[2]]
    water_to_light = [[int(n) for n in x.split()]for x in maps[3]]
    light_to_temp = [[int(n) for n in x.split()]for x in maps[4]]
    temp_to_humidity = [[int(n) for n in x.split()]for x in maps[5]]
    humidity_to_location = [[int(n) for n in x.split()]for x in maps[6]]

    seeds = []
    for i in range(0,len(seed_ranges),2):
        seeds.append((seed_ranges[i],seed_ranges[i]+seed_ranges[i+1]-1))
            
    info = []
    locations = []
    for seed in seeds:
        soil_num = -1
        fertilizer_num = -1
        water_num = -1
        light_num = -1
        temp_num = -1
        humidity_num = -1
        location_num = -1

        soil_num = GenerateSeedNumberRange([seed],seed_to_soil)
        fertilizer_num = GenerateSeedNumberRange(soil_num, soil_to_fertilizer)
        water_num = GenerateSeedNumberRange(fertilizer_num, fertilizer_to_water)
        light_num = GenerateSeedNumberRange(water_num, water_to_light)
        temp_num = GenerateSeedNumberRange(light_num, light_to_temp)
        humidity_num = GenerateSeedNumberRange(temp_num, temp_to_humidity)
        location_num = GenerateSeedNumberRange(humidity_num, humidity_to_location)

        locations.append(location_num)        

    minimum = 100000000000000
    for location in locations:
        for loc in location:
            if loc[0] < minimum:
                minimum = loc[0]

    return minimum

def main():
    file_contents = ReadFile("Inputs.txt")
    answer = PartASolve(file_contents)
    print("Part A Answer: ", answer)
    answer = PartBSolve(file_contents)
    print("Part B Answer: ", answer)

if __name__ == "__main__":
    main()
