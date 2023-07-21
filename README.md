# Readme - Programma 1: Creazione di una base di dati di sentieri montani con Neo4j

Questo programma utilizza il database graph-oriented Neo4j per creare una base di dati di sentieri montani e rifugi collegati. Utilizzando la libreria neo4j di Python, il programma si connette a un'istanza di Neo4j specificata tramite URL, nome utente e password. Successivamente, vengono definite le classi e i metodi per la creazione della base di dati.

Il programma consiste di due parti principali:

1. La classe SentieriMontani che contiene i metodi per creare le zone montane, i sentieri e i rifugi, nonché le relazioni tra di essi.
2. Il blocco if __name__ == "__main__": che istanzia un oggetto SentieriMontani, crea la base di dati richiamando il metodo create_mountain_database(), e chiude la connessione al database una volta terminata l'esecuzione.
## Istruzioni per l'esecuzione:

1. Assicurarsi di aver installato la libreria neo4j di Python.
2. Avviare un'istanza di Neo4j sulla piattaforma desiderata e ottenere l'URL del database, nome utente e password per l'autenticazione.
3. Incollare l'URL, nome utente e password nel codice Python nella variabile url, username e password, rispettivamente.
4. Eseguire il programma. Sarà creata una base di dati di esempio contenente zone montane, sentieri e rifugi con relazioni tra di essi.

# Readme - Programma 2: Trova percorsi tra rifugi montani con Neo4j

Questo programma utilizza il database graph-oriented Neo4j per trovare i percorsi tra due rifugi montani specificati dall'utente. Utilizzando la libreria neo4j di Python, il programma si connette a un'istanza di Neo4j specificata tramite URL, nome utente e password. Successivamente, viene definito il metodo find_paths_between_refuges() per eseguire la query di ricerca dei percorsi.

Il programma offre la possibilità di specificare se si desidera percorsi idonei per le biciclette o percorsi solo per i pedoni. Una volta trovati i percorsi, vengono restituiti i nomi dei nodi del grafo corrispondenti ai rifugi che compongono ciascun percorso.

## Istruzioni per l'esecuzione:

Assicurarsi di aver installato la libreria neo4j di Python.
Avviare un'istanza di Neo4j sulla piattaforma desiderata e ottenere l'URL del database, nome utente e password per l'autenticazione.
Incollare l'URL, nome utente e password nel codice Python nella variabile url, username e password, rispettivamente.
Eseguire il programma.
Inserire il nome del rifugio di partenza, il nome del rifugio di arrivo e specificare se si desidera percorsi adatti per le biciclette (digitando 's') o solo per i pedoni (digitando 'n') quando richiesto.
Il programma troverà e visualizzerà i percorsi possibili tra i rifugi specificati.
Nota: Per utilizzare questo programma, la base di dati dei sentieri montani deve essere stata creata utilizzando il primo programma fornito.