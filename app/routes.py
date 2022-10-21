from app import app
from flask import render_template

@app.route('/')
def homePage():
    characters = ['Pikachu', 'Bulbasaur', 'Charmander', 'Charizard', 'Kadabra', 'Spearow', 'Pidgeot', 'or so many others!!']
    
    
    
    return render_template('index.html', characters=characters)


@app.route('/pokemon')
def characterPage():
    
    
    
    url = 'https://pokeapi.co/'
    name = input("What pokemon are you looking for? ")
    url1 = f'{url}api/v2/pokemon/{name}'
    feedback = r.get(url1)
    if feedback.ok:
        data = feedback.json()
    ability = data['abilities'][0]['ability']['name']
    print(f"{name} has the {ability} ability")
    base_experience = data['base_experience']
    print(f"{name} has {base_experience} base experience")
    hp_stat = data['stats'][0]['base_stat']
    print(f"{name} has a {hp_stat} hp stat")
    attack_stat = data['stats'][1]['base_stat']
    print(f"{name} has a {attack_stat} attack stat")
    defense_stat = data['stats'][2]['base_stat']
    print(f"{name} has a {defense_stat} defense stat")
    front_shiny = data['sprites']['front_shiny']
    print(f"Here is the link, {front_shiny}, for a {name} image")
    
    

getPokemonInfo()
    
    
    
    
    return render_template('pokemon.html')