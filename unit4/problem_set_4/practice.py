
def subway(**lines):
    for color, stations in lines.items():
        lines[color] = stations.strip().split(' ')
    subway_map = dict([(s, {}) for stations in lines.values() for s in stations ])
    print subway_map
    for station_list in lines.values():
        for index, station in enumerate(station_list):
            if index == (len(station_list) - 1) :
                continue
            station_map, neighbor = subway_map[station], station_list[index+1]
            neighbor_map = subway_map[neighbor]
            station_map[neighbor] = [ color for color, rail in lines.items() if neighbor in rail ]
            neighbor_map[station] = [ color for color, rail in lines.items() if station in rail ]
    print "#####"
    print subway_map

    #for line, stations in lines.items():

boston = subway(red="monroe madison michigan sagan belleview",
              blue="morrison michigan pikachu hathaway corona ",
              pink="hang sour madison corona venice")
