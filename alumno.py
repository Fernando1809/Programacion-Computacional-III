import conexion

miconexion =  conexion.conexion()

class alumno:
    def consultar(self):
        return miconexion.consultar("select * from alumnos")
    def administrar_alumnos(self,alumnos):
        if alumnos["accion"]=="nuevo":
            sql = """
            INSERT INTO alumnos(codigo, nombre, direccion, telefono)
            VALUES(%s,%s,%s,%s)
            """
            val = (alumnos["codigo"],alumnos["nombre"],alumnos["direccion"],alumnos["telefono"])
        elif alumno["accion"]== "modificar":
            sql = """
            UPDATE alumnos SET codigo=%s,nombre=%s,direccion=%s,telefono=%s)
            """
            val =(alumnos["codigo"],alumnos["nombre"],alumnos["direccion"],alumnos["telefono"])
        elif alumno["accion"]=="eliminar":
            sql= "DELETE FROM alumnos WHERE idAlumno=%s"
            val =(alumnos["idAlumno"])
        return miconexion.ejecutar_consulta(sql, val)