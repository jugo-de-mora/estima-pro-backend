from neo4j import GraphDatabase

# Neo4j connection details
URI = "neo4j+ssc://bc0be911.databases.neo4j.io" 
USERNAME = "neo4j"            
PASSWORD = "0Q0zHyuv2OI1PWbuVApgpwjknVr6XM9GQhx_UlsYyjA"        
AUTH = (USERNAME, PASSWORD)

historiasUsuario = [{"nombre": "Inicio de sesión", "descripcion": "El sistema debe permitir acceder por medio de un usuario y contraseña."},
          {"nombre": "Notificaciones", "descripcion": "El sistema debe enviar notificaciones a los usuarios por correo electrónico."},]

with GraphDatabase.driver(URI, auth=AUTH) as driver:
    try:
        # Create some nodes
        for historia in historiasUsuario:
            records, summary, keys = driver.execute_query(
                "MERGE (h:HistoriaDeUsuario {nombre: $historia.nombre, descripcion: $historia.descripcion})",
                historia=historia,
                database_="neo4j",
            )

        # Create some relationships
        # for historia in historiasUsuario:
        #     if historia.get("friends"):
        #         records, summary, keys = driver.execute_query("""
        #             MATCH (p:historia {name: $historia.name})
        #             UNWIND $historia.friends AS friend_name
        #             MATCH (friend:historia {name: friend_name})
        #             MERGE (p)-[:KNOWS]->(friend)
        #             """, historia=historia,
        #             database_="neo4j",
        #         )

        records, summary, keys = driver.execute_query("""
            MATCH (p:HistoriaDeUsuario) RETURN p
            """, 
            routing_="r",
            database_="neo4j",
        )
        # Loop through results and do something with them
        for record in records:
            print(record.data())
        # Summary information
        # print("The query `{query}` returned {records_count} records in {time} ms.".format(
        #     query=summary.query, records_count=len(records),
        #     time=summary.result_available_after
        # ))

    except Exception as e:
        print(e)
        # further logging/processing