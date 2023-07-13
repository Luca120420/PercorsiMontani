from neo4j import GraphDatabase

# Crea la connessione al database Neo4j
url = "neo4j+s://793c71a3.databases.neo4j.io"
username = "neo4j"
password = "E_OchQ6w3qMp6jPMSVd9rYJVjczHKUa-sRqy_smT8u8" 
driver = GraphDatabase.driver(url, auth=(username, password))

# Funzione per creare la zona di montagna nel database
def create_mountain_zone(tx, name):
    tx.run("CREATE (:MountainZone {name: $name})", name=name)

# Funzione per creare un sentiero e collegarlo alla zona di montagna corrispondente
def create_trail(tx, name, mountain_zone, suitable_for_bike, duration, difficulty, starting_point):
    tx.run("""
        MATCH (m:MountainZone {name: $mountain_zone})
        CREATE (m)-[:HAS_TRAIL]->(:Trail {name: $name, suitable_for_bike: $suitable_for_bike, duration: $duration, difficulty: $difficulty, starting_point: $starting_point})
    """, name=name, mountain_zone=mountain_zone, suitable_for_bike=suitable_for_bike, duration=duration, difficulty=difficulty, starting_point=starting_point)

# Funzione per creare una relazione di arrivo tra un sentiero e un rifugio
def create_arrival(tx, trail, refuge):
    tx.run("""
        MATCH (t:Trail {name: $trail}), (r:Refuge {name: $refuge})
        CREATE (t)-[:ARRIVES_AT]->(r)
    """, trail=trail, refuge=refuge)

# Funzione per creare una relazione di collegamento tra due sentieri
def create_leads_to(tx, trail1, trail2):
    tx.run("""
        MATCH (t1:Trail {name: $trail1}), (t2:Trail {name: $trail2})
        CREATE (t1)-[:LEADS_TO]->(t2)
    """, trail1=trail1, trail2=trail2)
def create_refuge(tx, name, trails):
    tx.run("""
        MATCH (t:Trail)
        WHERE t.name IN $trails
        CREATE (t)-[:LEADS_TO]->(:Refuge {name: $name})
    """, name=name, trails=trails)

# Crea la zona di montagna, i sentieri e i rifugi nel database
def create_mountain_database():
    with driver.session() as session:
        session.write_transaction(create_mountain_zone, "Montagna A")

        # Crea i sentieri
        session.write_transaction(create_trail, "Sentiero 1", "Montagna A", True, 120, "Facile", "Punto A")
        session.write_transaction(create_trail, "Sentiero 2", "Montagna A", False, 90, "Medio", "Punto B")
        session.write_transaction(create_trail, "Sentiero 3", "Montagna A", True, 180, "Difficile", "Punto C")
        session.write_transaction(create_trail, "Sentiero 4", "Montagna A", True, 150, "Medio", "Punto D")
        session.write_transaction(create_trail, "Sentiero 5", "Montagna A", False, 120, "Difficile", "Punto E")
        # Aggiungi altri sentieri qui...

        # Crea i rifugi
        session.write_transaction(create_refuge, "Rifugio 1", ["Sentiero 1", "Sentiero 2"])
        session.write_transaction(create_refuge, "Rifugio 2", ["Sentiero 2", "Sentiero 3"])
        session.write_transaction(create_refuge, "Rifugio 3", ["Sentiero 3", "Sentiero 4"])
        session.write_transaction(create_refuge, "Rifugio 4", ["Sentiero 4", "Sentiero 5"])
        session.write_transaction(create_refuge, "Rifugio 5", ["Sentiero 5", "Sentiero 1"])
        # Aggiungi altri rifugi qui...

        # Crea le relazioni di arrivo ai rifugi
        session.write_transaction(create_arrival, "Sentiero 1", "Rifugio 1")
        session.write_transaction(create_arrival, "Sentiero 2", "Rifugio 1")
        session.write_transaction(create_arrival, "Sentiero 2", "Rifugio 2")
        session.write_transaction(create_arrival, "Sentiero 3", "Rifugio 2")
        session.write_transaction(create_arrival, "Sentiero 3", "Rifugio 3")
        session.write_transaction(create_arrival, "Sentiero 4", "Rifugio 3")
        session.write_transaction(create_arrival, "Sentiero 4", "Rifugio 4")
        session.write_transaction(create_arrival, "Sentiero 5", "Rifugio 4")
        session.write_transaction(create_arrival, "Sentiero 5", "Rifugio 5")
        session.write_transaction(create_arrival, "Sentiero 1", "Rifugio 5")
        # Aggiungi altre relazioni di arrivo qui...

        # Crea le relazioni di collegamento tra sentieri
        session.write_transaction(create_leads_to, "Sentiero 1", "Sentiero 2")
        session.write_transaction(create_leads_to, "Sentiero 2", "Sentiero 3")
        session.write_transaction(create_leads_to, "Sentiero 3", "Sentiero 4")
        session.write_transaction(create_leads_to, "Sentiero 4", "Sentiero 5")
        session.write_transaction(create_leads_to, "Sentiero 5", "Sentiero 1")
        # Aggiungi altre relazioni di collegamento qui...

        # Aggiungi altri sentieri e relazioni
        session.write_transaction(create_trail, "Sentiero 6", "Montagna A", True, 120, "Facile", "Punto F")
        session.write_transaction(create_trail, "Sentiero 7", "Montagna A", False, 90, "Medio", "Punto G")
        session.write_transaction(create_trail, "Sentiero 8", "Montagna A", True, 180, "Difficile", "Punto H")
        session.write_transaction(create_trail, "Sentiero 9", "Montagna A", True, 150, "Medio", "Punto I")
        session.write_transaction(create_trail, "Sentiero 10", "Montagna A", False, 120, "Difficile", "Punto J")
        # Aggiungi altri sentieri qui...

        # Crea le nuove relazioni di arrivo ai rifugi
        session.write_transaction(create_arrival, "Sentiero 6", "Rifugio 1")
        session.write_transaction(create_arrival, "Sentiero 7", "Rifugio 2")
        session.write_transaction(create_arrival, "Sentiero 8", "Rifugio 3")
        session.write_transaction(create_arrival, "Sentiero 9", "Rifugio 4")
        session.write_transaction(create_arrival, "Sentiero 10", "Rifugio 5")
        # Aggiungi altre relazioni di arrivo qui...

        # Crea le nuove relazioni di collegamento tra sentieri
        session.write_transaction(create_leads_to, "Sentiero 6", "Sentiero 7")
        session.write_transaction(create_leads_to, "Sentiero 7", "Sentiero 8")
        session.write_transaction(create_leads_to, "Sentiero 8", "Sentiero 9")
        session.write_transaction(create_leads_to, "Sentiero 9", "Sentiero 10")
        session.write_transaction(create_leads_to, "Sentiero 10", "Sentiero 6")
        # Aggiungi altre relazioni di collegamento qui...

# Esegui la creazione del database
create_mountain_database()

# Chiudi la connessione al database
driver.close()
