import csv
import matplotlib.pyplot as plt

INDIA_YEAR_TO_POPULATION={}
ASEAN_COUNTRY_TO_POPULATION={}
ASEAN_COUNTRIES=["Brunei Darussalam","Cambodia","Indonesia","Malaysia","Myanmar","Phillipenes","Singapore","Thailand","Vietnam"]
SAARC_COUNTRIES=["Afganistan","Bangladesh","Bhutan","India","Maldives","Nepal","Sri Lanka"]
SAARC_COUNTRY_TO_POPULATION={}
ASEAN_BY_YEAR={}
colors=["forestgreen","darkorange","maroon","lightcoral","cyan","goldenrod","magenta","black","tomato","tan"]

def calculate():
    with open("data/pop.csv",encoding='utf-8') as csv_file:
        population_reader=csv.DictReader(csv_file)
        for population in population_reader:
            if population["Region"]=="India":
                if population["Year"] not in INDIA_YEAR_TO_POPULATION:
                    INDIA_YEAR_TO_POPULATION[population["Year"]]=float(population["Population"])
            if population["Year"]=="2014":
                if population["Region"] in ASEAN_COUNTRIES:
                    ASEAN_COUNTRY_TO_POPULATION[population["Region"]]=float(population["Population"])
            if population["Region"] in SAARC_COUNTRIES:
                if population["Region"] not in SAARC_COUNTRY_TO_POPULATION:
                    SAARC_COUNTRY_TO_POPULATION[population["Region"]]=float(population["Population"])
                else:
                    SAARC_COUNTRY_TO_POPULATION[population["Region"]]+=float(population["Population"])
            start="2004"
            end="2014"        
            if population["Year"]>=start and population["Year"]<=end:                     
                if population["Region"] in ASEAN_COUNTRIES:
                    if population["Year"] not in ASEAN_BY_YEAR:
                        country_to_population={"Brunei Darussalam":0,"Cambodia":0,"Indonesia":0,"Malaysia":0,"Myanmar":0,"Phillipenes":0,"Singapore":0,"Thailand":0,"Vietnam":0}
                        country_to_population[population["Region"]]=float(population["Population"])
                        ASEAN_BY_YEAR[population["Year"]]=country_to_population
                    else:
                        ASEAN_BY_YEAR[population["Year"]][population["Region"]]+=float(population["Population"])
                


def india_population_over_years():
    """This function plots a bar chart of showing population trends in india over the years"""
    year=list(INDIA_YEAR_TO_POPULATION.keys())
    population=list(INDIA_YEAR_TO_POPULATION.values())
    year,population=zip(*sorted(zip(year,population)))
    plt.bar(year,population,color='maroon')
    plt.xticks(rotation=40)
    plt.ylabel("Population")
    plt.xlabel("Years")
    plt.title("Population growth of India over the years")
    plt.show()

def asean_population():
    """This function plots a bar char of ASEAN country vs their populations in the year 2014"""
    country=list(ASEAN_COUNTRY_TO_POPULATION.keys())
    population=list(ASEAN_COUNTRY_TO_POPULATION.values())
    plt.bar(country,population,color='maroon')
    plt.xticks(rotation=30)
    plt.xlabel("Countries")
    plt.ylabel("Populations")
    plt.title("Population of ASEAN countries in 2014")
    plt.show()

def saarc_population():
    """This function plots a bar chart of SAARC country vs their population in all years"""
    country=list(SAARC_COUNTRY_TO_POPULATION.keys())
    population=list(SAARC_COUNTRY_TO_POPULATION.values())
    plt.bar(country,population,color='maroon')
    plt.xlabel("Countries")
    plt.ylabel("Population")
    plt.title("The population of saarc countries in all years")
    plt.xticks(rotation=30)
    plt.show()


def asean_population_over_year():
    """This function plots a grouped bar chart of ASEAN countries over the years"""
    color_count=0
    Years=list(ASEAN_BY_YEAR.keys())
    width=0.10
    k=-5
    dynamic_width=[i for i in range(9)]
    color_count=0
    print(ASEAN_BY_YEAR)
    for countries in ASEAN_BY_YEAR:
        population=list(ASEAN_BY_YEAR[countries].values())
        print(population)
        plt.bar([i+(k*width) for i in dynamic_width],population,width)
        k+=1
    plt.xticks(rotation=45)
    plt.xticks(dynamic_width,ASEAN_COUNTRIES)
    plt.xlabel("Years")
    plt.ylabel("Population")
    plt.title("Grouped bar plot showcasing the growth of ASEAN countries over the years")
    plt.legend(Years)
    plt.show()


def main():
    calculate()
    while True:
        print("Please enter the corresponding number to select an option")
        print("1. Plot a bar chart of India's population over the years")
        print("2. Plot a bar chart comparing the population of ASEAN countries in 2014")
        print("3. Plot a bar chart of total saarc population vs years")
        print("4. Plot a grouped bar chart of ASEAN countries over the years")

        choice=int(input())
        if choice==1:
            india_population_over_years()
        elif choice==2:
            asean_population()
        elif choice==3:
            saarc_population()
        elif choice==4:
            asean_population_over_year()
        else:
            break

if __name__=="__main__":
    main()