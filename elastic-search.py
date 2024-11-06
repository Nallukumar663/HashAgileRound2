from elasticsearch import Elasticsearch
import pandas as pd

# Connect to Elasticsearch
es = Elasticsearch(['http://localhost:8989'])

def createCollection(p_collection_name):
    es.indices.create(index=p_collection_name, ignore=400)

def indexData(p_collection_name, p_exclude_column):
    df = pd.read_csv('path_to_your_downloaded_dataset.csv')
    df = df.drop(columns=[p_exclude_column])  # Exclude specified column
    for index, document in df.iterrows():
        es.index(index=p_collection_name, id=index, document=document.to_dict())

def searchByColumn(p_collection_name, p_column_name, p_column_value):
    query = {
        "query": {
            "match": {
                p_column_name: p_column_value
            }
        }
    }
    return es.search(index=p_collection_name, body=query)

def getEmpCount(p_collection_name):
    return es.count(index=p_collection_name)['count']

def delEmpById(p_collection_name, p_employee_id):
    es.delete(index=p_collection_name, id=p_employee_id)

def getDepFacet(p_collection_name):
    query = {
        "size": 0,
        "aggs": {
            "departments": {
                "terms": {
                    "field": "Department.keyword"
                }
            }
        }
    }
    return es.search(index=p_collection_name, body=query)












v_nameCollection = 'Hash_Robert Patel'
v_phoneCollection = 'Hash_5703'

# a)
create_collection(v_nameCollection)
# b)
create_collection(v_phoneCollection)

# e) Get employee count
print("Employee count in v_nameCollection:", get_emp_count(v_nameCollection))

# f)
index_data(v_nameCollection, 'Department')

# g)
index_data(v_phoneCollection, 'Gender')

# h) Get employee count after indexing
print("Employee count after indexing in v_nameCollection:", get_emp_count(v_nameCollection))

# i) Delete employee by ID
del_emp_by_id(v_nameCollection, 'E02003')

# j) Get employee count after deletion
print("Employee count after deletion in v_nameCollection:", get_emp_count(v_nameCollection))

# k) Search in v_nameCollection by Department
print("Search in v_nameCollection by Department=IT:", search_by_column(v_nameCollection, 'Department', 'IT'))

# l) Search in v_nameCollection by Gender
print("Search in v_nameCollection by Gender=Male:", search_by_column(v_nameCollection, 'Gender', 'Male'))

# m) Search in v_phoneCollection by Department
print("Search in v_phoneCollection by Department=IT:", search_by_column(v_phoneCollection, 'Department', 'IT'))

# n) Department facet in v_nameCollection
print("Department facet in v_nameCollection:", get_dep_facet(v_nameCollection))

# o) Department facet in v_phoneCollection
print("Department facet in v_phoneCollection:", get_dep_facet(v_phoneCollection))