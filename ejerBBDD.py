import sqlite3

# Implementar una función para crear una base de datos SQLite con dos tablas:
def createDatabase(dbName):
    conn = sqlite3.connect(dbName)
    cursor = conn.cursor()
    
    # Categorias
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS categories (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(100) UNIQUE NOT NULL
    )
    """)
    
    # Cursos
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS courses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(100) UNIQUE NOT NULL,
        category_id INTEGER NOT NULL,
        FOREIGN KEY(category_id) REFERENCES categories(id)
    )
    """)
    
    conn.commit()
    conn.close()

# Implementar una función que reciba un nombre de categoría (Fácil, Intermedio, Avanzado) y creará un nuevo registro en la tabla categorías.
def addCategory(dbName, categoryName):
    try:
        conn = sqlite3.connect(dbName)
        cursor = conn.cursor()
        
        cursor.execute("INSERT INTO categories (name) VALUES (?)", (categoryName,))
        conn.commit()
        print(f"New category: '{categoryName}' added successfully.")
    
    except sqlite3.IntegrityError:
        print(f"The category '{categoryName}' already exists.")
    
    except Exception as e:
        print(f"{e}")
    
    finally:
        conn.close()

# Implementar una función que reciba el nombre de un curso y un nombre categoría y creará un nuevo registro en la tabla de cursos.
def addCourse(dbName, courseName, categoryName):
    try:
        conn = sqlite3.connect(dbName)
        cursor = conn.cursor()
        
        cursor.execute("SELECT id FROM categories WHERE name = ?", (categoryName,))
        category = cursor.fetchone()
        
        if category is None:
            print(f"The category '{categoryName}' does not exist.")
            return
        
        categoryId = category[0]
        
        cursor.execute("INSERT INTO courses (name, category_id) VALUES (?, ?)", (courseName, categoryId))
        conn.commit()
        print(f"New course: '{courseName}' added successfully under category '{categoryName}'.")
    
    except sqlite3.IntegrityError:
        print(f"The course '{courseName}' already exists.")
    
    except Exception as e:
        print(f"{e}")
    
    finally:
        conn.close()

# Implementar una función que reciba un nombre de categoría y devolverá una lista con todos los cursos asociados a esa categoría.
def getCoursesByCategory(dbName, categoryName):
    try:
        conn = sqlite3.connect(dbName)
        cursor = conn.cursor()
        
        cursor.execute("SELECT id FROM categories WHERE name = ?", (categoryName,))
        category = cursor.fetchone()
        
        if category is None:
            print(f"The category '{categoryName}' does not exist.")
            return []
        
        categoryId = category[0]
        
        cursor.execute("SELECT name FROM courses WHERE category_id = ?", (categoryId,))
        courses = cursor.fetchall()
        
        return [course[0] for course in courses]
    
    except Exception as e:
        print(f"{e}")
        return []
    
    finally:
        conn.close()

if __name__ == "__main__":
    dbName = "courses.db"
    
    # Crear BBDD y tablas
    createDatabase(dbName)
    
    # Añadir categorias
    addCategory(dbName, "Fácil")
    addCategory(dbName, "Intermedio")
    addCategory(dbName, "Avanzado")
    
    # Añadir cursos
    addCourse(dbName, "Base de datos", "Fácil")
    addCourse(dbName, "Programación", "Intermedio")
    addCourse(dbName, "Sistemas informaticos", "Avanzado")
    addCourse(dbName, "Acceso a datos", "Avanzado")
    
    # Devolver cursos por categoria
    categoryName = input("Enter category name (e.g., 'Fácil', 'Intermedio', 'Avanzado'): ")
    courses = getCoursesByCategory(dbName, categoryName)
    print(f"Courses under '{categoryName}':", courses)
