# Implementar una función que recibe un archivo y un número N y devuelva las primeras N líneas del archivo.
def readFirstNLines(filePath, n):
    try:
        with open(filePath, 'r', encoding='utf-8') as file:
            lines = []
            for i, line in enumerate(file):
                if i >= n:
                    break
                lines.append(line.strip())  
            return lines
    except FileNotFoundError:
        print(f"The file '{filePath}' was not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []


filePath = 'exampleFile.txt'  # No me encuentra el fichero
numberOfLines = 3
firstLines = readFirstNLines(filePath, numberOfLines)
print("\n".join(firstLines))