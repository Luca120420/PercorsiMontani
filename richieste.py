from neo4j import GraphDatabase

url = "neo4j+s://793c71a3.databases.neo4j.io"
username = "neo4j"
password = "E_OchQ6w3qMp6jPMSVd9rYJVjczHKUa-sRqy_smT8u8"
driver = GraphDatabase.driver(url, auth=(username, password))


def find_paths_between_refuges(tx, start_refuge, end_refuge, bici):
      if bici == "s":
            result = tx.run("""
                  MATCH (start:Refuge {name: $start_refuge}), (end:Refuge {name: $end_refuge}),
                  path = shortestPath((start)-[:LEADS_TO*]-(end))
                  WHERE ALL(n IN nodes(path) WHERE n.suitable_for_bike = True)
                  RETURN [node IN nodes(path) | node.name] AS path_names
            """, start_refuge=start_refuge, end_refuge=end_refuge)
      else:

            result = tx.run("""
                  MATCH (start:Refuge {name: $start_refuge}), (end:Refuge {name: $end_refuge}),
                  path = shortestPath((start)-[:LEADS_TO*]-(end))
                  RETURN [node IN nodes(path) | node.name] AS path_names
            """, start_refuge=start_refuge, end_refuge=end_refuge)

      paths = result.single()
      if paths:
            paths = paths["path_names"]
            print(f"I percorsi tra il rifugio {start_refuge} e il rifugio {end_refuge} sono:")
            for path in paths:
                  print(path)
      else:
            if bici == "s":
                  print(f"Non esistono percorsi tra il rifugio {start_refuge} e il rifugio {end_refuge} per la bici.")
            else:
                  print(f"Non esistono percorsi tra il rifugio {start_refuge} e il rifugio {end_refuge}.")

while True:
      print("Inserisci il nome del rifugio di partenza e quello di arrivo, separati da una virgola (es. Rifugio 1,Rifugio 4) oppure premi invio per uscire.")
      start_refuge, end_refuge = input().split(",")
      bici = input("Vuoi usare la bici? (s/n)")
      if start_refuge == "":
            break
      with driver.session() as session:
            session.read_transaction(find_paths_between_refuges, start_refuge, end_refuge, bici)

driver.close()