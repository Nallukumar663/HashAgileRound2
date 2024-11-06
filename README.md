
---

# Employee Data Management with Elasticsearch

This project demonstrates the use of Elasticsearch for managing employee data, including creating collections, indexing data, retrieving specific employee records, and performing aggregations. The project utilizes the [Elasticsearch Python client](https://www.elastic.co/guide/en/elasticsearch/client/python-api/current/index.html) to interact with the Elasticsearch server.

## Prerequisites

1. **Install Elasticsearch**: Follow the [Elasticsearch: Getting Started](https://www.elastic.co/guide/en/elasticsearch/reference/current/getting-started.html) guide.
   
2. **Set up Elasticsearch on Port 8989**: 
   - Modify the `elasticsearch.yml` file to change the default port (9200) to 8989.
   
3. **Download Employee Dataset**:
   - Download the employee dataset from [Kaggle](https://www.kaggle.com/datasets/williamlucas0/employee-sample-data).
   - Place the CSV file in the project directory and update its path in the `indexData` function.

4. **Install Required Python Packages**:
   - Install the necessary libraries:
     ```bash
     pip install elasticsearch pandas
     ```

## Functions

The project includes several functions implemented to interact with the employee data in Elasticsearch. Here is a description of each function:

### 1. `createCollection(p_collection_name)`

- **Purpose**: Creates an Elasticsearch index (collection) with the specified name.
- **Parameters**:
  - `p_collection_name`: Name of the collection to be created.

### 2. `indexData(p_collection_name, p_exclude_column)`

- **Purpose**: Indexes data from the employee dataset into a specified collection, excluding a specific column.
- **Parameters**:
  - `p_collection_name`: Name of the collection where data is to be indexed.
  - `p_exclude_column`: Column name to exclude from indexing.

### 3. `searchByColumn(p_collection_name, p_column_name, p_column_value)`

- **Purpose**: Searches for documents in a collection where a specified column matches a given value.
- **Parameters**:
  - `p_collection_name`: Name of the collection to search in.
  - `p_column_name`: Column name to filter on.
  - `p_column_value`: Value to search for in the specified column.

### 4. `getEmpCount(p_collection_name)`

- **Purpose**: Retrieves the count of documents in the specified collection.
- **Parameters**:
  - `p_collection_name`: Name of the collection to count documents.

### 5. `delEmpById(p_collection_name, p_employee_id)`

- **Purpose**: Deletes a document from the collection by its ID.
- **Parameters**:
  - `p_collection_name`: Name of the collection to delete from.
  - `p_employee_id`: ID of the employee to delete.

### 6. `getDepFacet(p_collection_name)`

- **Purpose**: Aggregates the data to retrieve a count of employees grouped by department.
- **Parameters**:
  - `p_collection_name`: Name of the collection to perform the aggregation on.

## Execution Steps

After implementing the functions, execute them in the following order:

### 1. Variable Declarations

- Declare variables for collection names:
  - `v_nameCollection = 'Hash_<Your Name>'`
  - `v_phoneCollection = 'Hash_<Your Phone last four digits>'`

### 2. Function Executions

- **Create Collections**:
  ```python
  createCollection(v_nameCollection)
  createCollection(v_phoneCollection)
  ```

- **Get Employee Count**:
  ```python
  print("Employee count in v_nameCollection:", getEmpCount(v_nameCollection))
  ```

- **Index Data**:
  - Exclude the 'Department' column in `v_nameCollection`.
  - Exclude the 'Gender' column in `v_phoneCollection`.
  ```python
  indexData(v_nameCollection, 'Department')
  indexData(v_phoneCollection, 'Gender')
  ```

- **Get Employee Count After Indexing**:
  ```python
  print("Employee count after indexing in v_nameCollection:", getEmpCount(v_nameCollection))
  ```

- **Delete Employee by ID**:
  ```python
  delEmpById(v_nameCollection, 'E02003')
  ```

- **Get Employee Count After Deletion**:
  ```python
  print("Employee count after deletion in v_nameCollection:", getEmpCount(v_nameCollection))
  ```

- **Search by Column**:
  - Search `v_nameCollection` for employees in the 'IT' department.
  - Search `v_nameCollection` for male employees.
  - Search `v_phoneCollection` for employees in the 'IT' department.
  ```python
  print("Search in v_nameCollection by Department=IT:", searchByColumn(v_nameCollection, 'Department', 'IT'))
  print("Search in v_nameCollection by Gender=Male:", searchByColumn(v_nameCollection, 'Gender', 'Male'))
  print("Search in v_phoneCollection by Department=IT:", searchByColumn(v_phoneCollection, 'Department', 'IT'))
  ```

- **Get Department Facet**:
  - Retrieve department-wise employee count in both collections.
  ```python
  print("Department facet in v_nameCollection:", getDepFacet(v_nameCollection))
  print("Department facet in v_phoneCollection:", getDepFacet(v_phoneCollection))
  ```

## Screenshots

Capture screenshots after each step and save them in a folder named `screenshots`.

1. `createCollection(v_nameCollection)`
2. `createCollection(v_phoneCollection)`
3. `getEmpCount(v_nameCollection)`
4. `indexData(v_nameCollection, 'Department')`
5. `indexData(v_phoneCollection, 'Gender')`
6. `getEmpCount(v_nameCollection)`
7. `delEmpById(v_nameCollection, 'E02003')`
8. `getEmpCount(v_nameCollection)`
9. `searchByColumn(v_nameCollection, 'Department', 'IT')`
10. `searchByColumn(v_nameCollection, 'Gender', 'Male')`
11. `searchByColumn(v_phoneCollection, 'Department', 'IT')`
12. `getDepFacet(v_nameCollection)`
13. `getDepFacet(v_phoneCollection)`

## Notes

- Ensure Elasticsearch is running on port 8989 before executing the script.
- Replace `'path_to_your_downloaded_dataset.csv'` with the actual path to your employee dataset file in the `indexData` function.
- Adjust error handling for Elasticsearch connection issues if needed.

---

