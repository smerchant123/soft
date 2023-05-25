from project01.manager import AdminPersonasManager
from project01.serializer import AdminPersonasSerializer

class AdminPersonasController():
    @staticmethod
    def get_all():
        return AdminPersonasManager.get_all()

    @staticmethod
    def save_persona(data):
        serializer = AdminPersonasSerializer(data = data)
        if serializer.is_valid():
            AdminPersonasManager.save_persona(serializer)
            return serializer
        return serializer

    @staticmethod
    def get_persona_by_id(pk):
        return AdminPersonasManager.get_persona_by_id(pk)

    @staticmethod
    def update_persona(data, pk):
        AdminPersonasManager.update_persona(data, pk)

    @staticmethod
    def delete_persona(pk):
        AdminPersonasManager.delete_persona(pk)