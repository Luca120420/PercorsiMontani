from neo4j import GraphDatabase

url = "neo4j+s://793c71a3.databases.neo4j.io"
username = "neo4j"
password = "E_OchQ6w3qMp6jPMSVd9rYJVjczHKUa-sRqy_smT8u8" 
driver = GraphDatabase.driver(url, auth=(username, password))

# Funzione per trovare il percorso più breve tra due rifugi
def find_shortest_path(tx, start_refuge, end_refuge, suitable_for_bike):
    if suitable_for_bike:
        result = tx.run("""
            MATCH (start:Refuge {name: $start_refuge}), (end:Refuge {name: $end_refuge})
            MATCH path = shortestPath((start)-[:ARRIVES_AT*]-(end))
            WHERE all(rel in relationships(path) WHERE rel.suitable_for_bike = true)
            RETURN path
        """, start_refuge=start_refuge, end_refuge=end_refuge)
    else:
        result = tx.run("""
            MATCH (start:Refuge {name: $start_refuge}), (end:Refuge {name: $end_refuge})
            MATCH path = shortestPath((start)-[:ARRIVES_AT*]-(end))
            RETURN path
        """, start_refuge=start_refuge, end_refuge=end_refuge)
    return result.single()

# Funzione per ottenere i sentieri da un percorso
def get_trails_from_path(tx, path):
    trails = []
    for i in range(len(path)-1):
        result = tx.run("""
            MATCH (s:Trail)-[:LEADS_TO]->(e:Trail)
            WHERE s.name = $start_trail AND e.name = $end_trail
            RETURN s.name, e.name
        """, start_trail=path[i], end_trail=path[i+1])
        record = result.single()
        if record:
            trails.append(record["s.name"])
        else:
            return None
    return trails

# Ottieni i sentieri per arrivare dal rifugio di partenza al rifugio di destinazione
def get_trails_between_refuges(start_refuge, end_refuge, suitable_for_bike):
    with driver.session() as session:
        result = session.read_transaction(find_shortest_path, start_refuge, end_refuge, suitable_for_bike)
        if result:
            path = [record["name"] for record in result["path"].nodes]
            trails = session.read_transaction(get_trails_from_path, path)
            return trails
        else:
            return None

# Funzione principale del programma
def main():
    start_refuge = input("Inserisci il rifugio di partenza: ")
    end_refuge = input("Inserisci il rifugio di destinazione: ")
    suitable_for_bike = input("Sei in bici? (S/N): ").upper() == "S"
    print(suitable_for_bike)

    trails = get_trails_between_refuges(start_refuge, end_refuge, suitable_for_bike)
    if trails:
        print(f"\nPercorso consigliato:")
        for i, trail in enumerate(trails, start=1):
            print(f"{i}. {trail}")
    else:
        print("Sentiero assente o percorso non trovato.")

# Esegui il programma
if __name__ == "__main__":
    main()

# Chiudi la connessione al database
driver.close()