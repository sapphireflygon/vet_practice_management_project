from unittest import result
from db.run_sql import run_sql
from models.vet import Vet

# List all vets in database
def select_all():
    vets = []
    sql = "SELECT * FROM vets"
    results = run_sql(sql)
    for result in results:
        vet = Vet(result["id"], result["name"])
        vets.append(vet)
    return vets


# Find one vet in database
def select(id):
    sql = "SELECT * FROM vets WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)
    vet = Vet(result["id"], result["name"])
    return vet


# Create new vet in database
def save(vet):
    sql = "INSERT INTO vets (name) VALUES (%s) RETURNING id"
    values = [vet.name]
    result = run_sql(sql, values)
    vet.id = result[0]["id"]